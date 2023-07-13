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
        staticUrl: $el.data("static-url"),
        isShowingReorderModal: false,
        isShowingQuickOrderConfirmModal: false,
        loadedMyDesigns: null,
        orderSelection: [],
        selectedOrderPosition: 0,
        readOnlyOptions: null,
        selectedDesign: null,
        detailObject: {},
        instantBuyResponse: null,
        addressList: [],
        creditCardList: [],
        estimatedPriceObject: {},
      },
      showReorderModal() {
        this.state.isShowingReorderModal = true
      },
      closeReorderModal() {
        this.state.isShowingReorderModal = false
      },
      showQuickOrderConfirmModal() {
        this.state.isShowingQuickOrderConfirmModal = true
      },
      closeQuickOrderConfirmModal() {
        this.state.isShowingQuickOrderConfirmModal = false
      },
      deselectDesign() {
        this.state.selectedDesign = null
      },
      selectPosition(position) {
        this.state.selectedOrderPosition = position
      },
      selectDesign(design) {
        this.state.selectedDesign = design;
      },
      async getMyDesigns() {
        const { data } = await ApiManager.getMyDesigns();
        this.state.loadedMyDesigns = data.results;
      },
      async updateMyDesignName(id, newName) {
        try {
          await ApiManager.updateMyDesignName(id, newName);
          const finder = (el) => el.id == id;
          const index = this.state.loadedMyDesigns.findIndex(finder)
          if (index >= 0) {
            this.state.loadedMyDesigns[index].name = newName;
          } else {
            throw new Error("No element foud");
          }
        } catch (e) {
          console.error(e);
        }
      },
      async fetchReorderDetail(id) {
        const { data } = await ApiManager.getReorderMyDesign(id);
        this.state.orderSelection = data.options.items;
        this.state.selectedOrderPosition = this.state.orderSelection[0].position
        this.state.readOnlyOptions = data.read_only_options;
        const {
          name,
          product_name,
          slug,
          category,
          unit,
          image,
          shipping_date,
          read_only_options_str
        } = data;
        this.state.detailObject = {
          "name": name,
          "product_name": product_name,
          "slug": slug,
          "category": category,
          "unit": unit,
          "image": image,
          "shipping_date": shipping_date,
          "read_only_options_str": read_only_options_str
        }
      },
      async addCart() {
        const designId = this.state.selectedDesign.id;
        const selectedPosition = this.state.selectedOrderPosition;
        const selected = this.state.orderSelection.find(el=>el.position == selectedPosition)
        const quantity = parseInt(selected.value)
        const productSlug = this.state.detailObject.slug
        await ApiManager.addCartFromMyDesign(designId, quantity, this.state.readOnlyOptions, productSlug);
      },
      async instantBuy() {
        const designId = this.state.selectedDesign.id;
        const selectedPosition = this.state.selectedOrderPosition;
        const selected = this.state.orderSelection.find(el=>el.position == selectedPosition)
        const quantity = parseInt(selected.value)
        const productSlug = this.state.detailObject.slug
        const { data } = await ApiManager.getInstantBuyRequirementsInfo(designId, quantity, this.state.readOnlyOptions, productSlug);
        this.state.instantBuyResponse = data
      },
      async updateDefaultCard(cardId) {
        await ApiManager.updateInstantBuyDefaultCreditCart(cardId);
        const newElement = this.state.creditCardList.find(el => el.id == cardId)
        this.state.instantBuyResponse.card = newElement;
      },
      async upadteDefaultAddress(addressId) {
        await ApiManager.updateInstantBuyDefaultShippigAddress(addressId);
        const newElement = this.state.addressList.find(el => el.id == addressId)
        this.state.instantBuyResponse.address = newElement;
      },
      async fetchAddressList() {
        const { data } = await ApiManager.getShippingAddressListForInstantBuy()
        this.state.addressList = data.addresses
      },
      async fetchCreditCardList() {
        const { data } = await ApiManager.getCreditCardListForInstantBuy()
        this.state.creditCardList = data.cards
      },
      async orderInstantBuy(cardId, addressId, paymentMethod) {
        const designId = this.state.selectedDesign.id;
        const selectedPosition = this.state.selectedOrderPosition;
        const selected = this.state.orderSelection.find(el=>el.position == selectedPosition)
        const quantity = parseInt(selected.value)
        const productSlug = this.state.detailObject.slug;
        const { data } =  await ApiManager.orderInstantBuy(productSlug, this.state.readOnlyOptions, quantity, designId, cardId, addressId, paymentMethod);
        return data.redirect_to
      },
      async estimateOrder() {
        const quantities = this.state.orderSelection.map(el=>el.value);
        const productSlug = this.state.detailObject.slug;
        const designId = this.state.selectedDesign.id;
        const options = {
          ...this.state.readOnlyOptions,
          ...{
            "mydesign_id": designId,
            "from_mydesign": true,
          }
        }
        const { data } = await ApiManager.getEstimatedList(productSlug, options, quantities)
        this.state.estimatedPriceObject = data.prices;
      },
    });
    return this.store;
  }
}

export default new Store();
