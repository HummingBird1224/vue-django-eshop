<template>
<ModalWindow :isShow="isShow" class="c-modal--white" @close="close">
  <div class="content-wrapper">
    <div class="image-upload__container">
      <div class="upload-form__header">
        <h4>画像のアップロード</h4>
          <div class="upload-form__close-button" @click="close">
            <span>×</span>
          </div>
      </div>
      <div id="upload-form__box">
        <img :src="staticUrl() + 'img/upload_file_select.png'" class="file-sample__image" />
        <span>ドラッグしてアップロード</span>
        <label>
          <input type="file" @change="fileInput"/>
        </label>
      </div>
      <div class="file-input-error__container">
        <span
          v-if="hasFileInputError"
          class="file-input-error__text-label"
        >{{ errorText }}</span>
      </div>
    </div>
  </div>
</ModalWindow>
</template>

<script>
import ModalWindow from "../common/ModalWindow";
import StoreMixin from "../../mixins/StoreMixin";
import analyze from "rgbaster";
import ImageUtils from "../../../utils/ImageUtils.js";

export default {
  name: "EasyDraftUploadModal",
  mixins: [StoreMixin],
  components: { ModalWindow },
  props: {
    isShow: {
      type: Boolean,
    },
  },
  emits: ['close', 'file-uploaded'],
  data() {
    return {
      isLoadingFile: false,
      errorText: "",
    }
  },
  computed: {
    hasFileInputError()  {
      return this.errorText.length > 0;
    }
  },
  methods: {
    clearError() {
      this.errorText = "";
    },
    staticUrl() {
      return this.state.staticUrl;
    },
    close() {
      this.$emit('close');
    },
    isImage(file) {
      const filename = file.name;
      return filename.toUpperCase().match(/\.(png|jpeg|jpg|svg)$/i)
    },
    async loadImage(file) {

    },
    async validateColors(imgBuffer) {
      let results = await analyze(imgBuffer)
      let validatedColor = results;
      if (results.length > 1) {
        if (results[1].count / results[0].count < 0.06) {
          validatedColor = results.slice(0, 1);
        } else {
          validatedColor = results.slice(0, 2);
        }
      }
     return validatedColor
        .map((result) => result.color)
        .map((colorString) => {
          let result = colorString.match(/rgb\(([0-9]+),([0-9]+),([0-9]+)\)/)

          if (result == null) {
            result = colorString.match(/rgba\(([0-9]+),([0-9]+),([0-9]+),([0-9]+)\)/)
          }
          return result.slice(1, 4).map((v) => parseInt(v))
          }
        )
        .map((c) => this.nearValidation(c))
        .reduce((val, cur) => val && cur);
    },
    nearValidation(color) {
      return ImageUtils.isNearWhite(color) || ImageUtils.isNearBlack(color)
    },
    fileInput(e) {
      this.uploadImage(e.target.files[0])
    },
    async uploadImage(file) {

      if (this.isLoadingFile) {
        return
      }

      this.isLoadingFile = true;

      if (!this.isImage(file)) {
        this.displayError("非対応のファイルフォーマットです。");
        return;
      }

      const reader = new FileReader();
      reader.onload = async (e) => {
        this.processingText = "画像を検証中です...";
        let imgBuffer = e.target.result;

        if (!this.validateColors(imgBuffer)) {
          this.displayError("非対応のファイルフォーマットです。");
          return;
        }

        // 親にイベントを送る
        this.$emit('file-uploaded', imgBuffer);
        this.isLoadingFile = false;
      };
      reader.readAsDataURL(file);
    },
    displayError(errorText) {
      // 読み込み中のデータをリセット
      this.isLoadingFile = false;
      // エラー文言を表示する
      this.errorText = errorText;
      // ローディング

      setTimeout(this.clearError, 3000);
    },
    enableDropForm() {
      const dropForm = document.getElementById("upload-form__box");
      dropForm.addEventListener('dragover', (e)=>{
        e.stopPropagation();
        e.preventDefault();
        dropForm.style.backgroundColor = "rgba(0,0,0,0.1)"
      })
      dropForm.addEventListener('dragleave',  (e)=>{
        e.stopPropagation();
        e.preventDefault();
        dropForm.style.backgroundColor = "rgba(0,0,0,0.02)"
      });

      dropForm.addEventListener('drop', async (e) =>{
        e.stopPropagation();
        e.preventDefault();
        await this.uploadImage(e.dataTransfer.files[0])
        dropForm.style.backgroundColor = "rgba(0,0,0,0.02)"
      });
    },
  },
  mounted() {
    this.enableDropForm();
  }

}
</script>
<style scoped>

.content-wrapper {
  position: absolute;
  left: 0;
  right: 0;
  padding: 48px 46px 64px;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

</style>
