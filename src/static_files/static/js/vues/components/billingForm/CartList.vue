<template>
  <ul class="p-CartList">
    <CartListItem
      v-for="item in items"
      :key="item.ref_code"
      :item="item"
    />
  </ul>
</template>

<script>
import CartListItem from "./CartListItem";
import StoreMixin from "../../mixins/StoreMixin";

export default {
  name: "CartList",
  mixins: [StoreMixin],
  components: {CartListItem},
  computed: {
    orderInfo() {
      return this.state.orderInfo;
    },
    items() {
      if (!this.orderInfo) {
        return [];
      }

      return this.orderInfo.items;
    }
  }
}
</script>

<style scoped>

</style>
