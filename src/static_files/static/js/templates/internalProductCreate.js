import App from '../vues/pages/internal/ProductCreate.vue';
import Store from '../vues/stores/internal/productCreate';
import { vueMount } from '../helpers/vueMount';

const element = $('#js-internal-product-create');
element.ready(() => {
  if (element.length) {
    vueMount(App, Store, element)
  }
});
