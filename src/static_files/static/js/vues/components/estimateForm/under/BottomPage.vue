<template>
  <ContentBase>
    <template v-slot:left>
      <div class="p-LeftRow">
        <h3 class="g-title-tertiary p-LeftRow-title">選択しましょう</h3>
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
                v-model="editingForm.bottom"
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
        <div class="p-BottomInfo">
          <div
            class="p-BottomInfo-thumb"
            :style="{
              'background-image': `url(${selectingBottom.image})`
            }"
          ></div>
          <div class="p-BottomInfo-content">
            <h4 class="g-title-quaternary">{{ selectingBottom.name }}</h4>
            <p>{{ selectingBottom.extra }}</p>
          </div>
        </div>
      </div>
    </template>
  </ContentBase>
</template>

<script>
import ContentBase from "./ContentBase.vue";
import StoreMixin from "../../../mixins/StoreMixin";

export default {
  name: "BottomPage",
  mixins: [StoreMixin],
  components: {ContentBase},
  computed: {
    editingForm() {
      return this.state.editingForm;
    },
    bottom() {
      return this.store.selectBottomInfo();
    },
    options() {
      return this.bottom.options;
    },
    selectingBottom() {
      return this.options[this.editingForm.bottom];
    }
  },
  methods: {
    updateCurrentSelectingValStr() {
      this.store.updateCurrentSelectingValStr(this.selectingBottom.name);
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
