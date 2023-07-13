<template>
  <li
    v-if="process && process.options"
    class="p-MenuListItem"
  >
    <a
      class="p-MenuListItem-link"
      href="#"
      @click.prevent.stop="onClick"
    >
      <div class="p-MenuListItem-left">
        <div class="p-MenuListItemIconWrapper">
          <svg class="p-MenuListItemIcon p-MenuListItemIcon--buildingBlocks">
            <use xlink:href='#icons-building_blocks'/>
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
  name: "ProcessNavigation",
  mixins: [StoreMixin],
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
    process() {
      return this.store.selectProcessInfo();
    },
    label() {
      return this.process ? this.process.name + 'の選択' : '';
    },
    body() {
      return this.store.getProcessValueStr(this.form);
    }
  },
  methods: {
    onClick() {
      switch (this.productCategory) {
        case EstimateProductCategory.CARD_BOARD:
        case EstimateProductCategory.FLAT_BAG:
          this.state.flow = EstimateFlow.PROCESS;
          break;
      }
    }
  }
}
</script>

<style scoped>

</style>
