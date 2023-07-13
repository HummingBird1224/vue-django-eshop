<template>
  <div class="p-externalBaseProducts" id="external-products">
    <Header />
    <div class="p-externalBaseProducts-content">
      <Navigation />
      <ProductList />
    </div>
  </div>
</template>

<script>
import Header from "../components/externalBaseForm/Header";
import Navigation from "../components/externalBaseForm/Navigation";
import ProductList from "../components/externalBaseForm/ProductList";
import StoreMixin from "../mixins/StoreMixin";

export default {
  name: "ExternalBaseForm",
  mixins: [StoreMixin],
  components: {ProductList, Navigation, Header},
  mounted() {
    this.store.fetchProducts();
  }
}
</script>

<style>

</style>
