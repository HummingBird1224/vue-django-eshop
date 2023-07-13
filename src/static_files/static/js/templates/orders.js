import App from '../vues/pages/Reorder.vue';
import Store from "../vues/stores/reorderForm";
import { vueMount } from '../helpers/vueMount';
import { createApp, h,  } from "vue";
import OrdersUploadedModal from "../vues/pages/OrdersUploadedModal.vue";
import OrderCompleteModal from "../vues/pages/OrderCompleteModal.vue";

import OrderListApp from '../vues/pages/OrderList.vue';
import OrderListStore from '../vues/stores/orderList.js';

const mountOrderList = () => {
  const orderList = $('#js-order-list')
  if (orderList.length) {
    vueMount(OrderListApp, OrderListStore, orderList)
  }
};

const element = $('#js-reorder-form');

element.ready(() => {
  mountOrderList();

  if (element.length) {
    vueMount(App, Store, element)
  }

  const el1 = $('#js-uploaded-modal');
  const el2 = $('#js-completed-modal');

  if (el1.length) {
    createApp({
      render() {
        return h(OrdersUploadedModal)
      },
    }).mount(el1.get(0))
  }

  if (el2.length) {
    createApp({
      render() {
        return h(OrderCompleteModal)
      },
    }).mount(el2.get(0))
  }
});
