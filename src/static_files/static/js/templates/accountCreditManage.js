import App from '../vues/pages/account/CreditManage.vue';
import Store from '../vues/stores/account/creditManage';
import { vueMount } from '../helpers/vueMount';

const element =  $('#js-account-credit-manage');
element.ready(() => {
  if (element.length) {
    vueMount(App, Store, element)
  }
});
