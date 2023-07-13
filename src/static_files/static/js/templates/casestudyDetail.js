import { defineRule } from 'vee-validate';
import { localize } from '@vee-validate/i18n/vee-validate-i18n';
import { required } from '@vee-validate/rules';
import App from '../vues/pages/CasestudyDetail.vue';
import Store from '../vues/stores/casestudyList';

import { vueMount } from '../helpers/vueMount';

const element = $('#js-casestudy-detail')
element.ready(() => {
  if (element.length) {
    defineRule('required', required);
    localize('ja');
    vueMount(App, Store, element)
  }
});
