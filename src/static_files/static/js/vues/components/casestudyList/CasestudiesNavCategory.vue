<template>
  <div class="p-productsNavCategory">
    <!-- <h3 class="g-title-tertiary">商品カテゴリから探す</h3> -->
    <!-- <ul class="p-productsNavCategory-list" v-if="productCategory">
      <li
        v-for="(parentCategory, index) in productCategory.results" :key="parentCategory.slug"
        class="p-productsNavCategory-item" :class="{ 'is-current': parentCategorySlug == parentCategory.slug }"
      >
        <input :id="'category-menu-check-product-'+String(index+1)" class="category-menu-check" type="checkbox" />
        <label :for="'category-menu-check-product-'+String(index+1)">
          <div style="display:flex">
            <img :src="parentCategory.icon"/>
            <span><a :href="`/casestudies/product_category/`+parentCategory.slug">{{ parentCategory.name }}</a></span>
            
          </div>
        </label>
      </li>
    </ul> -->
    <ul  v-if="caseStudyCategory" >
      <li  v-for="(individualCategory, index) in caseStudyCategory.results" :key="individualCategory.slug">
        <div class="p-productsNavCategory">
          <h3 class="g-title-tertiary">{{individualCategory.name}}から探す</h3>
        </div>
        <ul class="p-productsNavCategory-list" v-if="individualCategory.children">
          <li
            v-for="(parentCategory, index) in individualCategory.children" :key="parentCategory.slug"
            class="p-productsNavCategory-item" :class="{ 'is-current': parentCategorySlug == parentCategory.slug }"
          >
            <input :id="'category-menu-check-'+parentCategory.name+'-'+String(index+1)" class="category-menu-check" type="checkbox" />
            <label :for="'category-menu-check-'+parentCategory.name+'-'+String(index+1)">
              <div style="display: flex;">
                <img :src="parentCategory.icon" class="category-menu-icon"/>
                <span><a :href="`/casestudies/`+individualCategory.slug+'/'+parentCategory.slug">{{ parentCategory.name }}</a></span>
              </div>
            </label>
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin"

export default {
  name: "CasestudyNavCategory",
  mixins: [StoreMixin],
  components: {},
  data: () => ({
  }),
  computed: {
    caseStudyCategory() {
      return this.state.caseStudyCategory
    },
    // materialCategory() {
    //   return this.state.materialCategory
    // },
    // categorySlug() {
    //   return this.state.categorySlug
    // },
    // parentCategorySlug() {
    //   return this.state.parentCategorySlug
    // },
  },
}
</script>

<style scoped>
</style>
