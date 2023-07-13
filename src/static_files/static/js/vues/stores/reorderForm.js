import axios from 'axios';
import ApiManager from "../../helpers/ApiManager";
import deepCopy from "../../helpers/deepCopy";
import { reactive } from "vue";

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
        refCode: $el.data('ref-code'),
        staticUrl: $el.data('static-url'),
        orderInfo: null,
        productSlug: null,
        isInitialized: false,
        product: null, // 商品情報.
        price: null, // 現在の選択肢に基づく料金情報.
        isSubmitting: false, // 購入処理が実行中か.
        isEstimating: false, // 価格計算処理が実行中か.
        form: {
          quantity: '',
        },
        estimationCancelTokenSource: null,
      },
      init() {
        return this.getOrderInfo()
          .then(() => {
            this.state.isInitialized = true;
          })
      },
      getOrderInfo() {
        return ApiManager.getReorderInfo(this.state.refCode).then((res) => {
          this.state.orderInfo = res.data;
          this.state.productSlug = res.data.product_slug;
        });
      },
      async postEstimate(quantity) {
        if (this.state.estimationCancelTokenSource) {
          this.state.estimationCancelTokenSource.cancel();
          this.state.estimationCancelTokenSource = null;
        }
        this.state.isEstimating = true;
        this.state.price = null;
        this.state.estimationCancelTokenSource = CancelToken.source();

        const formData = {
          ...this.state.orderInfo.extra_info,
          quantity: quantity,
          reordered: true,
        };

        const { data } =  await ApiManager.postCalcEstimate(this.state.productSlug, formData, this.state.estimationCancelTokenSource.token)
        this.state.price = data;
        this.state.isEstimating = false;
        this.state.estimationCancelTokenSource = null;
      },
      async postReorder(quantity) {
        if (this.state.isSubmitting) {
          return
        }

        this.state.isSubmitting = true;

        const formData = {
          ...this.state.orderInfo.extra_info,
          quantity: quantity,
          reordered: true,
        } ;

        await ApiManager.postReorder(this.state.refCode, formData);
        this.state.isSubmitting = false;
      }
    });
    return this.store;
  }
}

export default new Store();
