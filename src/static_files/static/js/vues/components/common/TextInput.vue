<template>
<div
  class="c-form-item"
  :class="{
    'is-error': true
  }"
>
  <input
    v-if="onKeyUp"
    type="text"
    :name="name"
    class="c-form-input"
    v-bind:autocomplete="autocomplete"
    v-bind:onKeyUp="onKeyUp"
    v-model="value"
  />
  <input
    v-else
    type="text"
    :name="name"
    class="c-form-input"
    v-bind:autocomplete="autocomplete"
    v-model="value"
  />
  <label class="c-form-label">
    {{ label }}
  </label>
  <span class="c-form-error"> {{ errorMessage }} </span>
  <p v-if="comment" class="c-form-comment">{{ comment }}</p>
</div>
</template>

<script>
import { useField } from 'vee-validate';
import * as yup from 'yup';

export default {
  props: {
    name: [String],
    label: [String],
    rules: [String],
    comment: [String],
    onKeyUp: [String],
    autocomplete: [String],
    rules: String
  },
  setup(props, context) {
    const { label, comment, onKeyUp, autocomplete, name, rules } = props;
    const { errorMessage, value } = useField(name, rules === 'required' ? yup.string().required().label(label) : {});
    return {
      label,
      comment,
      onKeyUp,
      autocomplete,
      value,
      errorMessage,
    };
  },
};
</script>

<style scoped>
.error-text {
  color: red;
}
</style>
