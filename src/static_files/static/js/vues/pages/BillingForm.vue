<template>
  <div class="p-billingForm">
    <div class="p-billingForm-body">
      <Header/>
      <Flow/>

      <Navigation/>

      <transition name="fade">
        <LoginPage
          v-if="isLoginPage(flow)"
        />
      </transition>

      <transition name="fade">
        <MailSendPage
          v-if="isMailSend(flow)"
        />
      </transition>

      <transition name="fade">
        <AddressPage
          v-if="isAddressPage(flow)"
        />
      </transition>

      <transition name="fade">
        <PaymentPage
          v-if="isPayment(flow)"
        />
      </transition>
    </div>

    <Cart
      v-if="orderInfo"
    />
  </div>
</template>

<script>
import Header from "../components/billingForm/Header";
import Navigation from "../components/billingForm/Navigation";
import Flow from "../components/billingForm/Flow";
import Cart from "../components/billingForm/Cart";
import LoginPage from "../components/billingForm/LoginPage";
import AddressPage from "../components/billingForm/AddressPage";
import PaymentPage from "../components/billingForm/PaymentPage";
import BillingFlow from "../../constants/BillingFlow";
import MailSendPage from "../components/billingForm/MailSendPage";

import { useStore } from "../providers/useStore";
import { reactive, computed, onBeforeMount, onMounted } from 'vue';

export default {
  name: "BillingForm",
  components: {MailSendPage, PaymentPage, AddressPage, LoginPage, Cart, Flow, Navigation, Header},
  setup(props, context) {
    // data
    const compState = reactive({
      isOrderInfoFetching: false,
    })

    // providers
    const { store, state } = useStore();

    const isLogin = computed(() => state.isLogin);
    const flow = computed(() => state.flow);
    const orderInfo = computed(() => state.orderInfo);

    const isLoginPage = (flow) => flow === BillingFlow.LOGIN;
    const isMailSend = (flow) => flow === BillingFlow.MAIL_SEND
    const isAddressPage = (flow) => flow === BillingFlow.ADDRESS
    const isPayment = (flow) => flow === BillingFlow.PAYMENT

    const didFetched = () => {
      // ログインしていて、
      // 住所入力済みなら -> PAYMENT
      // していなければ  -> ADDRESS
      // delivery_addressは新規登録時に値がすべてnullなレコードが作られる. つまり、delivery_addressのnullチェックのみでは住所入力済み判定にならない.
      // first_nameはrequiredなのでそれを住所を登録しているかのフラグとする.
      // 20200402 first_nameからpostal_codeに変更
      if (orderInfo.value.delivery_address && orderInfo.value.delivery_address.postal_code) {
        store.setFlow(BillingFlow.PAYMENT);
      } else {
        store.setFlow(BillingFlow.ADDRESS);
      }
    }

    onBeforeMount(async () => {
      if (!isLogin.value) {
        store.setFlow(BillingFlow.LOGIN);
        compState.isOrderInfoFetching = true;
        await store.fetchOrderInfo();
        compState.isOrderInfoFetching = false;
        return
      }

      await store.fetchCreditCards();
      compState.isOrderInfoFetching = true;
      await store.fetchOrderInfo();
      didFetched()
      compState.isOrderInfoFetching = false;
    })

    return {
      state: compState,
      isLogin,
      flow,
      orderInfo,
      isLoginPage,
      isMailSend,
      isAddressPage,
      isPayment
    }
  }
}
</script>

<style scoped>
  .fade-enter-active, .fade-leave-active {
    transition: opacity .1s
  }

  .fade-enter, .fade-leave {
    opacity: 0
  }
</style>
