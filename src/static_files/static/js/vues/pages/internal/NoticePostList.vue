<template>
  <div class="noticeInternal">
    <div class="noticeInternalList">
      <div class="listFunction">
        <div class="queryContainer">
          <img :src="`${staticUrl}img/search.svg`" class="queryIcon"/>
          <input type="text" placeholder="投稿タイトルで検索" class="query" v-model="keyword">
        </div>
      </div>
      <div class="listFunction">
        <div class="postCreateContainer clickable">
          <a href="/internal/notices/new">投稿作成</a>
        </div>
      </div>
      <div class="listTableContainer">
        <div class="listTable">
          <table>
            <tr>
              <th>投稿タイトル</th>
              <th>作成日時</th>
              <th>最終編集日時</th>
              <th>公開日時</th>
              <th>編集</th>
              <th></th>
            </tr>
            <tr v-for="post in noticePostList" :key="post.id">
              <td>{{ post.post_title }}</td>
              <td>{{ formatDate(post.created_at, 'yyyy年M月d日 HH:MM:ss') }}</td>
              <td>{{ formatDate(post.last_edited_at, 'yyyy年M月d日 HH:MM:ss') }}</td>
              <td v-if="post.published_at">{{ formatDate(post.published_at, 'yyyy年M月d日 HH:MM:ss') }}</td>
              <td v-else>非公開</td>
              <td class="middle">
                <a :href="post.id">
                  <button class="c-btn listTableContainer-publish-btn">編集</button>
                </a>
              </td>
              <td></td>
            </tr>
          </table>
        </div>
        <div class="pagination">
          <a v-if="previousPage" class="pagination-item" @click="loadPreviousNotices()" href="#">{{ currentPageNumber-1 }}</a>
          <a class="pagination-item-now">{{ currentPageNumber }}</a>
          <a v-if="nextPage" class="pagination-item" @click="loadNextNotices()" href="#">{{ currentPageNumber+1 }}</a>
        </div> 
      </div>
    </div>
  </div>
</template>


<script>
import DateUtils from "../../../utils/DateUtils";
import StoreMixin from "../../mixins/StoreMixin";

export default {
  name: "NoticePostList",
  mixins: [StoreMixin],
  components: {},
  data() {
    return {
      keyword: '',
    }
  },
  computed: {
    noticePostList() {
      return this.state.noticePostList;
    },
    staticUrl() {
      return this.state.staticUrl;
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
  },
  created() {
    this.store.fetchNoticePost()
  },
  methods: {
    formatDate(dateStr, format) {
      return DateUtils.dateFormat(new Date(dateStr), format);
    },
    loadPreviousNotices() {
      this.store.loadPreviousNoticePosts();
    },
    loadNextNotices() {
      this.store.loadNextNoticePosts();
    },
  },
  watch: {
    keyword: function() {
      this.store.fetchNoticePost(this.keyword)
    }
  }
}
</script>
