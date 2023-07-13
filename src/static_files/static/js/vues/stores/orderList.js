import ApiManager from "../../helpers/ApiManager"
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
        isProcessing: false,
        orders: null
      },
      init() {
        return ApiManager.getOrders()
          .then(res => {
            this.state.orders = res.data
            this.state.isInitialized = true
          })
      },
      loadNextOrders() {
        return ApiManager.getOrders(this.state.orders.next)
          .then(res => {
            this.state.orders.next = res.data.next
            this.state.orders.results = this.state.orders.results.concat(res.data.results)
          })
      },
      postCancelOrder(ref_code) {
        if (this.state.isProcessing) return
        this.state.isProcessing = true
        return ApiManager.postCancelOrder(ref_code, {})
          .then(() => {
            location.reload();
          })
      }
    });

    return this.store
  }
}

export default new Store()
