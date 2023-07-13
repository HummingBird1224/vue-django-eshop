<template>
  <div
    class="c-form-validator"
    :name="name"
    :rules="rules"
  >
    <div
      class="c-form-item"
      :class="{
        'is-error': true
      }"
    >
      <Field as="div" :name="name" class="c-form-select"  v-slot="{ field }">
        <select
          class="c-form-selectInput"
          :class="{
            'c-form-selectInput--hasLabel': isShowLabel
          }"
          v-html="optionsHTML"
          v-bind="field"
        >
        </select>
        <label
          v-if="isShowLabel"
          class="c-form-label"
        >{{ label }}</label>
        <svg class='c-form-selectIcon'>
          <use xlink:href='#icons-arrow_down'/>
        </svg>
      </Field>
      <p v-if="comment" class="c-form-comment">{{ comment }}</p>
      <p class="c-form-error">
        <ErrorMessage :name="name" />
      </p>
    </div>
  </div>
</template>

<script>
import { Field, ErrorMessage } from 'vee-validate';

export default {
  name: "SelectInput",
  components: { Field, ErrorMessage },
  props: {
    name: [String],
    label: [String],
    rules: [String],
    value: null,
    comment: [String],
    isShowLabel: [Boolean],
    placeholder: [String],
    hasBlankPlaceholder: [Boolean],
    options: [Array],
  },
  emits: ['input'],
  computed: {
    optionsHTML() {
      let optionsHTML = '';

      if (this.hasBlankPlaceholder) {
        optionsHTML += `<option value=""></option>`;
      } else if (this.placeholder) {
        optionsHTML += `<option value="">${this.placeholder}</option>`;
      }

      return optionsHTML +
        this.options.map(x => `<option value="${x}">${x}</option>`).join('');
    }
  }
}
</script>

<style scoped>

</style>
