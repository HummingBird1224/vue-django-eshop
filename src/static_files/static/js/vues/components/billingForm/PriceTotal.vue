<template>
  <div class="p-CartPriceTotal">
    <h4 class="g-title-quaternary p-CartPriceTotal-title">合計</h4>
    <p class="p-CartPriceTotal-body">{{ $filters.toPriceFormat(orderInfo.total) }}<span class="p-CartPrice-unit">円</span></p>
  </div>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin";

export default {
  name: "PriceTotal",
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
