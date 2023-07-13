import App from '../vues/pages/CasestudyList.vue';
import Store from '../vues/stores/casestudyList';
import { vueMount } from '../helpers/vueMount';

const element = $('#js-casestudy-list');
element.ready(() => {
  if (element.length) {
    vueMount(App, Store, element);
  }
});
