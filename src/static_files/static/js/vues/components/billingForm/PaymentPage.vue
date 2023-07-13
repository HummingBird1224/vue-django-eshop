<template>
  <div>
    <div class="p-billingContent is-billing">
      <h1 class="p-billingContent-title">ご注文を確定させましょう</h1>
      <p class="p-billingContent-description">
        <span>お支払い情報を入力して、ご注文を確定させましょう。</span>
      </p>
      <div v-show="state.isUseDefaultCard">
        <div class="p-billingContent-paymentMethod">
          <div class="p-billingContent-paymentMethod-choice">
            <input type="radio" id="credit_card" v-model="state.paymentMethod" name="payment" value="credit_card">
            <label for="credit_card">
              <div class="p-billingContent-paymentMethod-choice-content">
                <div class="p-billingContent-paymentMethod-choice-header">
                  <h3>クレジットカード</h3>
                  <div class="p-billingContent-paymentMethod-choice-cardLogo"><img :src="staticUrl + 'img/card_logos/icon_visa.png'"></div>
                  <div class="p-billingContent-paymentMethod-choice-cardLogo"><img :src="staticUrl + 'img/card_logos/icon_mastercard.png'"></div>
                  <div class="p-billingContent-paymentMethod-choice-cardLogo"><img :src="staticUrl + 'img/card_logos/icon_americanexpress.png'"></div>
                  <div class="p-billingContent-paymentMethod-choice-cardLogo"><img :src="staticUrl + 'img/card_logos/icon_dinersclub.png'"></div>
                  <div class="p-billingContent-paymentMethod-choice-cardLogo"><img :src="staticUrl + 'img/card_logos/icon_jcb.png'"></div>
                </div>
                <div v-if="!!cards && 0 < cards.length">
                  <div class="p-billingAddress">
                    <header class="p-billingAddress-header">
                      <h3 class="g-title-tertiary">
                        <i class="fas fa-credit-card" />
                        デフォルトカードを使用する
                      </h3>
                      <a
                        class="c-textLink c-textLink--black"
                        href="#"
                        @click.prevent.stop="useOtherCard"
                      >
                        他のカードを使う
                      </a>
                    </header>
                    <div>
                      <p>****-****-****-{{ defaultCard.last4 }}</p>
                      <p>{{ defaultCard.name }}</p>
                      <p>{{ defaultCard.exp_year }}年{{ defaultCard.exp_month }}月</p>
                    </div>
                  </div>
                </div>

                <div v-show="!cards || cards.length === 0">
                  <p v-show="hasFirstElementError" class="payjp-error">{{ state.payjpError }}</p>
                  <div id="number-form1" class="payjp-outer"></div>
                  <div id="expiry-form1" class="payjp-outer"></div>
                  <div id="cvc-form1" class="payjp-outer"></div>
                </div>
              </div>
            </label>
          </div>
          <hr>
          <div class="p-billingContent-paymentMethod-choice">
            <input type="radio" id="bank_transfer" v-model="state.paymentMethod" name="payment" value="bank_transfer">
            <label for="bank_transfer">
              <div class="p-billingContent-paymentMethod-choice-content">
                <div class="p-billingContent-paymentMethod-choice-header">
                  <h3>銀行振込</h3>
                </div>
                <p>
                  国内の各銀行からお振込にてお支払いいただけます。<br>
                  払込先の情報は、購入確定後、メールにてお知らせいたします。
                </p>
                <p class="p-billingContent-paymentMethod-choice-tag">支払手数料 : 各銀行所定の手数料</p>
              </div>
            </label>
          </div>
        </div>

        <div class="p-billingAddress">
          <header class="p-billingAddress-header">
            <h3 class="g-title-tertiary">
              <svg>
                <use xlink:href='#icons-pin_drop'/>
              </svg>
              配送先
            </h3>
            <a
              class="c-textLink c-textLink--black"
              href="#"
              @click.prevent.stop="backToAddressPage"
            >
              編集
            </a>
          </header>

          <div
            class="p-billingAddress-content"
            v-html="deliveryAddressHtml"
          >
          </div>
        </div>
      </div>
      <div v-show="!state.isUseDefaultCard">
        <div v-for="card in cards" :key="card.id" class="p-billingAddress">
          <div>
            <input type="radio" :id="'card_' + card.id" v-model="state.selectedCardId" name="selectedCard" :value="card.id">
            <label :for="'card_' + card.id">
              <div class="p-billingContent-paymentMethod-choice-content">
                <p><span class="p-billingContent-paymentMethod-choice-cardLogo" v-if="cardBrandImages[card.brand]" v-html="cardBrandImages[card.brand]" />****-****-****-{{ card.last4 }}</p>
                <p>{{ card.name }}</p>
                <p>{{ card.exp_year }}年{{ card.exp_month }}月</p>
              </div>
            </label>
          </div>
          <hr>
        </div>

        <div class="p-billingContent-paymentMethod-choice">
          <input type="radio" id="card_new" v-model="state.selectedCardId" name="selectedCard" value="new">
          <label for="card_new">
            <div class="p-billingContent-paymentMethod-choice-content">
              <div class="p-billingContent-paymentMethod-choice-header">
                <h3>新しいクレジットカードを使う</h3>
                <div class="p-billingContent-paymentMethod-choice-cardLogo"><img :src="staticUrl + 'img/card_logos/icon_visa.png'"></div>
                <div class="p-billingContent-paymentMethod-choice-cardLogo"><img :src="staticUrl + 'img/card_logos/icon_mastercard.png'"></div>
                <div class="p-billingContent-paymentMethod-choice-cardLogo"><img :src="staticUrl + 'img/card_logos/icon_americanexpress.png'"></div>
                <div class="p-billingContent-paymentMethod-choice-cardLogo"><img :src="staticUrl + 'img/card_logos/icon_dinersclub.png'"></div>
                <div class="p-billingContent-paymentMethod-choice-cardLogo"><img :src="staticUrl + 'img/card_logos/icon_jcb.png'"></div>
              </div>
              <p v-show="hasSecondElementError" class="payjp-error">{{ state.payjpError }}</p>
              <div id="number-form2" class="payjp-outer"></div>
              <div id="expiry-form2" class="payjp-outer"></div>
              <div id="cvc-form2" class="payjp-outer"></div>
            </div>
          </label>
        </div>
      </div>
    </div>
    <PaymentFooter
      :isProcessing="state.isProcessing"
      :isUseDefaultCard="state.isUseDefaultCard"
      :selectedCardId="state.selectedCardId"
      @submit="submit"
    />
  </div>
</template>

<script>
import PaymentFooter from "./PaymentFooter";
import BillingFlow from "../../../constants/BillingFlow";
import range from "../../../helpers/range";

import { computed, reactive, onMounted } from 'vue';
import { useStore } from '../../providers/useStore';
import { useCreditCardForm } from '../../providers/useCreditCardForm';
export default {
  name: "PaymentPage",
  components: { PaymentFooter },
  setup() {
    // data
    const compState = reactive({
      isProcessing: false,
      isUseDefaultCard: true,
      selectedCardId: '',
      paymentMethod: 'credit_card',
      payjp: null,
      payjpError: "",
      numberElement1: null,
      numberElement2: null,
      isFirstElement: false,
    })

    const hasFirstElementError = computed(()=> compState.isFirstElement && compState.payjpError.length > 0);
    const hasSecondElementError = computed(()=> !compState.isFirstElement && compState.payjpError.length > 0);

    const { payjp, generateForm } = useCreditCardForm()

    compState.payjp = payjp

    const createCreditForm = () => {

      // カードが一つもないときのフォーム
      const { number: number1, expiry: expiry1, cvc: cvc1 } = generateForm()
      number1.mount('#number-form1')
      expiry1.mount('#expiry-form1')
      cvc1.mount('#cvc-form1')

      // 新規カードを登録するフォーム
      const { number: number2, expiry: expiry2, cvc: cvc2 } = generateForm()
      number2.mount('#number-form2')
      expiry2.mount('#expiry-form2')
      cvc2.mount('#cvc-form2')

      compState.numberElement1 = number1
      compState.numberElement2 = number2
      $(".payjp-outer iframe").css("height", "56px")
    }

    // providers
    const { store, state } = useStore();

    // computed
    const orderInfo = computed(()=>state.orderInfo)
    const staticUrl = computed(()=>state.staticUrl)
    const cards     = computed(()=>state.cards)
    const defaultCard = computed(()=>state.cards.find(card => card.is_default) || {})
    const cardBrandImages = computed(()=> {
      const staticUrlValue = staticUrl.value;
      return {
        Visa: `<img src="${staticUrlValue}img/card_logos/icon_visa.png">`,
        MasterCard: `<img src="${staticUrlValue}img/card_logos/icon_mastercard.png">`,
        'American Express': `<img src="${staticUrlValue}img/card_logos/icon_americanexpress.png">`,
        'Diners Club': `<img src="${staticUrlValue}img/card_logos/icon_dinersclub.png">`,
        JCB: `<img src="${staticUrlValue}img/card_logos/icon_jcb.png">`,
        Discover: `<img src="${staticUrlValue}img/card_logos/icon_discover.png">`,
      }
    })
    const deliveryAddressHtml = computed(()=>{
      let html = '';

      if (orderInfo.value && orderInfo.value.delivery_address) {
        const da = orderInfo.value.delivery_address;

        html += `${da.full_name} 〒${da.postal_code}<br>`;
        if (da.building)
          html += `${da.prefecture}${da.city} ${da.building}<br>`;
        else
          html += `${da.prefecture}${da.city}<br>`;
        html += `${da.tel}`
      }

      return html;
    });

    const yearSelections = computed(()=>{
      const date = new Date();
      const currentYear = date.getFullYear();
      return range(currentYear, currentYear + 20);
    })

    const monthSelections = computed(()=>range(1,12))

    // methods
    const backToAddressPage = () =>{ if (!compState.isProcessing) { store.setFlow(BillingFlow.ADDRESS) } }
    const useOtherCard = () => {
      if (defaultCard.value.hasOwnProperty('id')) {
        compState.selectedCardId = defaultCard.value.id;
      }
      compState.isUseDefaultCard = false;
    }

    // 新規カード追加
    const handleForm = async (isNew, useDefault)=> {
      const isFirstelement = isNew & useDefault;
      const element = isFirstelement ? compState.numberElement1 : compState.numberElement2;
      compState.isFirstElement = isFirstelement;

      try {
        const { id: token, error } = await compState.payjp.createToken(element)

        if (error) {
          throw error
        }
        if (isFirstelement) {
          const { data } = await store.postCharge({card: token, payment_method: compState.paymentMethod})
          location.href = data.redirect_to;
        } else {
          await store.createCredit({token});
          await store.loadCredits();
          compState.isUseDefaultCard = true; // 画面をもどす
        }
      } catch (e) {
        compState.payjpError = e.message;
      } finally {
        compState.isProcessing = false;
        setTimeout(()=> compState.payjpError = "", 2000);
      }
    };

    const submit = async ()=> {
      compState.isProcessing = true;
      if (compState.paymentMethod === 'bank_transfer') {
        const { data } = await store.postCharge({payment_method: compState.paymentMethod });
        compState.isProcessing = false;
        location.href = data.redirect_to;
        return
      }

      // card processing
      if (compState.isUseDefaultCard) {
        if (cards.value && cards.value.length) {
          const { data } = await store.postCharge({ payment_method: compState.paymentMethod })
          location.href = data.redirect_to;
          compState.isProcessing = false;
        } else {
          // カードがない場合
          handleForm(true, true)
        }
        return
      }

      // カード新規作成
      if (compState.selectedCardId !== 'new') {
        await store.changeCredit({id: compState.selectedCardId});
        await store.loadCredits();
        compState.isUseDefaultCard = true; // 画面をもどす
        compState.isProcessing = false;
        return
      }

      handleForm(true, false)
    };

    onMounted(() => {
      createCreditForm()
    })

    return {
      state: compState,
      orderInfo,
      staticUrl,
      cards,
      defaultCard,
      cardBrandImages,
      deliveryAddressHtml,
      yearSelections,
      monthSelections,
      backToAddressPage,
      useOtherCard,
      submit,
      hasFirstElementError,
      hasSecondElementError
    }
  }
}
</script>

<style scoped>
</style>
