<template>
  <div class="p-UploadField">
    <svg class='p-UploadField-statusIcon'>
      <use xlink:href='#icons-zoom_in'/>
    </svg>

    <p>運営で入稿データをチェック中です...</p>
<!--    <a-->
<!--      class="c-textLink"-->
<!--      href="#"-->
<!--      @click.prevent.stop="openUploadModal"-->
<!--    >完了したらブラウザの通知でお知らせする</a>-->
    <div class="p-UploadSuccess-btn">
      <a
        class="c-textLink"
        href=""
        @click.prevent.stop="showUploadField"
      >
        別のデータを再アップロードする場合はこちら
      </a>
    </div>
  </div>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin";
import DraftFlow from "../../../constants/DraftFlow";

export default {
  name: "UploadChecking",
  mixins: [StoreMixin],
  methods: {
    openUploadModal() {
      this.store.openUploadModal();
    },
    showUploadField() {
      this.store.setFlow(DraftFlow.NOT_SUBMITTED);
      this.store.clearUploadedData();
    }
  }
}
</script>

<style scoped>

</style>
