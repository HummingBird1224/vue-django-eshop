<template>
  <div>
    <form>
      <div class="p-billingContent">
        <h2 class="g-title-secondary p-billingContent-title">配送先の情報を入力</h2>
        <p class="p-billingContent-description">
          <svg class="p-billingContent-icon--pin">
            <use xlink:href='#icons-pin_drop_lg'/>
          </svg>
          <span>どこにお届けしますか？</span>
        </p>

        <div class="c-form-col">
          <TextInput
            name="name"
            label="お名前"
            rules="required"
          />
        </div>

        <div class="c-form-col c-form-col--half">
          <TextInput
            name="postal_code"
            label="〒郵便番号"
            rules="required"
          />

          <SelectInput
            name="prefecture"
            label="都道府県"
            rules="required"
            placeholder="都道府県"
            :options="prefectures"
          />
        </div>
        <small>※現在、北海道、沖縄への配送は対応しておりません。</small>
        <div class="c-form-col">
          <TextInput
            name="city"
            label="市区町村・番地・建物"
            rules="required"
          />
        </div>

        <div class="c-form-col c-form-col--half">
          <TextInput
            name="tel"
            label="電話番号"
            rules="required"
          />
        </div>

        <div class="c-form-col c-form-col--bottom">
          <div class="c-form-item">
            <label class="c-form-checkbox">
              <input
                class="c-form-checkboxInput"
                type="checkbox"
                v-model="state.isInputBillingAddress"
              >
              <span class="c-form-checkboxMark"><i class="material-icons">done</i></span>
              請求先を別の住所にする
            </label>
          </div>
        </div>

        <template
          v-if="state.isInputBillingAddress"
        >
          <div class="c-form-col c-form-col--half c-form-col--bottom">
            <TextInput
              name="billing_postal_code"
              label="〒郵便番号"
              rules="required"
            />
            <SelectInput
              name="billing_prefecture"
              label="都道府県"
              rules="required"
              placeholder="都道府県"
              :options="prefectures"
            />
          </div>

          <div class="c-form-col">
            <TextInput
              name="billing_city"
              label="市区町村・番地・建物"
              rules="required"
            />
          </div>

          <div class="c-form-col c-form-col--half">
            <TextInput
              name="billing_tel"
              label="電話番号"
              rules="required"
            />
          </div>
        </template>
      </div>
      <AddressFooter
        :valid="hasNoError"
        :isProcessing="state.isProcessing"
        @submit="submit"
      />
      <ErrorMessage></ErrorMessage>
    </form>
  </div>
</template>

<script>
import AddressFooter from "./AddressFooter";
import BillingFlow from "../../../constants/BillingFlow";
import { PREFECTURES } from '../../../constants/Prefectures';
import TextInput from "../common/TextInput";
import SelectInput from "../common/SelectInput";
import { Form } from "vee-validate";
import { useStore } from "../../providers/useStore";
import { useFormValidation } from "../../providers/formValidation";
import { reactive, watch, ref} from "vue";
import { useForm, ErrorMessage } from "vee-validate";


export default {
  name: "AddressPage",
  components: { Form, SelectInput, TextInput, AddressFooter, ErrorMessage},
  setup(props, context) {

    // datas
    const compState = reactive({
      isProcessing: false,
      isInputBillingAddress: false,
      errors: [],
    });
    const prefectures = ref(PREFECTURES);
    const { store } = useStore();
    const { values, errors, setErrors, handleSubmit } = useForm();
    const { hasNoError } = useFormValidation(errors, values, 0);
    const submit = handleSubmit(async (values) => {
      if (compState.isProcessing) {
        return;
      }

      compState.isProcessing = true;
      const { city, name, postal_code, prefecture, tel } = values;

      const deliveryFormValue = {
        name,
        postal_code,
        city,
        prefecture,
        tel,
        use_as_billing_address: !compState.isInputBillingAddress
      }

      try {
        await store.postDeliveryAddress(deliveryFormValue)

      } catch (e) {

        compState.isProcessing = false;
        const errors = e.response.data.errors;
        setErrors(errors)
        throw e
      }


      if (!compState.isInputBillingAddress) {
        compState.isProcessing = false;
        store.setFlow(BillingFlow.PAYMENT)
        return
      }

      try {
        const { billing_city, billing_postal_code, billing_prefecture, billing_tel } = values;
        const billingFormValue = {
          name,
          postal_code: billing_postal_code,
          city: billing_city,
          prefecture: billing_prefecture,
          tel: billing_tel,
        }
        await store.postBillingAddress(billingFormValue)
      } catch (e) {
        let billingErrors = {};
        for (const [key, value] of Object.entries(e.response.data.errors)) {
          billingErrors = {
            ...billingErrors,
            ...{ ["billing_" + key] : value }
          }
        }
        setErrors(billingErrors)
        throw e
      } finally {
        compState.isProcessing = false;
      }

      store.setFlow(BillingFlow.PAYMENT)
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


    watch(
      () => values.billing_postal_code,
      (val) => {
        new YubinBango.Core(val, function(addr) {
          values.billing_prefecture = addr.region;
          values.billing_city = addr.locality + addr.street + addr.extended;
        });
      },
      { deep: true }
    )

    return {
      state: compState,
      hasNoError,
      prefectures,
      submit
    }
  }
}
</script>

<style scoped>
</style>
