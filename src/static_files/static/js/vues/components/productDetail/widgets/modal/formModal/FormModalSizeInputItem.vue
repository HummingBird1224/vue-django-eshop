<template>
  <div
    class="p-sizeForm-colWrapper"
    :class="{
      'is-error': !!error
    }"
  >
    <div class="c-form-item p-sizeForm-col">
      <input
        type="number"
        class="c-form-input p-sizeForm-input"
        :value="modelValue"
        @input="updateValue"
        @blur="blurOriginalSizeInput"
      />
      <label class="c-form-label p-sizeForm-label">{{ jaName }}</label>
      <span class="p-sizeForm-unit">mm</span>
    </div>
    <span
      v-if="error && error.hasBlur"
      class="p-sizeForm-error"
    >{{ error.msg }}</span>
  </div>
</template>

<script>
import toSizeJpName from "../../../../../../helpers/toSizeJpName";
import { computed, } from 'vue';

export default {
  name: "FormModalSizeInputItem",
  props: {
    name: {
      type: String,
      required: true,
    },
    error: {
      type: Object
    },
    modelValue: {
      type: String
    }
  },
  emits: ['input', 'blurOriginalSizeInput', 'update:modelValue'],
  setup(props, context) {
    const jaName = computed(()=>toSizeJpName(props.name))
    const blurOriginalSizeInput = () => {
      context.emit('blurOriginalSizeInput', props.name);
    }
    const updateValue = (e) => {
      context.emit('update:modelValue', e.target.value)
      blurOriginalSizeInput();
    }

    return {
      jaName,
      blurOriginalSizeInput,
      updateValue
    }
  }
}
</script>

<style scoped>

</style>
