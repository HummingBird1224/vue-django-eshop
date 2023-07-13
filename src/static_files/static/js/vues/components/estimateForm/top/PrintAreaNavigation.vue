<template>
  <li
    v-if="shouldShow"
    class="p-MenuListItem"
  >
    <a
      class="p-MenuListItem-link"
      href="#"
      @click.prevent.stop="onClick"
    >
      <div class="p-MenuListItem-left">
        <div class="p-MenuListItemIconWrapper">
          <svg class="p-MenuListItemIcon p-MenuListItemIcon--formatPaint">
            <use xlink:href='#icons-format_paint'/>
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
  name: "PrintAreaNavigation",
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
    shouldShow() {
      return this.productCategory === EstimateProductCategory.CARD_BOARD ||
        this.productCategory === EstimateProductCategory.PAPER_BOX;
    },
    label() {
      return  '印刷面数の選択';
    },
    body() {
      switch (this.productCategory) {
        case EstimateProductCategory.CARD_BOARD:
          return `外面 ${this.form.print_area.outside.length}`;
        case EstimateProductCategory.PAPER_BOX:
          return `外面 ${this.form.print_area.outside.length}　内面 ${this.form.print_area.inside.length}`;
        default:
          return '';
      }
    }
  },
  methods: {
    onClick() {
      switch (this.productCategory) {
        case EstimateProductCategory.CARD_BOARD:
        case EstimateProductCategory.PAPER_BOX:
          this.state.flow = EstimateFlow.PRINT_AREA;
          break;
      }
    }
  }
}
</script>

<style scoped>

</style>
