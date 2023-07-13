<template>
  <footer class="p-Footer">
    <div class="p-Footer-left">
      <p class="p-FooterSelecting">選択中<span class="p-FooterSelecting-value">{{ currentSelectingValStr }}</span></p>
    </div>
    <div class="p-Footer-right">
      <a
        class="p-FooterCancel"
        href="#"
        @click.prevent.stop="initEditingForm"
      >
        変更しない
      </a>
      <a
        class="c-btn c-btn--primary"
        href="#"
        :class="{
          'is-disabled': !canSubmit,
        }"
        @click.prevent.stop="applyEditingForm"
      >
        変更する
      </a>
    </div>
  </footer>
</template>

<script>
import StoreMixin from "../../../mixins/StoreMixin";
import EstimateFlow from "../../../../constants/EstimateFlow";

export default {
  name: "Footer",
  mixins: [StoreMixin],
  computed: {
    flow() {
      return this.state.flow;
    },
    form() {
      return this.state.editingForm;
    },
    product() {
      return this.state.product;
    },
    currentSelectingValStr() {
      return this.state.currentSelectingValStr;
    },
    canSubmit() {
      if (this.flow === EstimateFlow.PRINT_AREA) {
        return Object.keys(this.product.extra_info.print_area.options)
          .map(x => this.form.print_area[x])
          .every(x => x.length > 0);
      }

      return true;
    }
  },
  methods: {
    applyEditingForm() {
      if (!this.canSubmit) {
        return;
      }

      this.store.applyEditingForm();
      this.state.flow = EstimateFlow.TOP;
    },
    initEditingForm() {
      this.store.initEditingForm();
      this.state.flow = EstimateFlow.TOP;
    }
  }
}
</script>

<style scoped>

</style>
