import { setLocale } from "yup";
import * as ja from "yup-locale-ja";
import App from '../vues/pages/account/AddressManage.vue';
import Store from '../vues/stores/account/addressManage';
import { vueMount } from '../helpers/vueMount';

const element =  $('#js-account-address-manage');
element.ready(() => {
  if (element.length) {
    setLocale(ja.descriptive);
    vueMount(App, Store, element)
  }
});
