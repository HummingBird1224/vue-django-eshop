<template>
  <div v-if="priceInfo" class="p-ProductPrice">
    <ul class="p-ProductPrice-detailList">
      <li
        v-if="priceInfo.product_total"
        class="p-ProductPrice-detailItem"
      >
        <span class="p-ProductPrice-detailTitle">商品</span>
        <span class="p-ProductPrice-detailBody">{{ $filters.toPriceFormat(priceInfo.product_total) }}<span
          class="p-ProductPrice-detailUnit">円</span></span>
      </li>
      <li
        v-if="priceInfo.plate_price"
        class="p-ProductPrice-detailItem"
      >
        <span class="p-ProductPrice-detailTitle">版代</span>
        <span class="p-ProductPrice-detailBody">{{ $filters.toPriceFormat(priceInfo.plate_price) }}<span
          class="p-ProductPrice-detailUnit">円</span></span>
      </li>
      <li
        v-if="priceInfo.mold_price"
        class="p-ProductPrice-detailItem"
      >
        <span class="p-ProductPrice-detailTitle">木型代</span>
        <span class="p-ProductPrice-detailBody">{{ $filters.toPriceFormat(priceInfo.mold_price) }}<span
          class="p-ProductPrice-detailUnit">円</span></span>
      </li>
      <li
        v-if="priceInfo.tax"
        class="p-ProductPrice-detailItem"
      >
        <span class="p-ProductPrice-detailTitle">消費税</span>
        <span class="p-ProductPrice-detailBody">{{ $filters.toPriceFormat(priceInfo.tax) }}<span
          class="p-ProductPrice-detailUnit">円</span></span>
      </li>
    </ul>
    <div class="p-ProductPrice-main">
      <span class="p-ProductPrice-totalTitle">合計</span>
      <div class="p-ProductPrice-totalContent">
        <span class="p-ProductPrice-totalBody">{{ $filters.toPriceFormat(priceInfo.total) }}</span>
        <span class="p-ProductPrice-totalUnit">円（税込）</span>
        <span class="p-ProductPrice-unitBody">{{ $filters.toPriceFormat(priceInfo.unit_price) }}</span>
        <span class="p-ProductPrice-unitUnit">円</span>
        <span class="p-ProductPrice-unitPer">/{{ product.unit }}</span>
      </div>
    </div>
  </div>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin";
export default {
  name: "PriceInfo",
  mixins: [StoreMixin],
  computed: {
    product() {
      return this.state.product;
    },
    selectedQuantity() {
      return this.state.form.quantity;
    },
    price() {
      return this.state.price;
    },
    priceInfo() {
      if (!this.state.price || !this.selectedQuantity) {
        return null;
      }

      return this.state.price[this.selectedQuantity];
    }
  }
}
</script>

<style scoped>

</style>
