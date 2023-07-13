import App from '../vues/pages/ExternalColorMeForm.vue';
import Store from "../vues/stores/externalColorMeForm";
import { vueMount } from '../helpers/vueMount';

import 'swiper/swiper.scss'

const element = $('#js-external-color-me-form');
element.ready(() => {
  if (element.length) {
    vueMount(App,Store,element)
  }
})
