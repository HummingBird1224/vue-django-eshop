import ApiManager from "../../../helpers/ApiManager";

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
        noticePostList: null,
        staticUrl: $el.data('static-url') || '/static',
        currentPageNumber: null,
        nextPage: null,
        previousPage: null,
      },
      fetchNoticePost(kw) {
        const keyword = kw || '';
        return ApiManager.getInternalNoticePostList(null,keyword)
          .then(res => {
            this.state.nextPage = res.data.next
            this.state.previousPage = res.data.previous
            this.state.currentPageNumber = res.data.current_page
            this.state.noticePostList = res.data.results;
          })
      },
      loadPreviousNoticePosts() {
        return ApiManager.getInternalNoticePostList(this.state.previousPage)
          .then(res => {
            this.state.nextPage = res.data.next
            this.state.previousPage = res.data.previous
            this.state.currentPageNumber = res.data.current_page
            this.state.noticePostList = res.data.results
          })
      },
      loadNextNoticePosts() {
        return ApiManager.getInternalNoticePostList(this.state.nextPage)
          .then(res => {
            this.state.nextPage = res.data.next
            this.state.previousPage = res.data.previous
            this.state.currentPageNumber = res.data.current_page
            this.state.noticePostList = res.data.results
          })
      },
    };

    return this.store;
  }
}

export default new Store();
