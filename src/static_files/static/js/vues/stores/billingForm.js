import ApiManager from "../../helpers/ApiManager";
import { reactive } from 'vue';

class Store {
  constructor() {
    this.store = {};
  }

  getStore() {
    return this.store;
  }

  createStore($el) {
    this.store = reactive({
      state: {
        oid: $el.data('oid'),
        isLogin: $el.data('is-login') === 'True',
        staticUrl: $el.data('static-url'),
        colorMeUrl: $el.data('colorme-url'),
        baseUrl: $el.data('base-url'),
        flow: null,
        orderInfo: null,
        cards: null
      },
      setFlow(nextFlow) {
        this.state.flow = nextFlow;
      },
      fetchOrderInfo() {
        return ApiManager.getBillingOrderInfo()
          .then(res => {
            this.state.orderInfo = res.data;
          })
      },
      fetchCreditCards() {
        return ApiManager.getAccountsCredit().then(res => {
            this.state.cards = res.data.cards;
          })
      },
      postUserSignUp(formValue) {
        return ApiManager.postUserSignUp(formValue);
      },
      postDeliveryAddress(formValue) {
        return ApiManager.postCreateDeliveryAddress(formValue)
          .then(res => {
            this.state.orderInfo = {
              ...this.state.orderInfo,
              delivery_address: res.data.delivery_address,
            }
          });
      },
      postBillingAddress(formValue) {
        return ApiManager.postCreateBillingAddress(formValue)
//           .then(res => {
// //            this.state.orderInfo = {
// //                ...this.state.orderInfo,
// //                delivery_address: res.data.billing_address,
// //              };
//           });
      },
      postCharge(formValue) {
        return ApiManager.postBillingCharge(formValue);
      },
      loadCredits() {
        return ApiManager.getAccountsCredit().then(res => {
          this.state.cards = res.data.cards;
        })
      },
      createCredit(formValue) {
        return ApiManager.postAccountsCreditCreate(formValue);
      },
      changeCredit(formValue) {
        return ApiManager.postAccountsCreditChange(formValue);
      }
    });

    return this.store;
  }
}

export default new Store();
