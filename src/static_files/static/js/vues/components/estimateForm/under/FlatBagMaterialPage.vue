<template>
  <ContentBase>
    <template v-slot:left>
      <div class="p-LeftRow">
        <h3 class="g-title-tertiary p-LeftRow-title">選択しましょう</h3>

        <div class="c-form-item p-MaterialSelections">
          <div class="c-form-radioGroup">
            <label
              v-for="(option, key) in options"
              :key="key"
              class="c-form-radio"
            >
              <input
                type="radio"
                class="c-form-radioInput"
                name="radio01"
                :value="key"
                v-model="editingForm.material"
              >
              <span class="c-form-radioMark"></span>
              <span class="p-MaterialSelectionLabel">
                <span
                  class="p-MaterialSelectionLabel-thumb"
                  :style="{
                    'background-image': `url(${option.image})`
                  }"
                ></span>
                <span class="p-MaterialSelectionLabel-content">
                  <span class="p-MaterialSelectionLabel-title">{{ option.name }}</span>
                  <span class="p-MaterialSelectionLabel-body">
                    {{ option.extra }}
                  </span>
                </span>
              </span>
            </label>
          </div>
        </div>
      </div>
    </template>

    <template v-slot:right>
      <div class="p-RightRow">
        <h3 class="g-title-tertiary p-RightRow-title">選択中</h3>
        <div class="p-MaterialInfo">
          <h4 class="g-title-quaternary p-MaterialInfo-title">{{ selectingMaterial.name }}</h4>
          <img class="p-MaterialInfo-thumb" :src="selectingMaterial.image">
        </div>
      </div>
    </template>
  </ContentBase>
</template>

<script>
import ContentBase from "./ContentBase.vue";
import StoreMixin from "../../../mixins/StoreMixin";

export default {
  name: "FlatBagMaterialPage",
  mixins: [StoreMixin],
  components: {ContentBase},
  computed: {
    editingForm() {
      return this.state.editingForm;
    },
    material() {
      return this.store.selectMaterialInfo();
    },
    options() {
      return this.material.options;
    },
    selectingMaterial() {
      return this.options[this.editingForm.material];
    }
  },
  methods: {
    updateCurrentSelectingValStr() {
      this.store.updateCurrentSelectingValStr(this.selectingMaterial.name);
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
