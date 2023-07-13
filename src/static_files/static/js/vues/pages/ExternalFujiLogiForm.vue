<template>
  <div class="p-externalFujiLogiProducts" id="external-products">
    <Header />
    <div class="p-externalFujiLogiProducts-content">
      <Navigation />
      <ProductList />
    </div>
  </div>
</template>

<script>
import Header from "../components/externalFujiLogiForm/Header";
import Navigation from "../components/externalFujiLogiForm/Navigation";
import ProductList from "../components/externalFujiLogiForm/ProductList";
import StoreMixin from "../mixins/StoreMixin";

export default {
  name: "ExternalFujiLogiForm",
  mixins: [StoreMixin],
  components: {ProductList, Navigation, Header},
  mounted() {
    this.store.fetchProducts();
  }
}
</script>

<style>

</style>
