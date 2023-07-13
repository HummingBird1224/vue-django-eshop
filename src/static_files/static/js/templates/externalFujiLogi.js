import App from '../vues/pages/ExternalFujiLogiForm.vue';
import Store from "../vues/stores/externalFujiLogiForm";
import { vueMount } from '../helpers/vueMount';

import 'swiper/swiper.scss'

const element = $('#js-external-fujilogi-form');
element.ready(() => {
  if (element.length) {
    vueMount(App,Store,element)
  }
})
