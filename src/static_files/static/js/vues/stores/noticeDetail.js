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
        noticeTitle: $el.data('title'),
        noticeText: $el.data('text'),
      },
    }

    return this.store
  }
}

export default new Store()
