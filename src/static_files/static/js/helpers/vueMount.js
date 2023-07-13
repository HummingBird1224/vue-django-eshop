import 'regenerator-runtime';
import VueSmoothScroll from 'vue3-smooth-scroll';
import { createApp, h, reactive } from 'vue';
import toPriceFormat from '../vues/filters/toPriceFormat.js';
import { setLocale } from "yup";
import * as ja from "yup-locale-ja";

export const vueMount = (App, Store, element) => {
  setLocale(ja.descriptive);
  const store = Store.createStore(element);
  const app = createApp({ render() { return h(App) }})
  app.provide('store', store)
  app.config.globalProperties = {
    store: reactive(store),
    $filters: { toPriceFormat },
  }
  app.use(VueSmoothScroll)
  app.mount(element.get(0));
}
