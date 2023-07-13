<template>
  <li class="p-MenuListItem p-MenuListItem--disable">
    <a class="p-MenuListItem-link" href="#">
      <div class="p-MenuListItem-left">
        <div class="p-MenuListItemIconWrapper">
          <svg class="p-MenuListItemIcon p-MenuListItemIcon--localMall">
            <use xlink:href='#icons-local_mall'/>
          </svg>
        </div>

        <div class="p-MenuListItemContent">
          <h4 class="g-title-quaternary">{{ label }}</h4>
          <p>{{ body }}</p>
        </div>
      </div>
    </a>
  </li>
</template>

<script>
import StoreMixin from "../../../mixins/StoreMixin";
import EstimateProductCategory from "../../../../constants/EstimateProductCategory";

export default {
  name: "QuantityNavigation",
  mixins: [StoreMixin,],
  computed: {
    product() {
      return this.state.product;
    },
    form() {
      return this.state.form;
    },
    productCategory() {
      return this.state.productCategory;
    },
    label() {
      switch (this.productCategory) {
        case EstimateProductCategory.CARD_BOARD:
        case EstimateProductCategory.FLAT_BAG:
        case EstimateProductCategory.PAPER_BOX:
          return '注文数の選択';
        default:
          return '';
      }
    },
    body() {
      return $filters.toPriceFormat(this.form.quantity);
    }
  }
}
</script>

<style scoped>

</style>
