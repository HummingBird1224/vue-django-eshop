<template>
  <div>
    <Product
      v-for="product in products"
      :key="product.slug"
      :product="product"
    />
  </div>
</template>

<script>
import Product from "./Product";
import StoreMixin from "../../mixins/StoreMixin";

export default {
  name: "ProductList",
  mixins: [StoreMixin],
  components: {Product},
  computed: {
    products() {
      return this.state.products;
    }
  }
}
</script>

<style>

</style>
