<template>
  <div class="p-noticeList">
    <header class="p-orderedListHeader">
      <h2 class="g-title-secondary">お知らせ一覧</h2>
    </header>
    <ol v-if="noticeList" class="p-orderedNoticeList">
      <li v-for="notice in noticeList" :key="notice.id"
          class="p-orderedNotice badge">
        <img class="p-orderedNotice-itemIcon" :src="staticUrl + `${notice.icon_path}`">
        <div class="p-orderedNotice-item">
          <header class="p-orderedNotice-header">{{ notice.message }}</header>
          <a v-if="notice.reminders" class="js-read-notice" 
              :href="`/orders/history/${notice.reminders.orderitem_ref_code}`" @click="markRead(notice.id)"><p>注文番号：{{ notice.reminders.orderitem_ref_code }}</p></a>
          <a v-else class="js-read-notice" 
              :href="notice.id" @click="markRead(notice.id)"><p>お知らせの詳細：{{ notice.posts.title }}</p></a>
          
          <span v-show="!notice.read" class="p-orderedNotice-badge"></span>
          
        </div>
      </li>
    </ol>

    <p v-else>お知らせはありません。</p>
    
    <div class="p-noticeList-pagination">
      <li v-if="previousPage" class="p-noticeList-pagination-item"><a class="p-noticeList-pagination-link" @click="loadPreviousNotices()" href="#">{{ currentPageNumber-1 }}</a></li>
      <li class="p-noticeList-pagination-item p-noticeList-pagination-item--active"><a class="p-noticeList-pagination-link">{{ currentPageNumber }}</a></li>
      <li v-if="nextPage" class="p-noticeList-pagination-item"><a class="p-noticeList-pagination-link" @click="loadNextNotices()" href="#">{{ currentPageNumber+1 }}</a></li>
    </div>
  </div>
</template>

<script>
import StoreMixin from "../mixins/StoreMixin";

export default {
  name: "NoticeList",
  mixins: [StoreMixin],
  components: {},
  data: () => ({
  }),
  computed: {
    noticeList() {
      return this.state.noticeList
    },
    previousPage() {
      return this.state.previousPage
    },
    currentPageNumber() {
      return this.state.currentPageNumber
    },
    nextPage() {
      return this.state.nextPage
    },
    staticUrl() {
      return this.state.staticUrl;
    },
  },
  mounted() {
    this.store.fetchNoticeList()
  },
  methods: {
    loadPreviousNotices() {
      this.store.loadPreviousNotices();
    },
    loadNextNotices() {
      this.store.loadNextNotices();
    },
    markRead(value) {
      this.store.markNoticeRead(value)
    }
  }
}
</script>

<style scoped>
</style>
