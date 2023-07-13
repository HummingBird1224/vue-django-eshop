<template>
  <ModalWindow :isShow="isShow">
    <div ref="modalContent" class="contentWrapper">
      <div class="contentBody">
        <h3 class="g-title-tertiary" style="margin-bottom: 2rem;"><svg><use xlink:href='#icons-pin_drop'/></svg>配送先</h3>
        <form>
          <div>

            <div class="c-form-col">
              <TextInput
                name="name"
                label="名前"
                rules="required"
              />
            </div>
            <div v-if="Object.keys(state.resErrors).includes('name')" class="formErrors">
              <p v-for="err in state.resErrors.name">{{ err }}</p>
            </div>

            <div class="c-form-col c-form-col--half">
              <TextInput
                name="postal_code"
                label="郵便番号"
                rules="required"
              />
              <SelectInput
                name="prefecture"
                label="都道府県"
                placeholder="都道府県"
                :options="state.prefectures"
                rules="required"
              />
            </div>
            <div v-if="Object.keys(state.resErrors).includes('postal_code')" class="formErrors">
              <p v-for="err in state.resErrors.postal_code">{{ err }}</p>
            </div>
            <div v-if="Object.keys(state.resErrors).includes('prefecture')" class="formErrors">
              <p v-for="err in state.resErrors.prefecture">{{ err }}</p>
            </div>

            <small>※現在、北海道、沖縄への配送は対応しておりません。</small>
            <div class="c-form-col">
              <TextInput
                name="city"
                label="市区町村・番地・建物"
                rules="required"
              />
            </div>
            <div v-if="Object.keys(state.resErrors).includes('city')" class="formErrors">
              <p v-for="err in state.resErrors.city">{{ err }}</p>
            </div>

            <div class="c-form-col c-form-col--half">
              <TextInput
                name="tel"
                label="電話番号"
                rules="required"
              />
            </div>
            <div v-if="Object.keys(state.resErrors).includes('tel')" class="formErrors">
              <p v-for="err in state.resErrors.tel">{{ err }}</p>
            </div>

          </div>
          <div class="buttonContent">
            <div class="buttonContainer cancel" @click="cancelled">キャンセル</div>
            <div class="buttonContainer ok" @click="submit" :class="{ 'is-disabled': !hasNoError, 'is-loading': state.isProcessing }">登録する</div>
          </div>
        </form>
      </div>
    </div>
  </ModalWindow>
</template>

<script>
import ModalWindow from "../common/ModalWindow";
import TextInput from "../common/TextInput";
import SelectInput from "../common/SelectInput";
import { reactive, watch, inject } from 'vue';
import { useForm, ErrorMessage } from 'vee-validate';
import { PREFECTURES } from '../../../constants/Prefectures'
import { useStore } from '../../providers/useStore';
import { useFormValidation } from '../../providers/formValidation'

export default {
  name: "AddressFormModal",
  components: { ModalWindow, SelectInput, TextInput, ErrorMessage },
  props: {
    isShow: {
      type: Boolean,
    },
  },
  setup(props, context) {
    const compstate = reactive({
      isProcessing: false,
      errors: [],
      prefectures:PREFECTURES,
      resErrors: {},
    });

    const { store, state } = useStore();
    const { handleSubmit, errors, values, resetForm } = useForm();
    const { hasNoError } = useFormValidation(errors, values, 0);

    const cancelled = () => {
      resetForm();
      context.emit("close");
    }
    const submit = handleSubmit(async (form) => {
      if (state.isProcessing) {
        return;
      }

      compstate.isProcessing = true;
      const address = {
        name: form.name,
        postal_code: form.postal_code,
        prefecture: form.prefecture,
        city: form.city,
        building: '',
        tel: form.tel,
      };
      await store.createAddress(address)
        .then(() => {
          store.loadAddresses();
          resetForm();
          context.emit("close");
        })
        .catch((e) => {
          compstate.resErrors = e.response.data.errors
        })
        .finally(() => {
          compstate.isProcessing = false;
        })
    });

    watch(
      () => values.postal_code,
      (val) => {
        new YubinBango.Core(val, function(addr) {
          values.prefecture = addr.region;
          values.city = addr.locality + addr.street + addr.extended;
        });
      },
      { deep: true }
    )

    return {
      hasNoError,
      state: compstate,
      cancelled,
      submit,
    }
  }
};
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

.c-form-col > .c-form-validator {
  margin-left: 10px;
}

.formErrors p {
  color: #DF5475;
  font-size: 10px;
  line-height: 16px;
}
</style>
