import App from '../vues/pages/ExternalFutureShopForm.vue';
import Store from "../vues/stores/externalFutureShopForm";
import { vueMount } from '../helpers/vueMount';

import 'swiper/swiper.scss'

const element = $('#js-external-future-shop-form');
element.ready(() => {
  if (element.length) {
    vueMount(App,Store,element)
  }
})
