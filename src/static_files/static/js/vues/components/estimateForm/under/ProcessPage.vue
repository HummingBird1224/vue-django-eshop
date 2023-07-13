<template>
  <ContentBase>
    <template v-slot:left>
      <div>
        <div
          v-if="kadomaru"
          class="p-LeftRow p-LeftRow--small"
        >
          <h3 class="g-title-tertiary p-LeftRow-title">角丸の選択</h3>
          <div class="c-form-item p-ProcessSelections">
            <div class="c-form-radioGroup">
              <label
                v-for="(option, key) in kadomaruOptions"
                :key="key"
                class="c-form-radio"
              >
                <input
                  type="radio"
                  class="c-form-radioInput"
                  name="radio01"
                  :value="key"
                  v-model="editingForm.kadomaru"
                >
                <span class="c-form-radioMark"></span>
                {{ option.name }}
              </label>
            </div>
          </div>
        </div>

        <div
          v-if="notch"
          class="p-LeftRow p-LeftRow--small"
        >
          <h3 class="g-title-tertiary p-LeftRow-title">ノッチの選択</h3>
          <div class="c-form-item p-ProcessSelections">
            <div class="c-form-radioGroup">
              <label
                v-for="(option, key) in notchOptions"
                :key="key"
                class="c-form-radio"
              >
                <input
                  type="radio"
                  class="c-form-radioInput"
                  name="radio02"
                  :value="key"
                  v-model="editingForm.notch"
                >
                <span class="c-form-radioMark"></span>
                {{ option.name }}
              </label>
            </div>
          </div>
        </div>

        <div
          v-if="zipper"
          class="p-LeftRow p-LeftRow--small"
        >
          <h3 class="g-title-tertiary p-LeftRow-title">ジッパーの選択</h3>
          <div class="c-form-item p-ProcessSelections">
            <div class="c-form-radioGroup">
              <label
                v-for="(option, key) in zipperOptions"
                :key="key"
                class="c-form-radio"
              >
                <input
                  type="radio"
                  class="c-form-radioInput"
                  name="radio03"
                  :value="key"
                  v-model="editingForm.zipper"
                >
                <span class="c-form-radioMark"></span>
                {{ option.name }}
              </label>
            </div>
          </div>
        </div>
      </div>
    </template>

    <template v-slot:right>
      <div class="p-RightRow">
        <h3 class="g-title-tertiary p-RightRow-title">選択中</h3>
        <ul class="p-ProcessInfoList">
          <li
            v-if="kadomaru"
            class="p-ProcessInfo"
          >
            <div
              class="p-ProcessInfo-thumb"
              :style="selectingKadomaruThumbStyle"
            ></div>
            <div class="p-ProcessInfo-content">
              <h4 class="g-title-quaternary">角丸</h4>
              <p>{{ selectingKadomaru.name }}</p>
            </div>
          </li>

          <li
            v-if="notch"
            class="p-ProcessInfo"
          >
            <div
              class="p-ProcessInfo-thumb"
              :style="selectingNotchThumbStyle"
            ></div>
            <div class="p-ProcessInfo-content">
              <h4 class="g-title-quaternary">ノッチ</h4>
              <p>{{ selectingNotch.name }}</p>
            </div>
          </li>

          <li
            v-if="zipper"
            class="p-ProcessInfo"
          >
            <div
              class="p-ProcessInfo-thumb"
              :style="selectingZipperThumbStyle"
            ></div>
            <div class="p-ProcessInfo-content">
              <h4 class="g-title-quaternary">ジッパー</h4>
              <p>{{ selectingZipper.name }}</p>
            </div>
          </li>
        </ul>
      </div>
    </template>
  </ContentBase>
</template>

<script>
import ContentBase from "./ContentBase.vue";
import StoreMixin from "../../../mixins/StoreMixin";

export default {
  name: "ProcessPage",
  mixins: [StoreMixin],
  components: {ContentBase},
  computed: {
    editingForm() {
      return this.state.editingForm;
    },
    process() {
      return this.store.selectProcessInfo();
    },
    kadomaru() {
      return this.process.options.kadomaru;
    },
    notch() {
      return this.process.options.notch;
    },
    zipper() {
      return this.process.options.zipper;
    },
    kadomaruOptions() {
      return this.kadomaru.options;
    },
    notchOptions() {
      return this.notch.options;
    },
    zipperOptions() {
      return this.zipper.options;
    },
    selectingKadomaru() {
      return this.kadomaru.options[this.editingForm.kadomaru];
    },
    selectingKadomaruThumbStyle() {
      const style = {};

      if (this.selectingKadomaru && this.selectingKadomaru.image) {
        style['background-image'] = `url(${this.selectingKadomaru.image})`;
      }

      return style;
    },
    selectingNotch() {
      return this.notch.options[this.editingForm.notch];
    },
    selectingNotchThumbStyle() {
      const style = {};

      if (this.selectingNotch && this.selectingNotch.image) {
        style['background-image'] = `url(${this.selectingNotch.image})`;
      }

      return style;
    },
    selectingZipper() {
      return this.zipper.options[this.editingForm.zipper];
    },
    selectingZipperThumbStyle() {
      const style = {};

      if (this.selectingZipper && this.selectingZipper.image) {
        style['background-image'] = `url(${this.selectingZipper.image})`;
      }

      return style;
    }
  },
  methods: {
    updateCurrentSelectingValStr() {
      this.store.updateCurrentSelectingValStr(this.store.getProcessValueStr(this.editingForm));
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
