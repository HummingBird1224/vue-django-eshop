import { ref, reactive, computed, } from 'vue';

// DetailFormステート管理を行う
export const useProductDetailForm = (store, name) => {

  const form = computed(()=> store.state.form)
  const ownFormValue = ref("")
  const updateFormValue = (value) => {
    store.state.form[name] = value;
    ownFormValue.value = value;
  }

  return { form, ownFormValue, updateFormValue }
}