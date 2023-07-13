<template>
  <div class="p-billingFooter">
    <a class="c-textLink" href="/accounts/login/?next=/billing/">すでにアカウントをお持ちの方はログイン</a>
    <a
      class="c-btn c-btn--primary"
      :class="{
        'is-disabled': !valid,
        'is-loading': isProcessing
      }"
      href="#"
      @click.prevent.stop="submit"
    >
      配送先の入力へ
    </a>
  </div>
</template>

<script>
export default {
  name: "LoginFooter",
  emits: ['submit'],
  props: {
    valid: {
      type: Boolean,
      default: false
    },
    isProcessing: {
      type: Boolean,
      default: false
    }
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
