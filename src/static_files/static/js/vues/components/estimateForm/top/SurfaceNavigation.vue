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
          <svg class="p-MenuListItemIcon p-MenuListItemIcon--grain">
            <use xlink:href='#icons-grain'/>
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
  name: "SurfaceNavigation",
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
    surfaceMaterial() {
      return this.store.selectSurfaceMaterialInfo();
    },
    surfaceProcess() {
      return this.store.selectSurfaceProcessInto();
    },
    shouldShow() {
      switch (this.productCategory) {
        case EstimateProductCategory.CARD_BOARD:
        case EstimateProductCategory.PAPER_BOX:
          return !!this.surfaceMaterial || !!this.surfaceProcess;
        default:
          return false;
      }
    },
    label() {
      const labels = [];

      if (this.surfaceMaterial) {
        labels.push(this.surfaceMaterial.name);
      }

      if (this.surfaceProcess) {
        labels.push(this.surfaceProcess.name);
      }

      return labels.join(' / ') + 'の選択';
    },
    body() {
      return this.store.getSurfaceValueStr(this.form);
    }
  },
  methods: {
    onClick() {
      switch (this.productCategory) {
        case EstimateProductCategory.CARD_BOARD:
        case EstimateProductCategory.PAPER_BOX:
          this.state.flow = EstimateFlow.SURFACE;
          break;
      }
    }
  }
}
</script>

<style scoped>

</style>
