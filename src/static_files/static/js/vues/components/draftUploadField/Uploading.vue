<template>
  <div class="p-Uploading">
    <img :src="`${staticUrl}img/icon_file.png`"/>
    <p>アップロード中...</p>
    <div class="p-Uploading-status">
      <span
        :style="progressBarStyle"
      ></span>
    </div>
  </div>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin";

export default {
  name: "Uploading",
  mixins: [StoreMixin],
  computed: {
    progressBarStyle() {
      return {
        width: `${this.state.uploadPercentCompleted}%`
      };
    },
    staticUrl() {
      return this.state.staticUrl;
    }
  }
}
</script>

<style scoped>

</style>
