<template>
  <div class="p-UploadInfo">
    <h5 class="g-title-quinary p-UploadInfo-title">入稿したデータ</h5>

    <div class="p-UploadInfo-detail" v-if="orderInfo.design.data">
      <div class="p-UploadInfo-file">
        <img :src="`${staticUrl}img/icon_file_sm.png`"/>
        <p>
          {{ orderInfo.design.filename }}
          <span>{{ orderInfo.design.size }}</span>
        </p>
      </div>
      <a class="c-textLink" :href="orderInfo.design.data">データを確認する</a>
    </div>
    <div class="p-UploadInfo-detail" v-else>
      <p>データ入稿不要なためデザインデータはありません。</p>
    </div>
  </div>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin";

export default {
  name: "UploadCompleted",
  mixins: [StoreMixin],
  computed: {
    orderInfo() {
      return this.state.orderInfo;
    },
    staticUrl() {
      return this.state.staticUrl;
    }
  }
}
</script>

<style scoped>

</style>
