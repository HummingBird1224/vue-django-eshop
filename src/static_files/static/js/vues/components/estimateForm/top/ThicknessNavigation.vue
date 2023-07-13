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
          <svg class="p-MenuListItemIcon p-MenuListItemIcon--importExport">
            <use xlink:href='#icons-import_export'/>
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
  name: "ThicknessNavigation",
  mixins: [StoreMixin],
  computed: {
    product() {
      return this.state.product;
    },
    productCategory() {
      return this.state.productCategory;
    },
    shouldShow() {
      switch (this.productCategory) {
        case EstimateProductCategory.CARD_BOARD:
          return this.product.hasOwnProperty('thickness');
        default:
          return false;
      }
    },
    label() {
      switch (this.productCategory) {
        case EstimateProductCategory.CARD_BOARD:
          return this.product.thickness.name + 'の選択';
        default:
          return '';
      }
    },
    body() {
      return '通常 - 1.5mm';
    }
  },
  methods: {
    onClick() {
      switch (this.productCategory) {
        case EstimateProductCategory.CARD_BOARD:
          this.state.flow = EstimateFlow.CARD_BOARD_THICKNESS;
          break;
      }
    }
  }
}
</script>

<style scoped>

</style>
