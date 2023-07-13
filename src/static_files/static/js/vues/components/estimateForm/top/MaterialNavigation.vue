<template>
  <li
    v-if="material && material.options"
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
  name: "MaterialNavigation",
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
    material() {
      return this.store.selectMaterialInfo();
    },
    label() {
      return this.material ? this.material.name + 'の選択' : '';
    },
    body() {
      const selected = this.material.options[this.form.material];
      return selected ? selected.name : '';
    }
  },
  methods: {
    onClick() {
      switch (this.productCategory) {
        case EstimateProductCategory.FLAT_BAG:
          this.state.flow = EstimateFlow.FLAT_BAG_MATERIAL;
          break;
      }
    }
  }
}
</script>

<style scoped>

</style>
