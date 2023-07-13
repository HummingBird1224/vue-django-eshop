import { defineRule } from 'vee-validate';
import { required } from '@vee-validate/rules';
import { localize } from '@vee-validate/i18n/vee-validate-i18n';
import App from '../vues/pages/Cart.vue';
import Store from '../vues/stores/cart';
import { vueMount } from '../helpers/vueMount';

const element = $('#js-cart');
element.ready(() => {
  if (element.length) {
    defineRule('required', required);
    localize('ja');
    vueMount(App, Store, element)
  }
});
