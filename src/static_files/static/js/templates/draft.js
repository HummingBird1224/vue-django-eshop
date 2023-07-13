import { defineRule } from 'vee-validate';
import { localize } from '@vee-validate/i18n/vee-validate-i18n';
import { required } from '@vee-validate/rules';
import App from '../vues/pages/DraftUploadField.vue';
import Store from '../vues/stores/draftUploadField';
import { vueMount } from '../helpers/vueMount';

$(document).ready(() => {
  const element = $('#js-draft-upload-filed')
  if (element.length) {
    defineRule('required', required);
    localize('ja');
    vueMount(App, Store, element)
  }
});
