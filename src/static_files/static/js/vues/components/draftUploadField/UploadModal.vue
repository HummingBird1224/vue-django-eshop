<template>
  <ModalWindow
    :isShow="isShow"
  >
    <div
      ref="modalContent"
      class="p-draftModal p-draftModal--upload"
    >
      <header class="p-draftModalHeader">
        <h2 class="g-title-secondary">作成したデータをアップロード</h2>
        <a
          href="#"
          @click.prevent.stop="close"
        >
          <svg>
            <use xlink:href='#icons-cross'/>
          </svg>
        </a>
      </header>

      <div class="p-ModalUpload">
        <div class="p-ModalUpload-left">
          <h3 class="g-title-tertiary">アップ前に、データのチェックエリストをご活用ください</h3>
          <ul>
            <li class="c-form-item">
              <label class="c-form-checkbox">
                <input class="c-form-checkboxInput" type="checkbox">
                <span class="c-form-checkboxMark">
                      <i class="material-icons">done</i>
                    </span>
                作成したデータは注文する商品サイズと合っていますか？
              </label>
            </li>

            <li class="c-form-item">
              <label class="c-form-checkbox">
                <input class="c-form-checkboxInput" type="checkbox">
                <span class="c-form-checkboxMark">
                      <i class="material-icons">done</i>
                    </span>
                カラーモードはCMYKになっていますか？
              </label>
            </li>

            <li class="c-form-item">
              <label class="c-form-checkbox">
                <input class="c-form-checkboxInput" type="checkbox">
                <span class="c-form-checkboxMark">
                      <i class="material-icons">done</i>
                    </span>
                フルカラー（CMYK）印刷以外の場合、印刷する色数や加工別に色の置き換えは済んでいますか？
              </label>
            </li>

            <li class="c-form-item">
              <label class="c-form-checkbox">
                <input class="c-form-checkboxInput" type="checkbox">
                <span class="c-form-checkboxMark">
                      <i class="material-icons">done</i>
                    </span>
                リンクされた配置画像など、必要なデータは揃っていますか？
              </label>
            </li>

            <li class="c-form-item">
              <label class="c-form-checkbox">
                <input class="c-form-checkboxInput" type="checkbox">
                <span class="c-form-checkboxMark">
                      <i class="material-icons">done</i>
                    </span>
                文字はアウトライン化されていますか？
              </label>
            </li>

            <li class="c-form-item">
              <label class="c-form-checkbox">
                <input class="c-form-checkboxInput" type="checkbox">
                <span class="c-form-checkboxMark">
                      <i class="material-icons">done</i>
                    </span>
                紙の端にかかるデザインの場合、塗り足しは3mmありますか？
              </label>
            </li>
          </ul>
        </div>

        <div class="p-ModalUpload-right">
          <div class="p-UploadField-icons">
            <img :src="`${staticUrl}img/icon_ai_file.png`"/>
            <img :src="`${staticUrl}img/icon_pdf_file.png`"/>
          </div>

          <p>ファイルをドラッグ&ドロップ</p>
          <label class="c-textLink" href="#" style="cursor: pointer;">
            <svg>
              <use xlink:href='#icons-upload'/>
            </svg>
            クリックしてアップロード
            <input
              ref="inputFile"
              type="file"
              style="display:none"
              accept=".ai,.pdf"
              @change="onChangeFile"
            >
          </label>
        </div>
      </div>
    </div>
  </ModalWindow>
</template>

<script>
import ModalWindow from "../common/ModalWindow";
import StoreMixin from "../../mixins/StoreMixin";

export default {
  name: "UploadModal",
  mixins: [StoreMixin],
  components: {ModalWindow},
  props: {
    isShow: {
      type: Boolean,
    }
  },
  emits: ['close'],
  computed: {
    staticUrl() {
      return this.state.staticUrl;
    }
  },
  methods: {
    close() {
      this.$emit('close');
    },
    onChangeFile(e) {
      const file = e.target.files[0];
      const fileName = $(this.$refs.inputFile).prop('files')[0].name;

      // 拡張子判定.
      if (!fileName.toUpperCase().match(/\.(ai|pdf)$/i)) {
        return false;
      }

      this.state.uploadFileName = fileName;

      this.close();
      this.store.postUploadFile(file);
    }
  },
  mounted() {
    document.addEventListener("click", e => {
      const target = (e.target || e.srcElement).closest(".p-draftModal");
      if (!this.isShow || target === this.$refs.modalContent) return;

      this.close();
    });
  }
}
</script>

<style scoped>

</style>
