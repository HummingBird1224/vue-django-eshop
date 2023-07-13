import ApiManager from "../../helpers/ApiManager"
import objectizeQueryString from "../../helpers/objectizeQueryString"
import { reactive } from "vue";
class Store {
  constructor() {
    this.store = {}
  }

  getStore() {
    return this.store
  }

  createStore($el) {
    this.store = reactive({
      state: {
        staticUrl: $el.data('static-url'),
        isInitialized: false,
        thankyou: null
      },
      init() {
        const queryParams = objectizeQueryString(location.search)
        return ApiManager.getBillingThankyou(queryParams.oid)
          .then(res => {
            this.state.thankyou = res.data
            this.state.isInitialized = true
          })
      },
    });

    return this.store
  }
}

export default new Store()
