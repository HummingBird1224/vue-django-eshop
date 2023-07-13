<template>
  <div class="p-UploadField">
    <div class="p-UploadField-icons">
      <img :src="`${staticUrl}img/icon_ai_file.png`"/>
      <img :src="`${staticUrl}img/icon_pdf_file.png`"/>
    </div>

    <p>{{ description }}</p>
    <a
      class="c-textLink"
      href="#"
      @click.prevent.stop="openUploadModal"
    >
      クリックしてファイル選択へ
    </a>
  </div>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin";
import DraftFlow from "../../../constants/DraftFlow";

export default {
  name: "UploadField",
  mixins: [StoreMixin],
  computed: {
    flow() {
      return this.state.flow;
    },
    staticUrl() {
      return this.state.staticUrl;
    },
    description() {
      if (this.flow === DraftFlow.RE_SUBMITTION_REQUEST) {
        return '修正した入稿データを再アップロード';
      }

      return '作成した入稿データをアップロード';
    }
  },
  methods: {
    openUploadModal() {
      this.store.openUploadModal();
    }
  }
}
</script>

<style scoped>

</style>
