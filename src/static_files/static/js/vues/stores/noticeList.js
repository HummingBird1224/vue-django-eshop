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
        noticeList: null,
        currentPageNumber: null,
        nextPage: null,
        previousPage: null,
        staticUrl: $el.data('static-url'),
      },
      markNoticeRead(notice_id) {
        return ApiManager.readNotice(notice_id)
      },
      loadPreviousNotices() {
        return ApiManager.getNoticeList(this.state.previousPage)
          .then(res => {
            this.state.nextPage = res.data.next
            this.state.previousPage = res.data.previous
            this.state.currentPageNumber = res.data.current_page
            this.state.noticeList = res.data.results
          })
      },
      loadNextNotices() {
        return ApiManager.getNoticeList(this.state.nextPage)
          .then(res => {
            this.state.nextPage = res.data.next
            this.state.previousPage = res.data.previous
            this.state.currentPageNumber = res.data.current_page
            this.state.noticeList = res.data.results
          })
      },
      fetchNoticeList() {
        return ApiManager.getNoticeList()
          .then(res => {
            this.state.nextPage = res.data.next
            this.state.previousPage = res.data.previous
            this.state.currentPageNumber = res.data.current_page
            this.state.noticeList = res.data.results
          })
      },
    }

    return this.store
  }
}

export default new Store()
