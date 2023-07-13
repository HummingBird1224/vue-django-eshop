<template>
  <ContentBase>
    <template v-slot:left>
      <div class="p-LeftRow p-LeftRow--small">
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
                v-model="editingForm.special_print"
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
        <div class="p-PaperProcessInfo">
          <div
            class="p-PaperProcessInfo-thumb"
            :style="{
              'background-image': `url(${selectingSpecialPrint.image})`
            }"
          ></div>
          <div class="p-PaperProcessInfo-content">
            <h4 class="g-title-quaternary">{{ selectingSpecialPrint.name }}</h4>
            <p>{{ selectingSpecialPrint.extra }}</p>
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
  name: "SpecialPrintPage",
  mixins: [StoreMixin],
  components: {ContentBase},
  computed: {
    editingForm() {
      return this.state.editingForm;
    },
    specialPrint() {
      return this.store.selectSpecialPrintInfo();
    },
    options() {
      return this.specialPrint.options;
    },
    selectingSpecialPrint() {
      return this.options[this.editingForm.special_print];
    }
  },
  methods: {
    updateCurrentSelectingValStr() {
      this.store.updateCurrentSelectingValStr(this.selectingSpecialPrint.name);
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
