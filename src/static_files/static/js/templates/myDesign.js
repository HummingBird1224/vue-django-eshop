import App from "../vues/pages/MyDesign.vue";
import Store from "../vues/stores/myDesign";
import { vueMount } from '../helpers/vueMount';

const element = $('#js-mydesign');
element.ready(() => {
  if (element.length) {
    vueMount(App, Store, element)
  }
});
