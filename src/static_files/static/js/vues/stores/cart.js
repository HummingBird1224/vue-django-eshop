import ApiManager from "../../helpers/ApiManager";
import { reactive } from "vue";
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
        staticUrl: $el.data('static-url'),
        csrfToken: $el.data('csrf-token'),
        isInitialized: false,
        cart: null
      },
      init() {
        return ApiManager.getCart()
          .then(res => {
            this.state.cart = res.data
            this.state.isInitialized = true;
          })
      },
      postCartItemDelete(itemId) {
        const formData = {
          item_id: itemId
        };

        return ApiManager.postCartItemDelete(formData).then((res) => {
          this.state.cart = res.data
        }).catch((err) => {
          console.log(err)
        });
      },
    });

    return this.store;
  }
}

export default new Store();
