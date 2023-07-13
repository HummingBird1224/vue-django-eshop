<template>
  <div class="p-externalColorMeProducts" id="external-products">
    <Header />
    <div class="p-externalColorMeProducts-content">
      <Navigation />
      <ProductList />
    </div>
  </div>
</template>

<script>
import Header from "../components/externalColorMeForm/Header";
import Navigation from "../components/externalColorMeForm/Navigation";
import ProductList from "../components/externalColorMeForm/ProductList";
import StoreMixin from "../mixins/StoreMixin";

export default {
  name: "ExternalColorMeForm",
  mixins: [StoreMixin],
  components: {ProductList, Navigation, Header},
  mounted() {
    this.store.fetchProducts();
  }
}
</script>

<style>

</style>
