import { computed } from 'vue';

// use for vee-validate
export const useFormValidation = (errors ,values, optionalKeyCounts = 0) => {

  const checkErrors = (errors, values) => {
    const hasNoError = Object.keys(errors.value).length == 0;
    const inputedKeys =  Object.keys(values).filter(e=>e!=null).length;
    const inputedValues = Object.values(values).filter(e=>e!=null).length;
    return hasNoError &&
     inputedKeys > 0 &&
     inputedValues > 0 &&
     (inputedKeys - inputedValues) <= optionalKeyCounts
  }

  const hasNoError = computed(()=> checkErrors(errors, values))

  return { checkErrors, hasNoError }
}
