import App from '../vues/pages/internal/NoticePostList.vue';
import Store from '../vues/stores/internal/noticePostList';
import { vueMount } from '../helpers/vueMount';

const element = $('#js-internal-notice-post');
element.ready(() => {
  if (element.length) {
    vueMount(App, Store, element)
  }
});
