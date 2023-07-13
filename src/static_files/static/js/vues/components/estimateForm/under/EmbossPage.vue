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
                v-model="editingForm.emboss"
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
              'background-image': `url(${selectingEmboss.image})`
            }"
          ></div>
          <div class="p-PaperProcessInfo-content">
            <h4 class="g-title-quaternary">{{ selectingEmboss.name }}</h4>
            <p>{{ selectingEmboss.extra }}</p>
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
  name: "EmbossPage",
  mixins: [StoreMixin],
  components: {ContentBase},
  computed: {
    editingForm() {
      return this.state.editingForm;
    },
    emboss() {
      return this.store.selectEmbossInfo();
    },
    options() {
      return this.emboss.options;
    },
    selectingEmboss() {
      return this.options[this.editingForm.emboss];
    }
  },
  methods: {
    updateCurrentSelectingValStr() {
      this.store.updateCurrentSelectingValStr(this.selectingEmboss.name);
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
