<template>
  <div class="p-productsCategoryHeader--new" v-if="productList">
    <h1>
      <img class="p-productsCategoryHeader--new-headerImage" :src="staticUrl+productList.header.image" />
      {{categoryName}}
    </h1>
    <ul class="p-ProductsDescriptionList">
      <li class="p-ProductsDescription" v-for="(note, index) in productList.header.notes" :key="index">
        <img :src="staticUrl+note.svg" />
        <h3>{{note.title}}</h3>
        <div>{{note.content}}</div>
      </li>
    </ul>
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
  name: "ProductsCategoryHeader",
  mixins: [StoreMixin],
  components: {},
  data: () => ({
  }),
  computed: {
    productList() {
      return this.state.productList
    },
    staticUrl() {
      return this.state.staticUrl;
    },
    categoryName() {
      return this.state.categoryName
    },
  }
}
</script>

<style scoped>
</style>
