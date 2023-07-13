import { defineRule } from 'vee-validate';
import { localize } from '@vee-validate/i18n/vee-validate-i18n';
import { required } from '@vee-validate/rules';
import App from '../vues/pages/ProductDetail.vue';
import Store from '../vues/stores/productDetail';

import { vueMount } from '../helpers/vueMount';

const element = $('#js-product-detail')
element.ready(() => {
  if (element.length) {
    defineRule('required', required);
    localize('ja');
    vueMount(App, Store, element)
  }
});
