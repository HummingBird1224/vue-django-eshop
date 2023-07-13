import App from '../vues/pages/ProductList.vue';
import Store from '../vues/stores/productList';
import { vueMount } from '../helpers/vueMount';

const element = $('#js-product-list');
element.ready(() => {
  if (element.length) {
    vueMount(App, Store, element);
  }
});
