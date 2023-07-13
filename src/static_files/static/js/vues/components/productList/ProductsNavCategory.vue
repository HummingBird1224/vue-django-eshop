<template>
  <div class="p-productsNavCategory">
    <h3 class="g-title-tertiary">カテゴリから探す</h3>
    <ul class="p-productsNavCategory-list" v-if="productCategory">
      <li
        v-for="(parentCategory, index) in productCategory.results" :key="parentCategory.slug"
        class="p-productsNavCategory-item" :class="{ 'is-current': parentCategorySlug == parentCategory.slug }"
      >
        <input :id="'category-menu-check-'+String(index+1)" class="category-menu-check" type="checkbox" />
        <label :for="'category-menu-check-'+String(index+1)">
          <div>
            <img :src="parentCategory.icon"/>
            <span>{{ parentCategory.name }}</span>
          </div>
          <div class="menuArrow"></div>
        </label>
        <ul class="p-productsNavCategory-items">
          <li class="p-productsNavCategory-itemTags" :class="{ 'is-current-tag': categorySlug == parentCategory.slug }">
            <a :href="`/catalog/${parentCategory.slug}/`">すべて</a>
          </li>
          <li
            v-for="category in parentCategory.children" :key="category.slug"
            class="p-productsNavCategory-itemTags" :class="{ 'is-current-tag': categorySlug == category.slug }"
          >
            <a :href="`/catalog/${category.slug}/`">{{ category.name }}</a>
          </li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin"

export default {
  name: "ProductsNavCategory",
  mixins: [StoreMixin],
  components: {},
  data: () => ({
  }),
  computed: {
    productCategory() {
      return this.state.productCategory
    },
    categorySlug() {
      return this.state.categorySlug
    },
    parentCategorySlug() {
      return this.state.parentCategorySlug
    },
  }
}
</script>

<style scoped>
</style>
