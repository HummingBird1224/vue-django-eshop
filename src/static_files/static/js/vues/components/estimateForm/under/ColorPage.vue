<template>
  <ContentBase>
    <template v-slot:left>
      <div class="p-LeftRow">
        <h3 class="g-title-tertiary p-LeftRow-title">サイズを選択しましょう</h3>
        <div class="c-form-item p-ColorSelections">
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
                v-model="editingForm.color_num"
              >
              <span class="c-form-radioMark"></span>
              {{ option.name }}
            </label>
          </div>
        </div>
      </div>
    </template>

    <template v-slot:right>
      <div class="p-RightRow">
        <h3 class="g-title-tertiary p-RightRow-title">選択中</h3>
        <div class="p-ColorInfo">
          <div
            class="p-ColorInfo-thumb"
            :style="{
              'background-image': `url(${selectingColor.image})`
            }"
          ></div>
          <div class="p-ColorInfo-content">
            <h4 class="g-title-quaternary">{{ selectingColor.name }}</h4>
            <p>{{ selectingColor.extra }}</p>
          </div>
        </div>
      </div>
    </template>
  </ContentBase>
</template>

<script>
import ContentBase from "./ContentBase";
import StoreMixin from "../../../mixins/StoreMixin";

export default {
  name: "ColorPage",
  mixins: [StoreMixin],
  components: {ContentBase},
  computed: {
    editingForm() {
      return this.state.editingForm;
    },
    colorNum() {
      return this.store.selectColorInfo();
    },
    options() {
      return this.colorNum.options;
    },
    selectingColor() {
      return this.options[this.editingForm.color_num];
    }
  },
  methods: {
    updateCurrentSelectingValStr() {
      this.store.updateCurrentSelectingValStr(this.selectingColor.name);
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
