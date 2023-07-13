<template>
  <div
    class="c-form-validator"
    :name="name"
    :rules="rules"
  >
    <Field
      as="div"
      class="c-form-item"
      :name="name"
      :class="{
        'is-error': true
      }"
      v-slot="{ field }"
    >
      <input
        type="password"
        class="c-form-input"
        v-bind="field"
      />
      <label class="c-form-label">
        {{ label }}
      </label>
    </Field>
    <p v-if="comment" class="c-form-comment">{{ comment }}</p>
    <p class="c-form-error">
      <ErrorMessage :name="name"></ErrorMessage>
    </p>
  </div>
</template>

<script>
import { Field, ErrorMessage } from 'vee-validate';

export default {
  name: "PasswordInput",
  components: { Field, ErrorMessage },
  emits: ['input'],
  props: {
    name: [String],
    label: [String],
    rules: [String],
    comment: [String],
  }
}
</script>

<style scoped>

</style>
