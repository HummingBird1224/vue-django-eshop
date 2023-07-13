import App from '../vues/pages/Home.vue';
import Store from '../vues/stores/home';
import { vueMount } from '../helpers/vueMount';

const element = $('#js-home');
element.ready(() => {
  if (element.length) {
    vueMount(App, Store, element)
  }
});
