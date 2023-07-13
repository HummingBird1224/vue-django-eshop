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
        isOpen: false,
        productSlug: $el.data('product-slug'),
        cardboardColors: null
      },
      fetchColors() {
        if (!this.state.productSlug) {
          return Promise.resolve();
        }

        return ApiManager.getProductInfo(this.state.productSlug)
          .then(res => {
            if (res.data.hasOwnProperty('cardboard_colors')) {
              this.state.cardboardColors = res.data.cardboard_colors;
            }
          });
      },
      openModal() {
        this.state.isOpen = true;
      },
      closeModal() {
        this.state.isOpen = false;
      }
    };

    return this.store;
  }
}

export default new Store();
