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
        categoryName: $el.data('category-name'),
        parentCategorySlug: $el.data('parent-category-slug'),
        categorySlug: $el.data('category-slug'),
        productList: null,
        productCategory: null,
        staticUrl: $el.data('static-url'),
      },
      fetchProductCategory() {
        return ApiManager.getProductCategory()
          .then(res => {
            this.state.productCategory = res.data
          })
      },
      fetchProductList(slug) {
        return ApiManager.getProductList(slug)
          .then(res => {
            this.state.productList = res.data
          })
      },
    }

    return this.store
  }
}

export default new Store()
