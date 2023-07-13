import axios from 'axios';
import ApiManager from "../../helpers/ApiManager";
import deepCopy from "../../helpers/deepCopy";
import toSizeJpName from "../../helpers/toSizeJpName";
import { reactive } from 'vue';

const CancelToken = axios.CancelToken;

class Store {
  constructor() {
    this.store = {};
  }

  getStore() {
    return this.store;
  }

  createStore($el) {
    this.store = reactive({
      state: {
        productSlug: $el.data('product-slug'),
        categorySlug: $el.data('category-slug'),
        contactUrl: $el.data('contact-url'),
        staticUrl: $el.data('static-url'),
        sizeFields: $el.data('size-fields') && typeof $el.data('size-fields') === "string" ? JSON.parse($el.data('size-fields').replace(/'/g, '"')) : {},
        isInitialized: false, // 初期化フラグ
        product: null, // 商品情報.
        price: null, // 現在の選択肢に基づく料金情報.
        isSubmitting: false, // 購入処理が実行中か.
        isEstimating: false, // 価格計算処理が実行中か.
        estimationCancelTokenSource: null,
        form: {}, // form情報. 商品情報を元に項目を生成.
      },
      async init() {
        await this.getProductInfo()
        this.state.isInitialized = true;
      },
      getDefaultItem(option) {
        if (option.slug == 'print_area_inside'){
          return option.items.find(item => item.is_default);
        } else {
          return option.items.find(item => item.is_default) || option.items[0];
        }
      },
      getSizeOptionHasDepth() {
        const sizeOption = this.getOptionBySlug('size');
        const defaultItem = this.getDefaultItem(sizeOption);
        return defaultItem.value.split(defaultItem.delimiter).length === 3;
      },
      getProductInfo() {
        return ApiManager.getProductInfo(this.state.productSlug)
          .then(res => {
            this.state.product = res.data;
          });
      },
      getOptionBySlug(slug) {
        return this.state.product.options.find(option => option.slug === slug);
      },
      postEstimate() {
        if (this.state.estimationCancelTokenSource) {
          this.state.estimationCancelTokenSource.cancel();
          this.state.estimationCancelTokenSource = null;
        }
        this.state.estimationCancelTokenSource = CancelToken.source();

        this.state.isEstimating = true;
        this.state.price = null;

        const options = deepCopy(this.state.form);
        delete options.quantity;

        const quantityItems = this.getOptionBySlug('quantity').items;
        const formData = {
          options,
          lots: quantityItems.map(item => item.value.replace(',', '')),
          listed: true
        };

        return ApiManager.postCalcEstimateList(this.state.productSlug, formData, this.state.estimationCancelTokenSource.token)
          .then(res => {
            this.state.price = res.data.prices;
          })
          .finally(() => {
            this.state.isEstimating = false;
            this.state.estimationCancelTokenSource = null;
          });
      },
      postAddCart() {
        if (this.state.isSubmitting) {
          return Promise.then();
        }

        this.state.isSubmitting = true;

        const formData = {
          product: this.state.productSlug,
          options: deepCopy(this.state.form)
        };

        return ApiManager.postAddCart(formData);
      },
      canSelectOriginalSize() {
        if (!this.state.product) {
          return false;
        }

        return this.state.product.info.can_select_original_size;
      },
      isSizeNotSelected() {
        return !this.state.product || !this.state.form.size || Object.values(this.state.form.size).every(x => x === null);
      },
      getSizeFormVal(sizeItem) {
        if (sizeItem.position === 0) {
          return sizeItem.value;
        }
        const sizeItemValues = sizeItem.value.split(sizeItem.delimiter).map(value => Number(value));
        let formVal = {
          width: sizeItemValues[0]
        };
        if (this.getSizeOptionHasDepth()) {
          formVal.depth = sizeItemValues[1]
          formVal.height = sizeItemValues[2]
        }
        else {
          formVal.height = sizeItemValues[1]
        }
        return formVal;
      },
      getCurrentSelectedSizeOption() {
        if (this.isSizeNotSelected()) {
          return null;
        }

        const sizeOption = this.getOptionBySlug('size');

        const matchValue = sizeOption.items.find(item => {
          const formVal = this.state.form.size;
          const itemFormVal = this.getSizeFormVal(item);
          const checkTargetKeys = ['width', 'height', 'depth'];
          return checkTargetKeys.every(key => formVal[key] === itemFormVal[key]);
        }) || null;

        return matchValue;
      },
      getSizeValStr() {
        const currentSizeOption = this.getCurrentSelectedSizeOption();

        if (!currentSizeOption) {
          return '-';
        }

        if(currentSizeOption.position !== 0) {
          return `${currentSizeOption.name} ${currentSizeOption.detail}`;
        }
        return `${currentSizeOption.name} ${Object.keys(currentSizeOption.value).map(key => `${toSizeJpName(key)} ${currentSizeOption.value[key]}mm`).join(' ')}`;
      },
      isMeetCondition(condition) {
        if (!condition || 0 === condition.length) {
          return true;
        }

        let isValid = true;
        for (const rule of condition) {
          const targetFormValue = this.state.form[rule.option];
          isValid = isValid && rule.values.includes(targetFormValue);
        }

        return isValid;
      }
    });

    return this.store;
  }
}

export default new Store();
