<template>
  <div class="p-externalFutureShopProducts" id="external-products">
    <Header />
    <div class="p-externalFutureShopProducts-content">
      <Navigation />
      <ProductList />
    </div>
  </div>
</template>

<script>
import Header from "../components/externalFutureShopForm/Header";
import Navigation from "../components/externalFutureShopForm/Navigation";
import ProductList from "../components/externalFutureShopForm/ProductList";
import StoreMixin from "../mixins/StoreMixin";

export default {
  name: "ExternalFutureShopForm",
  mixins: [StoreMixin],
  components: {ProductList, Navigation, Header},
  mounted() {
    this.store.fetchProducts();
  }
}
</script>

<style>

</style>
