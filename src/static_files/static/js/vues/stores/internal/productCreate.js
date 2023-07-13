import axios from 'axios';
import ApiManager from "../../../helpers/ApiManager";

const CancelToken = axios.CancelToken;

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
        categories: null,
        tags: null,
        isInitialized: false,
      },
      init() {
        return this.getCatNTags()
          .then(() => {
            this.state.isInitialized = true;
          });
      },
      createProduct(formValue) {
        return ApiManager.postInternalProductCreate(formValue);
      },
      getCatNTags() {
        return ApiManager.getInternalProductCreateCatNTagList()
          .then(res => {
            this.state.categories = res.data.categories;
            this.state.tags = res.data.tags;
          })
      }
    };

    return this.store;
  }
}

export default new Store();
