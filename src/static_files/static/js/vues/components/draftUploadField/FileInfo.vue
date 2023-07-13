<template>
  <div class="p-File">
    <div class="p-UploadInfo-detail" v-if="orderInfo">
      <div class="p-UploadInfo-file">
        <img :src="`${staticUrl}img/icon_file_sm.png`"/>
        <p>
          {{ orderInfo.design.filename }}
        </p>
      </div>
      <a class="c-textLink" :href="orderInfo.design.data">データを確認する</a>
    </div>
  </div>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin";

export default {
  name: "FileInfo",
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
