import ApiManager from "../../helpers/ApiManager";
import EstimateProductCategory from "../../constants/EstimateProductCategory";
import EstimateFlow from "../../constants/EstimateFlow";
import objectizeQueryString from "../../helpers/objectizeQueryString";
import toEstimateProductCategory from "../../helpers/toEstimateProductCategory";
import {SMALL_LOT_QUANTITY_THRESHOLD} from "../../constants/Estimate";
import deepCopy from "../../helpers/deepCopy";

/**
 'height': 高さ
 'width': 幅
 'depth': 奥行き
 'color_num': 色数
 'quantity': 注文数
 'material': 素材(平袋)
 'print_area': 印刷面(ダンボール/紙器)
 'surface_material': 表面素材(ダンボール/紙器)
 'surface_process': 表面加工(ダンボール/紙器)
 'emboss': エンボス/デボス(紙器)
 'special_print': 特殊印刷(紙器)
 'bottom': 底(紙器)

 価格に関係ないもの
 'notch': ノッチ(平袋)
 'kadomaru': 角丸(平袋)
 'zipper': ジッパー(ダンボール)
 */

const getDefaultValue = extraInfo => {
  if (!extraInfo) {
    return null;
  }

  if (extraInfo.hasOwnProperty('default') && extraInfo.default) {
    return extraInfo.default;
  } else if (extraInfo.hasOwnProperty('value') && extraInfo.value) {
    return extraInfo.value;
  } else if (extraInfo.hasOwnProperty('options')) {
    const options = Object.entries(extraInfo.options);
    return options.length ? options[0][0] : null;
  }

  return null;
};

const OPTIONS_INITIAL_VALUE = '1';

class Store {
  constructor() {
    this.store = {};
  }

  getStore() {
    return this.store;
  }

  createStore($el) {
    this.store = {
      state: {
        productCategory: EstimateProductCategory.FLAT_BAG,
        flow: EstimateFlow.TOP,
        productSlug: $el.data('product-slug'),
        absoluteUrl: $el.data('absolute-url'),
        csrfToken: $el.data('csrf-token'),
        sizeFields: JSON.parse($el.data('size-fields').replace(/'/g, '"')),
        form: {
          size: OPTIONS_INITIAL_VALUE,
          freeSize: null,
          quantity: 0, // 注文数
          color_num: OPTIONS_INITIAL_VALUE, // 色数
          print_area: {
            outside: [],
            inside: []
          },
          material: OPTIONS_INITIAL_VALUE, // 素材(平袋)
          surface_material: OPTIONS_INITIAL_VALUE, // 表面素材(ダンボール/紙器)
          surface_process: OPTIONS_INITIAL_VALUE, // 表面加工(ダンボール/紙器)
          emboss: OPTIONS_INITIAL_VALUE, // エンボス/デボス(紙器)
          special_print: OPTIONS_INITIAL_VALUE, // 特殊印刷(紙器)
          bottom: OPTIONS_INITIAL_VALUE, // 底(紙器)
          notch: OPTIONS_INITIAL_VALUE, // ノッチ(平袋)
          kadomaru: OPTIONS_INITIAL_VALUE, // 角丸(平袋)
          zipper: OPTIONS_INITIAL_VALUE, // ジッパー(ダンボール)
        },
        editingForm: null,
        product: null,
        price: null,
        currentSelectingValStr: '', // 下層ページのfooterに表示するテキスト.
      },
      updateCurrentSelectingValStr(str) {
        this.state.currentSelectingValStr = str;
      },
      isSmallLot() {
        if (!this.state.product) {
          return false;
        }

        return this.state.product.extra_info.small_lot_availability.value &&
          this.state.form.quantity <= SMALL_LOT_QUANTITY_THRESHOLD;
      },
      getProductInfo() {
        return ApiManager.getProductInfo(this.state.productSlug)
          .then(res => {
            this.state.product = res.data;

            this.setProductCategory();

            this.initForm();
            this.initEditingForm();

            if (this.isSmallLot()) {
              this.overwriteToSmallLotColorOptions();
            }

            this.postCalcEstimate();
          });
      },
      overwriteToSmallLotColorOptions() {
        const extraInfo = this.state.product.extra_info;

        const matchOptions = Object.entries(extraInfo.small_lot_color.options)
          .filter(x => this.state.form.quantity >= x[1].min_quantity && this.state.form.quantity < x[1].max_quantity)
          .map(x => x[1].options);

        if (matchOptions.length) {
          extraInfo.color_num.options = matchOptions[0];
        }
      },
      setProductCategory() {
        this.state.productCategory = toEstimateProductCategory(this.state.product.main_category.slug);
      },
      initForm() {
        // 参照を代入.
        const extraInfos = this.state.product.extra_info;
        const queryParams = objectizeQueryString(location.search);

        const form = this.state.form;

        // ここでfilterされている属性は他の値の初期化方法とは統一できない.
        Object.keys(form)
          .filter(x =>
            x !== 'size' &&
            x !== 'freeSize' &&
            x !== 'quantity' &&
            x !== 'print_area' &&
            x !== 'notch' &&
            x !== 'kadomaru' &&
            x !== 'zipper'
          )
          .forEach(x => {
            if (extraInfos[x]) {
              form[x] = getDefaultValue(extraInfos[x]);
            }
          });

        // processは一階層深いので.
        if (extraInfos.process && extraInfos.process.options) {
          Object.keys(extraInfos.process.options)
            .forEach(x => {
              if (extraInfos.process.options[x]) {
                form[x] = getDefaultValue(extraInfos.process.options[x]);
              }
            })
        }

        // 印刷面をデフォルトで1面選ぶ!
        if (extraInfos.print_area && extraInfos.print_area.options) {
          Object.keys(extraInfos.print_area.options)
            .forEach(x => {
              if (extraInfos.print_area.options[x]) {
                const values = Object.keys(extraInfos.print_area.options[x].options);
                form.print_area[x] = [values[0]];
              }
            })
        }

        if (queryParams.hasOwnProperty('size') && queryParams.size !== '-1') {
          form.size = queryParams.size;
        } else {
          form.size = '-1';
          form.freeSize = Object.entries(this.state.sizeFields)
            .map(x => x[0])
            .reduce((obj, key) => {
              obj[key] = queryParams[key];
              return obj;
            }, {});
        }

        form.quantity = queryParams.quantity;
      },
      selectSizeInfo() {
        if (!this.state.product) {
          return null;
        }

        return this.state.product.extra_info.size;
      },
      selectColorInfo() {
        if (!this.state.product) {
          return null;
        }

        switch (this.state.productCategory) {
          case EstimateProductCategory.CARD_BOARD:
          case EstimateProductCategory.FLAT_BAG:
          case EstimateProductCategory.PAPER_BOX:
            return this.state.product.extra_info.color_num;
          default:
            return null;
        }
      },
      selectMaterialInfo() {
        if (!this.state.product) {
          return null;
        }

        switch (this.state.productCategory) {
          case EstimateProductCategory.FLAT_BAG:
            return this.state.product.extra_info.material;
          default:
            return null;
        }
      },
      selectPrintAreaInfo() {
        if (!this.state.product) {
          return null;
        }

        switch (this.state.productCategory) {
          case EstimateProductCategory.CARD_BOARD:
          case EstimateProductCategory.PAPER_BOX:
            return this.state.product.extra_info.print_area;
          default:
            return null;
        }
      },
      selectSurfaceMaterialInfo() {
        if (!this.state.product) {
          return null;
        }

        switch (this.state.productCategory) {
          case EstimateProductCategory.CARD_BOARD:
          case EstimateProductCategory.PAPER_BOX:
            return this.state.product.extra_info.surface_material;
          default:
            return null;
        }
      },
      selectSurfaceProcessInto() {
        if (!this.state.product) {
          return null;
        }

        switch (this.state.productCategory) {
          case EstimateProductCategory.CARD_BOARD:
          case EstimateProductCategory.PAPER_BOX:
            return this.state.product.extra_info.surface_process;
          default:
            return null;
        }
      },
      selectEmbossInfo() {
        if (!this.state.product) {
          return null;
        }

        switch (this.state.productCategory) {
          case EstimateProductCategory.PAPER_BOX:
            return this.state.product.extra_info.emboss;
          default:
            return null;
        }
      },
      selectProcessInfo() {
        if (!this.state.product) {
          return null;
        }

        switch (this.state.productCategory) {
          case EstimateProductCategory.FLAT_BAG:
          case EstimateProductCategory.CARD_BOARD:
            return this.state.product.extra_info.process;
          default:
            return null;
        }
      },
      selectSpecialPrintInfo() {
        if (!this.state.product) {
          return null;
        }

        switch (this.state.productCategory) {
          case EstimateProductCategory.PAPER_BOX:
            return this.state.product.extra_info.special_print;
          default:
            return null;
        }
      },
      selectBottomInfo() {
        if (!this.state.product) {
          return null;
        }

        switch (this.state.productCategory) {
          case EstimateProductCategory.PAPER_BOX:
            return this.state.product.extra_info.bottom;
          default:
            return null;
        }
      },
      getProcessValueStr(form) {
        const process = this.selectProcessInfo();

        if (!process) {
          return '';
        }

        return Object.entries(process.options)
          .map(type => {
            const formValue = form[type[0]];
            const typeValue = type[1];

            if (!typeValue.options || !typeValue.options[formValue]) {
              return null;
            }

            return typeValue.options[formValue].name;
          })
          .filter(x => x)
          .join(' / ');
      },
      getSurfaceValueStr(form) {
        let values = [];

        const material = this.selectSurfaceMaterialInfo();
        const process = this.selectSurfaceProcessInto();

        if (material === null && process === null) {
          return '';
        }

        const selectedMaterial = material ? material.options[form.surface_material] : null;
        const selectedProcess = process ? process.options[form.surface_process] : null;

        if (selectedMaterial) {
          values.push(selectedMaterial.name);
        }

        if (selectedProcess) {
          values.push(selectedProcess.name);
        }

        return values.join(' / ');
      },
      applyEditingForm() {
        if (this.state.editingForm) {
          this.state.form = {
            ...this.state.editingForm,
          };
        }
      },
      initEditingForm() {
        this.state.editingForm = deepCopy(this.state.form);
      },
      postCalcEstimate() {
        if (!this.state.product) {
          return Promise.resolve(null);
        }

        const requireFields = this.state.product.required_fields;

        // required_fieldsから必要なPOST情報のキーを取得.
        // ただし、sizeとquantityは抽出方法を統一できないのでこの時点では除外.
        const shouldPostExtraInfoKeys = requireFields
          .filter(x =>
            x !== 'height' &&
            x !== 'width' &&
            x !== 'depth' &&
            x !== 'lip' &&
            x !== 'top' &&
            x !== 'quantity' &&
            x !== 'outside' &&
            x !== 'inside' &&
            x !== 'kadomaru' &&
            x !== 'notch' &&
            x !== 'zipper'
          )
          .map(x => x);

        let formValue = shouldPostExtraInfoKeys
          .reduce((obj, key) => {
            obj[key] = this.state.product.extra_info[key].options[this.state.form[key]].value;
            return obj;
          }, {});

        // サイズと注文数とprint_areaをformValueに注入.

        formValue = {
          ...formValue,
          quantity: this.state.form.quantity,
        };

        if (requireFields.indexOf("inside") >= 0) {
          formValue = {
            ...formValue,
            inside: [...this.state.form.print_area.inside]
          };
        }

        if (requireFields.indexOf("outside") >= 0) {
          formValue = {
            ...formValue,
            outside: [...this.state.form.print_area.outside]
          };
        }

        if (requireFields.indexOf("kadomaru") >= 0) {
          formValue = {
            ...formValue,
            kadomaru: this.selectProcessInfo().options.kadomaru
              .options[this.state.form.kadomaru].value
          };
        }

        if (requireFields.indexOf("notch") >= 0) {
          formValue = {
            ...formValue,
            notch: this.selectProcessInfo().options.notch
              .options[this.state.form.notch].value
          };
        }

        if (requireFields.indexOf("zipper") >= 0) {
          formValue = {
            ...formValue,
            zipper: this.selectProcessInfo().options.zipper
              .options[this.state.form.zipper].value
          };
        }

        const sizeInfo = this.selectSizeInfo();
        const sizeFormVal = this.state.form.size;

        if (this.state.form.freeSize) {
          formValue = {
            ...formValue,
            ...this.state.form.freeSize,
          }
        } else if (sizeInfo.options[sizeFormVal]) {
          const sizeObj = sizeInfo.options[sizeFormVal].value
            .reduce((obj, sizeVal) => {
              obj[sizeVal.name] = sizeVal.value;
              return obj;
            }, {});

          formValue = {
            ...formValue,
            ...sizeObj,
          };
        } else {
          return Promise.resolve(null);
        }

        return ApiManager.postCalcEstimate(this.state.productSlug, formValue)
          .then(res => {
            this.state.price = res.data;
          });
      },
      postAddCart() {
        if (!this.state.product) {
          return Promise.resolve(null);
        }

        const cartFields = this.state.product.cart_fields;

        // ただし、sizeとquantityとprint_areaは抽出方法を統一できないのでこの時点では除外.
        const shouldPostExtraInfoKeys = cartFields
          .filter(x =>
            x !== 'height' &&
            x !== 'width' &&
            x !== 'depth' &&
            x !== 'lip' &&
            x !== 'top' &&
            x !== 'quantity' &&
            x !== 'outside' &&
            x !== 'inside' &&
            x !== 'kadomaru' &&
            x !== 'notch' &&
            x !== 'zipper'
          )
          .map(x => x);

        let priceVals = shouldPostExtraInfoKeys
          .reduce((obj, key) => {
            obj[key] = this.state.product.extra_info[key].options[this.state.form[key]].value;
            return obj;
          }, {});

        // サイズと注文数とprint_areaをformValueに注入.

        priceVals = {
          ...priceVals,
          quantity: this.state.form.quantity,
        };

        if (cartFields.indexOf("inside") >= 0) {
          priceVals = {
            ...priceVals,
            inside: [...this.state.form.print_area.inside]
          };
        }

        if (cartFields.indexOf("outside") >= 0) {
          priceVals = {
            ...priceVals,
            outside: [...this.state.form.print_area.outside]
          };
        }

        if (cartFields.indexOf("kadomaru") >= 0) {
          priceVals = {
            ...priceVals,
            kadomaru: this.selectProcessInfo().options.kadomaru
              .options[this.state.form.kadomaru].value
          };
        }

        if (cartFields.indexOf("notch") >= 0) {
          priceVals = {
            ...priceVals,
            notch: this.selectProcessInfo().options.notch
              .options[this.state.form.notch].value
          };
        }

        if (cartFields.indexOf("zipper") >= 0) {
          priceVals = {
            ...priceVals,
            zipper: this.selectProcessInfo().options.zipper
              .options[this.state.form.zipper].value
          };
        }

        const sizeInfo = this.selectSizeInfo();
        const sizeFormVal = this.state.form.size;

        if (this.state.form.freeSize) {
          priceVals = {
            ...priceVals,
            ...this.state.form.freeSize,
          }
        } else if (sizeInfo.options[sizeFormVal]) {
          const sizeObj = sizeInfo.options[sizeFormVal].value
            .reduce((obj, sizeVal) => {
              obj[sizeVal.name] = sizeVal.value;
              return obj;
            }, {});

          priceVals = {
            ...priceVals,
            ...sizeObj,
          };
        } else {
          return Promise.resolve(null);
        }

        const formValue = {
          product: this.state.productSlug,
          price_vals: priceVals
        };

        return ApiManager.postAddCart(formValue);
      }
    };

    return this.store;
  }
}

export default new Store();
