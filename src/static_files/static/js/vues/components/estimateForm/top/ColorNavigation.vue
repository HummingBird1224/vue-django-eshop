<template>
  <li
    v-if="colorNum && colorNum.options"
    class="p-MenuListItem"
  >
    <a
      class="p-MenuListItem-link"
      href="#"
      @click.prevent.stop="onClick"
    >
      <div class="p-MenuListItem-left">
        <div class="p-MenuListItemIconWrapper">
          <svg class="p-MenuListItemIcon p-MenuListItemIcon--colorLens">
            <use xlink:href='#icons-color_lens'/>
          </svg>
        </div>

        <div class="p-MenuListItemContent">
          <h4 class="g-title-quaternary">{{ label }}</h4>
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
  name: "ColorNavigation",
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
    colorNum() {
      return this.store.selectColorInfo();
    },
    label() {
      return this.colorNum ? this.colorNum.name + 'の選択' : '';
    },
    body() {
      const selected = this.colorNum.options[this.form.color_num];
      return selected ? selected.name : '';
    }
  },
  methods: {
    onClick() {
      switch (this.productCategory) {
        case EstimateProductCategory.CARD_BOARD:
        case EstimateProductCategory.FLAT_BAG:
        case EstimateProductCategory.PAPER_BOX:
          this.state.flow = EstimateFlow.COLOR;
          break;
      }
    }
  }
}
</script>

<style scoped>

</style>
