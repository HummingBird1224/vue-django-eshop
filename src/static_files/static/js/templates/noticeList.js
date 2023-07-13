import App from '../vues/pages/NoticeList.vue';
import Store from '../vues/stores/noticeList';
import { vueMount } from '../helpers/vueMount';

const element = $('#js-notice-list');
element.ready(() => {
  if (element.length) {
    vueMount(App, Store, element);
  }
});
