<template>
  <ModalWindow
    :isShow="isShow"
    class="c-modal--white">
    <div
      ref="modalContent"
      class="p-quickorderModal"
    >
      <div
        class="p-quickorderModal-contents"
       v-if="isDesignSelected">
        <div class="contents-header bottom-border">
          <div class="product-title">
            <div class="product-photo" :style="{ backgroundImage: `url(${selectedDesign.image})`}">
            </div>
            <h1> {{ selectedDesign.name }} </h1>
          </div>
          <div class="close-button" @click="close">
            <svg>
              <use xlink:href='#icons-cross'/>
            </svg>
          </div>
        </div>
        <div class="contents-wrapper">
          <transition name="slide-fade">
            <div v-if="isShowingSelectionComponent" class="selection-component">
              <div @click="applyDefaultSelection"  class="selection-header bottom-border is-selectable">
                <div class="arrow-icon_wrapper">
                  <svg class="arrow-icon">
                    <use xlink:href='#icons-arrow_forward'/>
                  </svg>
                </div>
                <span class="selection-type_label"> {{ selectedComponentTitle }} </span>
              </div>
              <ul class="available-selections bottom-border">
                <li class="available-selection is-selectable" v-for="(selection, i) in componentSelection" :key="i" @click="selectIndex(i)">
                  <input type="radio" :checked="i == selectedPosition" />
                  <div class="selection-detail">
                    <span v-for="(element, i) in selection" :key='i'> {{ element }} </span>
                  </div>
                </li>
              </ul>
              <div class="selection-footer">
                <span @click="addOptionalSelection">新しい{{ isPayment ? 'お支払い手段' :'お届け先住所'}}を追加</span>
              </div>
            </div>
          </transition>
          <div v-if="!isShowingSelectionComponent">
            <div @click="selectAddressList" class="current-select__label bottom-border is-selectable">
              <span class="selection-title">お届け先</span>
              <div class="selection-container">
                <div class="selection-detail">
                  <span> {{ defaultAddressName }}</span>
                  <span> {{ defaultAddressPostalCode }} {{ defaultAddress }} </span>
                </div>
                <span class="change-button">変更</span>
              </div>
            </div>
            <div class="current-select__label partial-selectable bottom-border">
              <span class="selection-title">お支払い</span>
              <div class="payment-selection">
                <div class="payment-method  is-selectable" @click="changePaymentMethod('credit_card')">
                  <input type="radio" :checked="paymentMethod == 'credit_card'" @change="changePaymentMethod('credit_card')"/>
                  <div class="creditcard-payment-detail">
                    <span>クレジットカード</span>
                    <span class="current-creditcard"> {{ defaultCreditCard }} </span>
                  </div>
                  <span class="change-button" @click="selectPaymentsList"> 変更 </span>
                </div>
                <div class="payment-method is-selectable" @click="changePaymentMethod('bank_transfer')">
                  <input type="radio" :checked="paymentMethod == 'bank_transfer'" @change="changePaymentMethod('bank_transfer')"/>
                  <span> 銀行振り込み </span>
                </div>
              </div>
            </div>
            <div class="current-select__label bottom-border">
              <span class="selection-title">合計</span>
              <div class="selection-detail">
                <span> {{ $filters.toPriceFormat(totalPrice) }}円 (税込) </span>
              </div>
            </div>
            <div class="order-button_container" @click="orderInstantBuy">
              <div class="submit-order c-btn" :class="isOrdering ? 'is-loading' : ''">注文を確定する</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </ModalWindow>
</template>

<script>
import ModalWindow from "../common/ModalWindow";
import { ref, computed } from 'vue';
import { useStore } from '../../providers/useStore';

export default {
  name: "QuickOrderConfirmModal",
  components: {ModalWindow},
  props: {
    isShow: {
      type: Boolean,
    },
  },
  setup(props, context) {
    // datas
    const selectedComponentTitle = ref("お支払い")
    const isShowingSelectionComponent = ref(false)
    const componentSelection = ref([])
    const selectedPosition = ref(0)
    const paymentMethod = ref('credt_card')
    const isOrdering = ref(false)

    const { store, state } = useStore();

    // computed
    const isDesignSelected = computed(()=>state.selectedDesign != null)
    const isPayment = computed(()=>selectedComponentTitle.value === 'お支払い')
    const selectedDesign = computed(()=>state.selectedDesign)
    const instantBuyResponse = computed(()=>state.instantBuyResponse)
    const hasInstantBuyResponse = computed(() => state.instantBuyResponse != null)
    const defaultAddress = computed(()=> {
      if (!hasInstantBuyResponse.value) return "";
      return state.instantBuyResponse.address.address;
    })
    const defaultAddressName = computed(()=> {
      if (!hasInstantBuyResponse.value) return "";
      return instantBuyResponse.value.address.name
    })

    const defaultAddressPostalCode = computed(()=> {
      if (!hasInstantBuyResponse.value) return "";
      return instantBuyResponse.value.address.postal_code
    })
    const defaultCreditCard = computed(()=> {
      if (!hasInstantBuyResponse.value) return "";
      const { card } = state.instantBuyResponse;
      return `${card.brand} *${card.last4}`
    })

    const totalPrice = computed(()=> {
      if (!hasInstantBuyResponse.value) return "";
      const { prices } = state.instantBuyResponse;
      return prices.total
    })

    // methods
    const changePaymentMethod = (method) => paymentMethod.value = method;
    const selectPaymentsList = () => {
      selectedComponentTitle.value = 'お支払い';
      componentSelection.value = state.creditCardList.map(el=>[`${el.brand} *${el.last4}`]);
      selectedPosition.value = state.creditCardList.findIndex(el => el.id == state.instantBuyResponse.card.id)
      isShowingSelectionComponent.value = true;
    }

    const selectAddressList = () => {
      selectedComponentTitle.value = 'お届け先';
      componentSelection.value = state.addressList.map(el=> [`${el.name}`, `〒${el.postal_code} ${el.address}`])
      selectedPosition.value = state.addressList.findIndex(el => el.id == state.instantBuyResponse.address.id)
      isShowingSelectionComponent.value = true;
    }

    const applyDefaultSelection = async ()=>{
      const isPaymentSelected = isPayment.value;
      const newSelectedId = isPaymentSelected ? state.creditCardList[selectedPosition.value].id : state.addressList[selectedPosition.value].id;
      const defaultSelectedId = isPaymentSelected ? state.instantBuyResponse.card.id : state.instantBuyResponse.address.id
      if (defaultSelectedId == newSelectedId) {
        isShowingSelectionComponent.value = false;
        return
      }
      try {
        if (isPaymentSelected) {
          await store.updateDefaultCard(newSelectedId);
        } else {
          await store.upadteDefaultAddress(newSelectedId);
        }
      } finally {
        isShowingSelectionComponent.value = false;
      }
    }

    const selectIndex = (index) => selectedPosition.value = index;

    const close = () => context.emit('close');
    const orderInstantBuy = async () => {
      isOrdering.value = true;
      const { card, address } = state.instantBuyResponse;
      const redirect_to = await store.orderInstantBuy(card.id, address.id, paymentMethod.value);
      isOrdering.value = false;
      location.href = redirect_to;
    }

    const addOptionalSelection = async () => {
      if (isPayment.value) {
        location.href= "/accounts/credit/"
      } else {
        location.href= "/accounts/address/"
      }
    }

    return {
      selectedComponentTitle,
      isShowingSelectionComponent,
      componentSelection,
      selectedPosition,
      paymentMethod,
      isOrdering,
      isPayment,
      isDesignSelected,
      selectedDesign,
      instantBuyResponse,
      defaultAddress,
      defaultAddressName,
      defaultAddressPostalCode,
      defaultCreditCard,
      hasInstantBuyResponse,
      totalPrice,
      changePaymentMethod,
      selectPaymentsList,
      selectAddressList,
      applyDefaultSelection,
      selectIndex,
      close,
      orderInstantBuy,
      addOptionalSelection,
    }
  }
}
</script>

<style scoped>
.slide-fade-enter-active {
  transition: all .4s ease;
}
.slide-fade-leave-active {
  transition: none;
}

.slide-fade-enter {
  transform: translateX(-20px);
  opacity: 0;
}

.slide-fade-leave-to {
  transform: translateX(-20px);
  opacity: 0;
}
</style>
