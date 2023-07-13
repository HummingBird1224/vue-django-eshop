<template>
  <footer class="p-ProductFooter">
    <div
      v-if="price"
      class="p-ProductPrice"
    >
      <span class="p-ProductPrice-label">商品価格 （税抜）</span>
      <p class="p-ProductPrice-value">{{ $filters.toPriceFormat(price.product_total) }}<span class="p-ProductPrice-unit">円</span></p>
    </div>
  </footer>
</template>

<script>
import StoreMixin from "../../../mixins/StoreMixin";

export default {
  name: "EstimateInfoFooter",
  mixins: [StoreMixin],
  computed: {
    price() {
      return this.state.price;
    }
  }
}
</script>

<style scoped>

</style>
