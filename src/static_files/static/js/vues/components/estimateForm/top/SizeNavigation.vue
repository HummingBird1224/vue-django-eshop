<template>
  <li class="p-MenuListItem p-MenuListItem--disable">
    <a class="p-MenuListItem-link" href="#">
      <div class="p-MenuListItem-left">
        <div class="p-MenuListItemIconWrapper">
          <svg class="p-MenuListItemIcon p-MenuListItemIcon--fullscreenExit">
            <use xlink:href='#icons-fullscreen_exit'/>
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
  name: "SizeNavigation",
  mixins: [StoreMixin],
  computed: {
    product() {
      return this.state.product;
    },
    form() {
      return this.state.form;
    },
    size() {
      return this.store.selectSizeInfo();
    },
    productCategory() {
      return this.state.productCategory;
    },
    label() {
      switch (this.productCategory) {
        case EstimateProductCategory.CARD_BOARD:
        case EstimateProductCategory.FLAT_BAG:
        case EstimateProductCategory.PAPER_BOX:
          return 'サイズの選択';
        default:
          return '';
      }
    },
    body() {
      const selected = this.size.options[this.form.size];

      if (selected) {
        return `${selected.name} ${selected.value.map(x => x.value).join(' x ')} mm`;
      } else if (this.form.freeSize) {
        return `${Object.entries(this.form.freeSize).map(x => x[1]).join(' x ')} mm`;
      }

      return '';
    }
  }
}
</script>

<style scoped>

</style>
