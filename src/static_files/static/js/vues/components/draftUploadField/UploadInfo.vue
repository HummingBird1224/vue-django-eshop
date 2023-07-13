<template>
  <div class="p-UploadInfo">
    <div class="p-UploadInfo-detail">
      <div class="p-UploadInfo-file">
        <img :src="`${staticUrl}img/icon_file_sm.png`"/>
        <p>
          {{ uploadFileName }}
          <span>{{ uploadFileSize }}</span>
        </p>
      </div>
      <a
        class="c-textLink"
        href="#"
        @click.prevent.stop="showUploadView"
      >
        別のファイルをアップロード
      </a>
    </div>
    <div class="p-UploadInfo-cta">
      <p>このデータでよければ入稿を完了させましょう</p>
      <a
        class="c-btn c-btn--primary"
        :class="{
          'is-loading': isProcessing
        }"
        href=""
        @click.prevent.stop="confirmDesign"
      >
        データ入稿を完了する
      </a>
    </div>
  </div>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin";

export default {
  name: "UploadInfo",
  mixins: [StoreMixin],
  data: () => ({
    isProcessing: false,
  }),
  computed: {
    uploadFileName() {
      return this.state.uploadFileName;
    },
    uploadFileSize() {
      return this.state.uploadFileSize;
    },
    staticUrl() {
      return this.state.staticUrl;
    }
  },
  methods: {
    showUploadView() {
      this.store.clearUploadedData();
    },
    confirmDesign() {
      if (this.isProcessing) {
        return;
      }

      this.isProcessing = true;

      this.store.postConfirmUpload()
        .then(() => {
          location.href = '/orders/history/?uploaded=true';
        })
        .finally(() => {
          this.isProcessing = false;
        })
    }
  }
}
</script>

<style scoped>

</style>
