import ApiManager from "../../helpers/ApiManager";

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
        staticUrl: $el.data('static-url') || '/static',
        csrfToken: $el.data('csrf-token'),
        products: null,
      },
      fetchProducts() {
        return ApiManager.getBaseProducts()
          .then(res => {
            this.state.products = res.data.results;
          });
      },
      postCalcPriceList(formValue) {
        return ApiManager.postCalcBasePriceList(formValue);
      },
      postEstimateProduct(formValue) {
        return ApiManager.postEstimateBaseProduct(formValue);
      },
      postAddCart(formValue) {
        return ApiManager.postAddCart(formValue);
      }
    };

    return this.store;
  }
}

export default new Store();
