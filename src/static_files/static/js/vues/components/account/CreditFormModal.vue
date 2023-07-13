<template>
  <ModalWindow :isShow="isShow">
    <div ref="modalContent" class="contentWrapper">
      <div class="contentBody">
        <h3 class="g-title-tertiary" style="margin-bottom: 2rem;"><i class="fas fa-credit-card" />クレジットカードの追加</h3>
        <p class="payjp-error">{{ state.payjpError }}</p>
        <div id="number-form" class="payjp-outer"></div>
        <div id="expiry-form" class="payjp-outer"></div>
        <div id="cvc-form" class="payjp-outer"></div>
        <div class="buttonContent">
            <div class="buttonContainer cancel" @click="cancelled">キャンセル</div>
            <div class="buttonContainer ok" @click="submit" :class="{ 'is-loading': state.isProcessing }">登録する</div>
        </div>
      </div>
    </div>
  </ModalWindow>
</template>

<script>
import ModalWindow from "../common/ModalWindow";
import TextInput from "../common/TextInput";
import PasswordInput from "../common/PasswordInput";
import SelectInput from "../common/SelectInput";
import range from "../../../helpers/range";
import { computed, onMounted, reactive } from 'vue';
import { useStore } from "../../providers/useStore";
import { useCreditCardForm } from "../../providers/useCreditCardForm";

export default {
  name: "CreditFormModal",
  components: { ModalWindow, SelectInput, PasswordInput, TextInput },
  props: {
    isShow: {
      type: Boolean,
    },
  },
  setup(props, context) {
    const compState = reactive({
      payjp: null,
      payjpError: "",
      numberElement:null,
      isProcessing: false
    })
    const yearSelections = computed(()=> {

      const date = new Date();
      const currentYear = date.getFullYear();

      return range(currentYear, currentYear + 20);
    })

    const monthSelections = computed(()=>{
      return range(1, 12);
    })

    const { store } = useStore();

    const { payjp, generateForm } = useCreditCardForm();
    compState.payjp = payjp;


    const submit = async () => {

      if (compState.isProcessing) {
        return
      }

      compState.isProcessing = true;

      try {
        const { id: token, error } = await compState.payjp.createToken(compState.numberElement)
        if (error) {
          throw error
        }
        await store.createCredit({ token })
        await store.loadCredits()
        context.emit('close')

      } catch (e) {
        compState.payjpError = e.message;
        compState.isProcessing = false;
        setTimeout(()=>{
          compState.payjpError  = ""
        }, 2000)
      } finally {
        compState.isProcessing = false;
      }
    }

    onMounted(() => {
      const { number, expiry, cvc } = generateForm();
      number.mount('#number-form')
      expiry.mount('#expiry-form')
      cvc.mount('#cvc-form')
      $(".payjp-outer iframe").css("height", "56px")
      compState.numberElement = number;
    })

    const cancelled = () => {
      context.emit('close')
    }

    return {
      yearSelections,
      monthSelections,
      submit,
      cancelled,
      state: compState,
    }
  }
}

</script>

<style scoped>
.c-modal {
  background: rgba(255, 255, 255, 0.64) !important;
}
.contentWrapper {
  position: absolute;
  left: 0;
  right: 0;
  padding: 48px 46px 64px;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}

.draftDeleteCaustionText {
  margin-top: 24px;
}
.contentBody {
  padding: 44px;
  background: white;
  width: 600px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  box-shadow: 2px 2px 20px rgba(0, 0, 0, 0.08);
  border-radius: 8px;
}

.buttonContent {
  display: flex;
  width: 100%;
  justify-content: flex-end;
  flex-direction: row;
  margin-top: 24px;
}

.buttonContainer {
  padding: 8px 16px;
  font-weight: bold;
  border-radius: 20px;
  margin: 0 14px;
  cursor: pointer;
}

.ok {
  color: white;
  background: #205efb;
}

.is-disabled {
  cursor: default;
  pointer-events: none;
  color: #A0A0AA;
  border: 0.5px solid #DADBDD;
  background-color: #DADBDD;
}

@keyframes loading {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}

.is-loading {
  font-size: 0;
  cursor: default;
  pointer-events: none;
  background-color: #FFFFFF;
}

.is-loading::after {
  display: inline-block;
  content: "";
  border-radius: 50%;
  width: 19.5px;
  height: 19.5px;
  border-top: 1px solid #FFFFFF;
  border-right: 1px solid #FFFFFF;
  border-bottom: 1px solid #205efb;
  border-left: 1px solid #205efb;
  animation: loading 0.9s infinite linear;
}

.cancel {
  color: #a0a0aa;
  font-weight: bold;
}

.error-text {
  color: red;
}
</style>
