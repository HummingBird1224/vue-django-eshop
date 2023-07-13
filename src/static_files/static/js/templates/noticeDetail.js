import App from '../vues/pages/NoticeDetail.vue';
import Store from '../vues/stores/noticeDetail';
import { vueMount } from '../helpers/vueMount';

const element = $('#js-notice-detail');
element.ready(() => {
  if (element.length) {
    vueMount(App, Store, element);
  }
});
