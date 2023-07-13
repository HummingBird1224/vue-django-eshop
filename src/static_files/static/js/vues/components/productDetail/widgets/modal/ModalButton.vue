<template>
  <li class="p-productSelect-ModalButton">
    <p
      :class="{
        'is-empty': isEmptyValue
      }"
    >{{ title }}</p>
    <a
      class="c-btn"
      href="#"
      @click.prevent.stop="openModal"
    >選択する</a>
    <FormModal
      v-if="isInitialized"
      :title="parentNameJa"
      :isOpen="isOpeningModal"
      :option="option"
      :name="name"
      :widgetType="widgetType"
      :currentSelectedOption="currentSelectedOption"
      @close="closeModal"
      @updateFormValue="updateFormValue"
    />
  </li>
</template>

<script>
import FormModal from "./formModal/FormModal";

import { useModal } from "../../../../providers/useModal";
import { useStore } from "../../../../providers/useStore";
import { useProductDetailForm } from "../../../../providers/productDetail/useProductDetailForm";
import { onMounted, onBeforeMount, ref, computed} from 'vue';

import isObject from '../../../../../helpers/isObject';

export default {
  name: "ModalButton",
  components: { FormModal },
  props: {
    parentName: {
      type: String,
      required: true
    },
    parentNameJa: {
      type: String,
      required: true
    },
    widgetType: {
      type: String,
      required: true
    },
    name: {
      type: String,
      required: true
    },
    option: {
      type: Object,
      required: true
    }
  },
  setup(props, context) {
    const isInitialized = ref(false)
    const { store } = useStore();
    const { widget_type } = props.option;
    const { name } = props;
    const { form, ownFormValue, updateFormValue: updateValue } = useProductDetailForm(store, name);

    const updateFormValue = (value) => {
      updateValue(value)
      context.emit('onUpdate');
    }

    const isEmptyValue = computed(()=> {
      const currentValue = ownFormValue.value;
      if (!currentValue) {
        return true;
      }
      
      if (isObject(currentValue)) {
        return Object.values(currentValue).every(x => x === null);
      }

      return currentValue === null;
    })

    const currentSelectedOption = computed(()=>{
      if (isEmptyValue.value) {
        return null
      }

      if  (name === 'size') {
        return store.getCurrentSelectedSizeOption();
      }

      switch (widget_type) {

        case 'modal-check':
          return ownFormValue.value;
        case 'modal-radio':
          const matchValue = Object.entries(option.options)
            .filter(x => x[1].value === ownFormValue.value);
          return matchValue.length ? matchValue[0] : null;
      }

      return null
    })

    const title = computed(()=>{
      if (isEmptyValue.value) {
        return 'ボタンから項目を選択しましょう'
      }

      if (name === 'size') {
        return store.getSizeValStr();
      }

      switch (widget_type) {

        case 'modal-check':
          return currentSelectedOption.value.length ? `${currentSelectedOption.value.length}つ` : '-'
        case 'modal-radio':
          return currentSelectedOption.value.length ? currentSelectedOption.value[1].name : '-'

      }

      return 'ボタンから項目を選択しましょう'
    })

    onMounted(()=>{
      // modal-checkだった場合、formを arrayで初期化しておく.
      if (widget_type === 'modal-check') {
        updateFormValue([]);
      }

      isInitialized.value = true;
    })

    onBeforeMount(()=>{
      // Provider分けるなどの対応をしたい
      if (name === 'size') {
        let resetVal = {};
        Object.keys(ownFormValue.value)
          .forEach(x=>{
            resetVal[x] = null;
          })
        updateFormValue(resetVal);
      } else if (widget_type === 'modal-check') {
        updateFormValue([]);
      } else if (widget_type === 'modal-radio') {
        updateFormValue(null)
      }
    })

    return {
      isInitialized,
      isEmptyValue,
      title,
      option: props.option,
      name,
      widgetType: widget_type,
      currentSelectedOption,
      updateFormValue,
      ownFormValue,
      form,
      ...useModal(),
    }
  }
}
</script>

<style scoped>

</style>
