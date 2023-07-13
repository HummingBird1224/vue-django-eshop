<template>
  <ContentBase>
    <template v-slot:left>
      <div class="p-LeftRow p-LeftRow--small">
        <h3 class="g-title-tertiary p-LeftRow-title">選択しましょう</h3>

        <div class="c-form-item p-RawMaterialSelections">
          <div class="c-form-radioGroup">
            <label class="c-form-radio">
              <input type="radio" class="c-form-radioInput" name="radio01" checked="">
              <span class="c-form-radioMark"></span>
              <span class="p-RawMaterialSelectionLabel">
                    <span class="p-RawMaterialSelectionLabel-thumb"></span>
                    <span class="p-RawMaterialSelectionLabel-content">
                      <span class="p-RawMaterialSelectionLabel-title">白ダンボール</span>
                      <span class="p-RawMaterialSelectionLabel-body">
                        通常の材質です。<br>
                        アルミの光沢感があります
                      </span>
                    </span>
                  </span>
            </label>
            <label class="c-form-radio">
              <input type="radio" class="c-form-radioInput" name="radio01">
              <span class="c-form-radioMark"></span>
              <span class="p-RawMaterialSelectionLabel">
                    <span class="p-RawMaterialSelectionLabel-thumb"></span>
                    <span class="p-RawMaterialSelectionLabel-content">
                      <span class="p-RawMaterialSelectionLabel-title">白ダンボール</span>
                      <span class="p-RawMaterialSelectionLabel-body">
                        光沢が抑えられ、手触りがツルツルした印象の素材です。
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
        <div class="p-ThicknessInfo">
          <div class="p-ThicknessInfo-thumb"></div>
          <div class="p-ThicknessInfo-content">
            <h4 class="g-title-quaternary">通常の厚さ 1.5mm</h4>
            <p>このタイプで標準の厚さです。</p>
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
  name: "CardBoardThicknessPage",
  mixins: [StoreMixin],
  components: {ContentBase},
  computed: {
    editingForm() {
      return this.state.editingForm;
    }
  }
}
</script>

<style scoped>

</style>
