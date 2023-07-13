import ApiManager from "../../../helpers/ApiManager";
import { reactive } from "vue";
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
        staticUrl: $el.data('static-url'),
        cards: []
      },
      postCardToPayJp(card) {
        return new Promise(function (resolve, reject) {
          Payjp.createToken(card, function (status, response) {
            if (status === 200) {
              resolve(response);
            } else {
              reject(response);
            }
          });
        });
      },
      async loadCredits() {
        const { data } = await ApiManager.getAccountsCredit()
        this.state.cards = data.cards;
      },
      createCredit(formValue) {
        return ApiManager.postAccountsCreditCreate(formValue);
      },
      deleteCredit(formValue) {
        return ApiManager.postAccountsCreditDelete(formValue);
      },
      changeCredit(formValue) {
        return ApiManager.postAccountsCreditChange(formValue);
      }
    });

    return this.store;
  }
}

export default new Store();
