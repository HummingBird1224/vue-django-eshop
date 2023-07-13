<template>
  <div class="p-UploadSuccess">
    <h5 class="g-title-quinary">データに問題ない場合は最終確認へ進みましょう</h5>
    <p>
      <svg class="time">
        <use xlink:href='#icons-access_time'/>
      </svg>
      最終確定後、印刷・加工工程に移り出荷予定日が確定します
    </p>
    <p>
      <svg class="delivery">
        <use xlink:href='#icons-airport_shuttle'/>
      </svg>
      最終確認後、約3週間程度でお手元に到着いたします
    </p>
    <div class="p-UploadSuccess-btn">
      <a
        class="c-btn c-btn--green"
        href=""
        @click.prevent.stop="showCheckDraftModal"
      >
        最終確認へ進む
        <svg>
          <use xlink:href='#icons-arrow_forward'/>
        </svg>
      </a>
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
  name: "UploadSuccess",
  mixins: [StoreMixin],
  methods: {
    showCheckDraftModal() {
      this.store.openCheckDraftModal();
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
