import ApiManager from "../../helpers/ApiManager"

class Store {
  constructor() {
    this.store = {}
  }

  getStore() {
    return this.store
  }

  createStore($el) {
    this.store = {
      state: {
        staticUrl: $el.data('static-url'),
      },
      fetch() {
      },
    }

    return this.store
  }
}

export default new Store()
