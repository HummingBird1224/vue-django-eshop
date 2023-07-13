import App from '../vues/pages/ExternalBaseForm.vue';
import Store from "../vues/stores/externalBaseForm";
import { vueMount } from '../helpers/vueMount';

import 'swiper/swiper.scss'

const element = $('#js-external-base-form');
element.ready(() => {
  if (element.length) {
    vueMount(App, Store, element)
  }
})

