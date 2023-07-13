<template>
  <div class="p-noticePostBody">
    <header class="p-noticePostTitle">
      <h2 class="g-title-secondary">{{ noticeTitle }}</h2>
    </header>
    <div class="p-noticePostText">
      {{ noticeText }}
    </div>
    <div class="p-noticePostLinks">
      <div class="p-noticePostLinks-link">
        <a class="button secondaryAction" href="/notices/">一覧に戻る</a>
      </div>
    </div>
  </div>
</template>

<script>
import StoreMixin from "../mixins/StoreMixin";

export default {
  name: "NoticeDetail",
  mixins: [StoreMixin],
  components: {},
  data: () => ({
  }),
  computed: {
    noticeTitle() {
      return this.state.noticeTitle
    },
    noticeText() {
      return this.state.noticeText
    }
  },
}
</script>

<style scoped>
</style>
