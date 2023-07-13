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
        isInitialized: false,
        addresses: null
      },
      async loadAddresses() {
        const { data } = await ApiManager.getAccountsAddress()
        this.state.addresses = data.addresses;
      },
      createAddress(formValue) {
        return ApiManager.postAccountsAddressCreate(formValue);
      },
      deleteAddress(formValue) {
        return ApiManager.postAccountsAddressDelete(formValue);
      },
      changeAddress(formValue) {
        return ApiManager.postAccountsAddressChange(formValue);
      }
    });

    return this.store;
  }
}

export default new Store();
