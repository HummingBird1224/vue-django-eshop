<template>
  <div class="p-product-formRight-form">
    <div id="form-selects">
      <h3 class="p-product-formRight-header">
        <svg width="16" height="14" viewBox="0 0 16 14" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M11.4734 5.57667H14.6667C15.0334 5.57667 15.3334 5.87667 15.3334 6.24334L15.3134 6.42334L13.6201 12.6033C13.4601 13.1633 12.9467 13.5767 12.3334 13.5767H3.66675C3.05342 13.5767 2.54008 13.1633 2.38675 12.6033L0.693415 6.42334C0.673415 6.36334 0.666748 6.30334 0.666748 6.24334C0.666748 5.87667 0.966748 5.57667 1.33341 5.57667H4.52675L7.44675 1.21001C7.57342 1.01667 7.78675 0.92334 8.00008 0.92334C8.21342 0.92334 8.42675 1.01667 8.55342 1.20334L11.4734 5.57667ZM9.86663 5.57673L7.99997 2.77673L6.1333 5.57673H9.86663ZM12.3334 12.2433L3.67336 12.25L2.2067 6.90997H13.8L12.3334 12.2433ZM6.66669 9.57668C6.66669 8.84335 7.26669 8.24335 8.00002 8.24335C8.73335 8.24335 9.33335 8.84335 9.33335 9.57668C9.33335 10.31 8.73335 10.91 8.00002 10.91C7.26669 10.91 6.66669 10.31 6.66669 9.57668Z" fill="#205EFB"/>
        </svg>
        見積もり＆購入
      </h3>
      <div class="p-ProductForm">
        <template
          v-for="(option, index) in options"
        >
          <VerticalSelect
            v-if="option.widget_type === 'slider-lg' || option.widget_type === 'slider-sm'"
            :id="`form-select${index}`"
            :key="index"
            :optionIndex="index"
            isActive
            @form-updated="estimate"
          />
          <HorizontalSelect
            v-if="option.widget_type === 'radio'"
            :id="`form-select${index}`"
            :key="index"
            :optionIndex="index"
            isActive
            @form-updated="estimate"
          />
          <ModalSelect
            v-if="option.widget_type === 'modal-radio' || option.widget_type === 'modal-check' || !option.hasOwnProperty('widget_type')"
            :id="`form-select${index}`"
            :key="index"
            :optionIndex="index"
            isActive
            @form-updated="estimate"
          />
        </template>
      </div>
    </div>
    <Footer
      canSubmit
      id="form-submit-btn"
    />
  </div>
</template>

<script>
import Footer from "./Footer";
import VerticalSelect from "./widgets/VerticalSelect";
import HorizontalSelect from "./widgets/HorizontalSelect";
import ModalSelect from "./widgets/ModalSelect";
import isObject from "../../../helpers/isObject";

import { computed, watch, provide, onUpdated } from 'vue';
import { useStore } from '../../providers/useStore';

export default {
  name: "ProductForm",
  components: {ModalSelect, HorizontalSelect, VerticalSelect, Footer},
  setup() {
    const { store, state } = useStore();
    const product = computed(() => state.product)
    provide('product_options', state.product.options)
    const form = computed(()=> state.form)

    const options = computed(() => {
      return state.product.options.sort((a, b) => a.position - b.position)
    })
    const optionsKey = computed(()=>state.product.options.map(x=>x.slug))
    const estimate = ()=>{
      const canEstimate = (()=> {
        let estimatable = true;
        optionsKey.value.forEach(x => {
          if (x === 'quantity') {
            return;
          }

          const formValue = form.value[x];
          if (formValue === null || formValue == undefined) {
            estimatable = false;
          } else if (isObject(formValue) && Object .values(formValue).filter(y => y === null).length) {
            estimatable = false;
          }

        })
        return estimatable;
      })();
      if (canEstimate) {
        store.postEstimate();
      }
    }

    return {
      product,
      form,
      options,
      optionsKey,
      estimate
    }
  }
}
</script>

<style scoped>

</style>
