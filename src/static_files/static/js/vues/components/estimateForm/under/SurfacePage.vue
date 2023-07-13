<template>
  <ContentBase>
    <template v-slot:left>
      <div>
        <div
          v-if="surfaceMaterial"
          class="p-LeftRow p-LeftRow--small"
        >
          <h3 class="g-title-tertiary p-LeftRow-title">表面生地の選択</h3>

          <div class="c-form-item p-RawMaterialSelections">
            <div class="c-form-radioGroup">
              <label
                v-for="(option, key) in surfaceMaterialOptions"
                :key="key"
                class="c-form-radio"
              >
                <input
                  type="radio"
                  class="c-form-radioInput"
                  name="radio01"
                  :value="key"
                  v-model="editingForm.surface_material"
                >
                <span class="c-form-radioMark"></span>
                <span class="p-RawMaterialSelectionLabel">
                    <span
                      v-if="option.image"
                      class="p-RawMaterialSelectionLabel-thumb"
                      :style="{
                        'background-image': `url(${option.image})`
                      }"
                    ></span>
                    <span class="p-RawMaterialSelectionLabel-content">
                      <span class="p-RawMaterialSelectionLabel-title">{{ option.name }}</span>
                      <span class="p-RawMaterialSelectionLabel-body">{{ option.extra }}</span>
                    </span>
                  </span>
              </label>
            </div>
          </div>
        </div>

        <div
          v-if="surfaceProcess"
          class="p-LeftRow p-LeftRow--small"
        >
          <h3 class="g-title-tertiary p-LeftRow-title">表面加工の選択</h3>

          <div class="c-form-item p-RawMaterialSelections">
            <div class="c-form-radioGroup">
              <label
                v-for="(option, key) in surfaceProcessOptions"
                :key="key"
                class="c-form-radio"
              >
                <input
                  type="radio"
                  class="c-form-radioInput"
                  name="radio02"
                  :value="key"
                  v-model="editingForm.surface_process"
                >
                <span class="c-form-radioMark"></span>
                <span class="p-RawMaterialSelectionLabel">
                    <span
                      v-if="option.image"
                      class="p-RawMaterialSelectionLabel-thumb"
                      :style="{
                        'background-image': `url(${option.image})`
                      }"
                    ></span>
                    <span class="p-RawMaterialSelectionLabel-content">
                      <span class="p-RawMaterialSelectionLabel-title">{{ option.name }}</span>
                      <span class="p-RawMaterialSelectionLabel-body">{{ option.extra }}</span>
                    </span>
                  </span>
              </label>
            </div>
          </div>
        </div>
      </div>
    </template>

    <template v-slot:right>
      <div class="p-RightRow">
        <div class="p-RawMaterialInfoList p-RawMaterialInfoList--no-main-title">
          <div
            v-if="surfaceMaterial"
            class="p-RawMaterialInfo"
          >
            <h3 class="g-title-tertiary p-RawMaterialInfo-title">選択中：表面生地</h3>

            <div class="p-RawMaterialInfo-body">
              <div
                v-if="selectingSurfaceMaterial.image"
                class="p-RawMaterialInfo-thumb"
                :style="{
                  'background-image': `url(${selectingSurfaceMaterial.image})`
                }"
              ></div>
              <div class="p-RawMaterialInfo-content p-RawMaterialInfo-content--large">
                <h4 class="g-title-quaternary">{{ selectingSurfaceMaterial.name }}</h4>
                <p>{{ selectingSurfaceMaterial.extra }}</p>
                <a class="c-textLink js-open-color-list-modal-btn" href="">印刷に使用可能な色が限られます。色のリストはこちら。</a>
              </div>
            </div>
          </div>

          <div
            v-if="surfaceProcess"
            class="p-RawMaterialInfo"
          >
            <h3 class="g-title-tertiary p-RawMaterialInfo-title">選択中：表面加工</h3>

            <div class="p-RawMaterialInfo-body">
              <div
                v-if="selectingSurfaceProcess.image"
                class="p-RawMaterialInfo-thumb"
                :style="{
                  'background-image': `url(${selectingSurfaceProcess.image})`
                }"
              ></div>
              <div class="p-RawMaterialInfo-content p-RawMaterialInfo-content--large">
                <h4 class="g-title-quaternary">{{ selectingSurfaceProcess.name }}</h4>
                <p>{{ selectingSurfaceProcess.extra }}</p>
                <a class="c-textLink js-open-color-list-modal-btn" href="">印刷に使用可能な色が限られます。色のリストはこちら。</a>
              </div>
            </div>
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
  name: "SurfacePage",
  mixins: [StoreMixin],
  components: {ContentBase},
  computed: {
    editingForm() {
      return this.state.editingForm;
    },
    surfaceMaterial() {
      return this.store.selectSurfaceMaterialInfo();
    },
    surfaceProcess() {
      return this.store.selectSurfaceProcessInto();
    },
    surfaceMaterialOptions() {
      return this.surfaceMaterial.options;
    },
    surfaceProcessOptions() {
      return this.surfaceProcess.options;
    },
    selectingSurfaceMaterial() {
      return this.surfaceMaterialOptions[this.editingForm.surface_material];
    },
    selectingSurfaceProcess() {
      return this.surfaceProcessOptions[this.editingForm.surface_process];
    }
  },
  methods: {
    updateCurrentSelectingValStr() {
      this.store.updateCurrentSelectingValStr(this.store.getSurfaceValueStr(this.editingForm));
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
