<template>
  <ContentBase>
    <template v-slot:left>
      <div class="p-LeftRow">
        <h3 class="g-title-tertiary p-LeftRow-title">選択しましょう</h3>
        <div
          v-if="outside"
          class="p-PrintAreaSelections"
        >
          <h4 class="g-title-quaternary p-PrintAreaSelections-title">外面</h4>
          <ul>
            <li
              v-for="(option, key) in outsideOptions"
              :key="key"
              class="p-PrintAreaSelectionItem"
            >
              <div class="c-form-item">
                <label class="c-form-checkbox">
                  <input
                    class="c-form-checkboxInput"
                    type="checkbox"
                    :value="option.value"
                    v-model="editingForm.print_area.outside"
                  >
                  <span class="c-form-checkboxMark"><i class="material-icons">done</i></span>
                  {{ option.name }}
                </label>
              </div>
            </li>
          </ul>
        </div>

        <div
          v-if="inside"
          class="p-PrintAreaSelections"
        >
          <h4 class="g-title-quaternary p-PrintAreaSelections-title">内面</h4>
          <ul>
            <li
              v-for="(option, key) in insideOptions"
              :key="key"
              class="p-PrintAreaSelectionItem"
            >
              <div class="c-form-item">
                <label class="c-form-checkbox">
                  <input
                    class="c-form-checkboxInput"
                    type="checkbox"
                    :value="option.value"
                    v-model="editingForm.print_area.inside"
                  >
                  <span class="c-form-checkboxMark"><i class="material-icons">done</i></span>
                  {{ option.name }}
                </label>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </template>

    <template v-slot:right>
      <div class="p-RightRow">
        <h3 class="g-title-tertiary p-RightRow-title">選択中</h3>
        <div class="p-PrintAreaInfoList">
          <div
            v-if="outside"
            class="p-PrintAreaInfo"
          >
            <div class="p-PrintAreaInfo-content">
              <h3 class="g-title-tertiary p-PrintAreaInfo-title">外面</h3>
              <ul class="p-PrintAreaInfo-list">
                <li
                  v-for="surface in sortedSelectedOutside"
                  :key="surface"
                >{{ surface }}
                </li>
              </ul>
            </div>
            <img class="p-PrintAreaInfo-thumb" :src="outside.image" alt="">
          </div>

          <div
            v-if="inside"
            class="p-PrintAreaInfo"
          >
            <div class="p-PrintAreaInfo-content">
              <h3 class="g-title-tertiary p-PrintAreaInfo-title">内面</h3>
              <ul class="p-PrintAreaInfo-list">
                <li
                  v-for="surface in sortedSelectedInside"
                  :key="surface"
                >{{ surface }}
                </li>
              </ul>
            </div>
            <img class="p-PrintAreaInfo-thumb" :src="inside.image" alt="">
          </div>
        </div>
      </div>
    </template>
  </ContentBase>
</template>

<script>
import ContentBase from "./ContentBase.vue";
import StoreMixin from "../../../mixins/StoreMixin";
import EstimateProductCategory from "../../../../constants/EstimateProductCategory";

export default {
  name: "PrintAreaPage",
  mixins: [StoreMixin],
  components: {ContentBase},
  computed: {
    editingForm() {
      return this.state.editingForm;
    },
    productCategory() {
      return this.state.productCategory;
    },
    printArea() {
      return this.store.selectPrintAreaInfo();
    },
    outside() {
      return this.printArea.options.outside;
    },
    inside() {
      return this.printArea.options.inside;
    },
    outsideOptions() {
      return this.outside.options;
    },
    insideOptions() {
      return this.inside.options;
    },
    sortedSelectedOutside() {
      return this.editingForm.print_area.outside.sort();
    },
    sortedSelectedInside() {
      return this.editingForm.print_area.inside.sort();
    },
  },
  methods: {
    updateCurrentSelectingValStr() {
      let valStr = '';

      switch (this.productCategory) {
        case EstimateProductCategory.CARD_BOARD:
          valStr = `外面 ${this.editingForm.print_area.outside.length}`;
          break;
        case EstimateProductCategory.PAPER_BOX:
          valStr = `外面 ${this.editingForm.print_area.outside.length} / 内面 ${this.editingForm.print_area.inside.length}`;
          break;
      }

      this.store.updateCurrentSelectingValStr(valStr);
    }
  },
  watch: {
    editingForm: {
      handler: function () {
        this.updateCurrentSelectingValStr();
      },
      deep: true
    }
  },
  mounted() {
    this.updateCurrentSelectingValStr();
  }
}
</script>

<style scoped>

</style>
