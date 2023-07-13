<template>
  <ol class="p-billingFlow">
    <li
      class="p-billingFlow-item"
      :class="{
        'is-active': flow === BillingFlow.LOGIN,
        'is-done': flow !== BillingFlow.LOGIN,
      }"
    >
      1. 登録/ログイン
    </li>
    <li
      class="p-billingFlow-item"
      :class="{
        'is-active': flow === BillingFlow.ADDRESS,
        'is-done': flow === BillingFlow.PAYMENT,
      }"
    >
      2. 配送先情報
    </li>
    <li
      class="p-billingFlow-item"
      :class="{
        'is-active': flow === BillingFlow.PAYMENT,
      }"
    >
      3. お支払い＆注文確定
    </li>
  </ol>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin";
import BillingFlow from "../../../constants/BillingFlow";

export default {
  name: "Flow",
  mixins: [StoreMixin],
  data: () => ({
    BillingFlow,
  }),
  computed: {
    flow() {
      return this.state.flow;
    }
  }
}
</script>

<style scoped>

</style>
