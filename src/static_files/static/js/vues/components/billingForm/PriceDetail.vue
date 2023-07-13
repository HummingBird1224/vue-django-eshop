<template>
  <div class="p-CartPriceDetail">
    <div class="p-CartPriceDetail-col">
      <small>内訳</small>
    </div>
    <div class="p-CartPriceDetail-col">
      <h4 class="g-title-quaternary p-CartPriceDetail-title">商品合計</h4>
      <p class="p-CartPriceDetail-body">{{ $filters.toPriceFormat(orderInfo.product_total) }}<span class="p-CartPrice-unit">円</span></p>
    </div>

    <div class="p-CartPriceDetail-col">
      <h4 class="g-title-quaternary p-CartPriceDetail-title">版代</h4>
      <p class="p-CartPriceDetail-body">{{ $filters.toPriceFormat(orderInfo.plate_total) }}<span class="p-CartPrice-unit">円</span></p>
    </div>

    <div class="p-CartPriceDetail-col">
      <h4 class="g-title-quaternary p-CartPriceDetail-title">木型代</h4>
      <p class="p-CartPriceDetail-body">{{ $filters.toPriceFormat(orderInfo.mold_total) }}<span class="p-CartPrice-unit">円</span></p>
    </div>

    <div class="p-CartPriceDetail-col">
      <h4 class="g-title-quaternary p-CartPriceDetail-title">配送料</h4>
      <p class="p-CartPriceDetail-body">{{ $filters.toPriceFormat(orderInfo.shipping_total) }}<span class="p-CartPrice-unit">円</span></p>
    </div>

    <div class="p-CartPriceDetail-col">
      <h4 class="g-title-quaternary p-CartPriceDetail-title">消費税</h4>
      <p class="p-CartPriceDetail-body">{{ $filters.toPriceFormat(orderInfo.tax_total) }}<span class="p-CartPrice-unit">円</span></p>
    </div>
  </div>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin";

export default {
  name: "PriceDetail",
  mixins: [StoreMixin],
  computed: {
    orderInfo() {
      return this.state.orderInfo;
    }
  }
}
</script>

<style scoped>

</style>
