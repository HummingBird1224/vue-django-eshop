import { defineRule } from 'vee-validate';
import { required } from '@vee-validate/rules';
import { localize } from '@vee-validate/i18n/vee-validate-i18n';
import App from '../vues/pages/EstimateForm.vue';
import Store from "../vues/stores/estimateForm";
import { vueMount } from '../helpers/vueMount';

$(document).ready(() => {
  const element = $('#js-estimate-form')
  if (element.length) {
    defineRule('required', required);
    localize('ja');
    vueMount(App, Store, element)
  };
  }
)
