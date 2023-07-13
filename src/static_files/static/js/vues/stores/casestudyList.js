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
        // categoryName: $el.data('category-name'),
        category: $el.data('parent-category-slug')?
                  $el.data('parent-category-slug'):'all',
        // tagName: $el.data('tag-name'),
        tag: $el.data('category-slug')?$el.data('category-slug'):'all',
        detailCategory: $el.data('detail-category'),
        detailTag: $el.data('detail-tag'),
        detailSlug: $el.data('detail-slug'),
        caseStudyList: null,
        caseStudyCategory: null,
        staticUrl: $el.data('static-url'),
        caseStudy: null,
        caseStudySameTagList:null,
        caseStudyCategoryObject:null,
        // productCategoryObject:null,
      },
      fetchCaseStudyCategory() {
        return ApiManager.getCaseStudyCategory()
          .then(res => {
            this.state.caseStudyCategory = res.data
          })
      },
      fetchCaseStudyList(category, tag) {
        return ApiManager.getCaseStudyList(category, tag)
          .then(res => {
            this.state.caseStudyList = res.data.casestudy_list;
            this.state.caseStudyCategoryObject = res.data.category_object;
          })
      },
      fetchCaseStudy() {
        return ApiManager.getCaseStudy(this.state.detailSlug)
          .then(res=>{
            // console.log(res.data)
            this.state.caseStudy=res.data
          })
      },
      fetchCaseStudySameTagList(category, tag, slug){
        return ApiManager.getCaseStudySameTagList(category, tag, slug)
              .then(res => {
                this.state.caseStudySameTagList=res.data
              })
      },
    }

    return this.store
  }
}

export default new Store()
