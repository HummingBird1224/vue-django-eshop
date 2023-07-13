<template>
  <li
    v-if="specialPrint && specialPrint.options"
    class="p-MenuListItem"
  >
    <a
      class="p-MenuListItem-link"
      href="#"
      @click.prevent.stop="onClick"
    >
      <div class="p-MenuListItem-left">
        <div class="p-MenuListItemIconWrapper">
          <svg class="p-MenuListItemIcon p-MenuListItemIcon--flare">
            <use xlink:href='#icons-flare'/>
          </svg>
        </div>

        <div class="p-MenuListItemContent">
          <h4 class="g-title-quaternary">{{ label }}<span class="p-MenuListItemSupplement">任意</span></h4>
          <p>{{ body }}</p>
        </div>
      </div>

      <div class="p-MenuListItem-right">
        <svg>
          <use xlink:href='#icons-arrow_down'></use>
        </svg>
      </div>
    </a>
  </li>
</template>

<script>
import StoreMixin from "../../../mixins/StoreMixin";
import EstimateProductCategory from "../../../../constants/EstimateProductCategory";
import EstimateFlow from "../../../../constants/EstimateFlow";

export default {
  name: "SpecialPrintNavigation",
  mixins: [StoreMixin],
  computed: {
    form() {
      return this.state.form;
    },
    product() {
      return this.state.product;
    },
    productCategory() {
      return this.state.productCategory;
    },
    specialPrint() {
      return this.store.selectSpecialPrintInfo();
    },
    label() {
      return this.specialPrint ? this.specialPrint.name + 'の選択' : '';
    },
    body() {
      const selected = this.specialPrint.options[this.form.special_print];
      return selected ? selected.name : '';
    }
  },
  methods: {
    onClick() {
      switch (this.productCategory) {
        case EstimateProductCategory.PAPER_BOX:
          this.state.flow = EstimateFlow.SPECIAL_PRINT;
          break;
      }
    }
  }
}
</script>

<style scoped>

</style>
