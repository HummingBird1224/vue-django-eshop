<template>
  <div>
    <div class="p-reorderHeader">
      <h3>同じデザインで再注文</h3>
      <p>再注文の際は版代・木型代が差し引かれます。</p>
      <p>デザインの変更はできません。</p>
    </div>
    <ReorderForm
      v-if="isInitialized"
    />
  </div>
</template>

<script>
import ReorderForm from "../components/ReorderForm/ReorderForm";
import isObject from "../../helpers/isObject";
import StoreMixin from "../mixins/StoreMixin";

export default {
  name: "Reorder",
  mixins: [StoreMixin],
  components: {ReorderForm},
  computed: {
    isInitialized() {
      return this.state.isInitialized;
    },
  },
  mounted() {
    this.store.init();
  }
}
</script>

<style>

</style>
