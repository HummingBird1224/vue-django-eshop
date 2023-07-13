<template>
  <div class="p-productsCategoryHeader--new p-caseStudyHeader" v-if="casestudiesList">
    <div v-if="isListView">
      <h1>
        <img class="p-productsCategoryHeader--new-headerImage " :src="staticUrl+'img/product_category/flatbag/category_flatbag_all.png'" />
        製品事例一覧
      </h1>
    </div>
    <div v-else>
      <div v-if="caseStudyCategoryObject">
        <h1 class="bottom-border">
          <img class="p-productsCategoryHeader--new-headerImage " :src="caseStudyCategoryObject.icon" />
          {{ caseStudyCategoryObject.name }}
        </h1>
        <div v-if="caseStudyCategoryObject.explanatory_image">
          <img :src="caseStudyCategoryObject.explanatory_image" alt="explanatory_image" class="full-image"/>
        </div>
        <div v-else >
          <div class="p-caseStudyCategoryHearder--new-tagContent m-b-30" >
            <h2 class="m-b-15">{{ caseStudyCategoryObject.name }}とは?</h2>
            <p >{{ caseStudyCategoryObject.text }}
            </p>
          </div>
          <div class="p-caseStudyCategoryHearder--new-properties" >
            <ul class="advantage m-b-15">
              <h2 class="m-b-15">メリット</h2>
              <li v-for="item in caseStudyCategoryObject.advantage.split('\n')">{{ item }}</li>
            </ul>
            <ul class="disadvantage m-b-15" >
              <h2 class="m-b-15">デメリット</h2>
              <li v-for="item in caseStudyCategoryObject.disadvantage.split('\n')">{{ item }}</li>
            </ul>
          </div>
        </div>
      </div>
      <div v-else>
        <h1 v-if="productCategoryObject">
          <img class="p-productsCategoryHeader--new-headerImage " :src="productCategoryObject.icon" />
          {{ productCategoryObject.name }}
        </h1>
      </div>
    </div>
  </div>
  <div class="p-productsCategoryHeader--new"  v-else>
    <h1>
      ---
    </h1>
    <ul class="p-ProductsDescriptionList">
      <li class="p-ProductsDescription">
        <h3>---</h3>
        <div>---</div>
      </li>
      <li class="p-ProductsDescription">
        <h3>---</h3>
        <div>---</div>
      </li>
      <li class="p-ProductsDescription">
        <h3>---</h3>
        <div>---</div>
      </li>
    </ul>
  </div>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin"

export default {
  name: "CaseStudyCategoryHeader",
  mixins: [StoreMixin],
  components: {},
  props : {
    category:{
      type:String
    }
  },
  data: () => ({
  }),
  computed: {
    isListView(){
      return this.category=="all"
    },
    casestudiesList() {
      return this.state.caseStudyList
    },
    staticUrl() {
      return this.state.staticUrl;
    },
    categoryName() {
      return this.state.categoryName
    },
    caseStudyCategoryObject(){
      return this.state.caseStudyCategoryObject;
    },
    productCategoryObject(){
      return this.state.productCategoryObject;
    }
  }
}
</script>

<style scoped>
</style>
