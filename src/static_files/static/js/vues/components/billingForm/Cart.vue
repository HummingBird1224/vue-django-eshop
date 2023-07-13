<template>
  <div class="p-billingForm-cart">
    <h3 class="g-title-tertiary p-CartHeader">注文内容</h3>
    <CartList />
    <div class="p-CartPrice">
      <PriceDetail/>
      <PriceTotal/>
    </div>
  </div>
</template>

<script>
import PriceTotal from "./PriceTotal";
import PriceDetail from "./PriceDetail";
import CartList from "./CartList";

export default {
    name: "Cart",
    components: {CartList, PriceDetail, PriceTotal}
}
</script>

<style scoped>

</style>
