<template>
  <div class="p-billingFooter">
    <p><span v-if="isUseDefaultCard">ボタンを押すとご注文が確定されます</span></p>
    <a
      class="c-btn c-btn--primary"
      :class="{
        'is-loading': isProcessing
      }"
      href="#"
      @click.prevent.stop="submit"
    >
      <span v-if="isUseDefaultCard">注文を確定する</span>
      <span v-if="!isUseDefaultCard">カードを確定する</span>
    </a>
  </div>
</template>

<script>
export default {
  name: "PaymentFooter",
  emits: ['submit'],
  props: {
    valid: {
      type: Boolean,
      default: false
    },
    isProcessing: {
      type: Boolean,
      default: false
    },
    isUseDefaultCard: {
      type: Boolean,
      default: false
    },
  },
  methods: {
    submit() {
      this.$emit('submit');
    }
  }
}
</script>

<style scoped>

</style>
