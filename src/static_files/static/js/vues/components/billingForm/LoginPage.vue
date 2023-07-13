<template>
  <div>
    <form>
      <div class="p-billingContent">
        <h2 class="g-title-secondary p-billingContent-title">canalへようこそ！👋</h2>

        <div class="p-billingContent-externalService">
          <p class="p-billingContent-externalService-header">外部情報を使ってアカウント作成</p>
          <div class="p-billingContent-externalService-buttons">
            <a class="p-billingContent-externalService-button p-billingContent-externalService-button--base" :href="baseUrl">
              <div class="">
                <img :src="staticUrl + 'img/partners/base_new.png'">
              </div>
              <p>で作成</p>
            </a>
            <a class="p-billingContent-externalService-button p-billingContent-externalService-button--colorme" :href="colorMeUrl">
              <div class="">
                <img :src="staticUrl + 'img/partners/colorme_sm.png'">
              </div>
              <p>カラーミーで作成</p>
            </a>
          </div>
        </div>

        <p class="p-billingContent-divider">or メールアドレスを使って作成</p>

        <div class="c-form-col">
          <TextInput
            name="email"
            label="メールアドレス"
            rules="required"
          />
        </div>

        <div class="c-form-col">
          <TextInput
            name="name"
            label="氏名"
            rules="required"
          />
        </div>

        <div class="c-form-col">
          <TextInput
            name="company_name"
            label="会社名(任意)"
          />
        </div>

        <div class="c-form-col">
          <TextInput
            name="url"
            label="ホームページURL(任意)"
          />
        </div>

        <div class="c-form-col">
          <PasswordInput
            name="password1"
            label="パスワード"
          />
        </div>

        <div class="c-form-col">
          <PasswordInput
            name="password2"
            label="パスワード（確認）"
          />
        </div>

        <div class="c-form-col c-form-col--bottom">
          <div class="c-form-item">
            <label class="c-form-checkbox">
              <input
                name="利用規約"
                type="checkbox"
                class="c-form-checkboxInput"
                v-model="kiyaku"
              >
              <span class="c-form-checkboxMark"><i class="material-icons">done</i></span>
              <a href="/privacypolicy/">プライバシーポリシー</a>と<a href="/terms/">利用規約</a>に同意する
            </label>
            <p v-if="errorMessage" class="c-form-error">同意が必要です</p>
          </div>
        </div>
      </div>
      <ErrorMessage></ErrorMessage>
      <LoginFooter
        :valid="hasNoError"
        :isProcessing="state.isProcessing"
        @submit="submit"
      />
    </form>
  </div>
</template>

<script>
import LoginFooter from "./LoginFooter";
import TextInput from "../common/TextInput";
import PasswordInput from "../common/PasswordInput";
import { useStore } from "../../providers/useStore";
import { useFormValidation } from '../../providers/formValidation'
import { useForm, useField, Field, ErrorMessage } from "vee-validate"
import { reactive, computed } from "vue";

export default {
  name: "LoginPage",
  components: { PasswordInput, TextInput, LoginFooter, Field, ErrorMessage },
  setup() {

    // datas
    const compState = reactive({
      isProcessing: false
    })

    // providers
    const { store, state } = useStore();
    const { values, errors, handleSubmit, setErrors } = useForm();
    const { errorMessage, value: kiyaku } = useField("利用規約", inputValue => !!inputValue && inputValue == true);

    const { hasNoError } = useFormValidation(errors, values, 2);// Optionalなフォームは2こ

    // computed
    const orderInfo = computed(()=> state.orderInfo);
    const staticUrl = computed(()=> state.staticUrl);
    const colorMeUrl= computed(()=> state.colorMeUrl);
    const baseUrl   = computed(()=> state.baseUrl);

    const submit = handleSubmit(async (values)=>{
      const { email, name, company_name, url, password1, password2, "利用規約": is_confirmed } = values;

      const currentUrl = new URL(window.location.href);
      const params = currentUrl.searchParams;
      const oid = params.get("oid");

      const formValue = {
        email,
        name,
        company_name,
        url,
        password1,
        password2,
        oid,
        is_confirmed
      }
      try {
        compState.isProcessing = true;
        await store.postUserSignUp(formValue)
        await location.reload()
      } catch (e) {
        let erros = e.response.data.errors;
        setErrors(erros)
        throw e
      } finally {
        compState.isProcessing = false;
      }

    });

    return {
      hasNoError,
      state: compState,
      orderInfo,
      staticUrl,
      colorMeUrl,
      baseUrl,
      submit,
      kiyaku,
      errorMessage,
    }
  }
}
</script>

<style scoped>

</style>
