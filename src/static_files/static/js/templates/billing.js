import { configure, defineRule } from 'vee-validate';
import { localize } from '@vee-validate/i18n/vee-validate-i18n';
import { required } from '@vee-validate/rules';
import ja from '@vee-validate/i18n/locale/ja.json';
import App from '../vues/pages/BillingForm.vue';
import Store from '../vues/stores/billingForm';
import { vueMount } from '../helpers/vueMount';

const element = $('#js-billing-form')
element.ready(() => {
  if (element.length) {
   defineRule('required', required);
   configure({
      generateMessage: localize({
        ja: {
          messages: ja.messages,
          names: {
            "name": "お名前",
            "last_name": "姓",
            "first_name": "名",
            "postal_code": "郵便番号",
            "prefecture": "都道府県",
            "city": "市区町村・番地",
            "building": "建物",
            "tel": "電話番号",
            "billing_postal_code": "郵便番号",
            "billing_prefecture": "都道府県",
            "billing_city": "市区町村・番地",
            "billing_building": "建物",
            "billing_tel": "電話番号",
            "card[number]": "クレジット番号",
            "card[exp_year]": "年",
            "card[exp_month]": "月",
            "card[cvc]": "セキュリティコード"
          }
        }
      })
    });

    localize('ja');
    vueMount(App, Store, element);
  }
});
