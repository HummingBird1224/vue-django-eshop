import App from '../vues/pages/Thankyou.vue'
import Store from '../vues/stores/thankyou'
import { vueMount } from '../helpers/vueMount';

const element = $('#js-thankyou');
element.ready(() => {
  vueMount(App, Store, element);
});
