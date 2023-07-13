import { configure, defineRule } from 'vee-validate';
import App from '../vues/pages/internal/custom/CreateCustomProduct.vue';
import Store from '../vues/stores/internal/custom/createCustomProduct';
import { vueMount } from '../helpers/vueMount';
import { localize } from '@vee-validate/i18n/vee-validate-i18n';
import { required } from '@vee-validate/rules';
import ja from '@vee-validate/i18n/locale/ja.json';

const element = $('#js-internal-create-custom-product')
element.ready(() => {
  if (element.length) {
    vueMount(App, Store, element)
  }
});
