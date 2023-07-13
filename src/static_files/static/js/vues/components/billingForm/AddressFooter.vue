<template>
  <div class="p-billingFooter">
    <div class="p-billingFooter-right">
      <img :src="`${staticUrl}img/credit_card.jpg`"/>
      <p>次にクレジットカードの入力に進みます</p>
    </div>
    <a
      type="submit"
      class="c-btn c-btn--primary"
      :class="{
        'is-disabled': !valid,
        'is-loading': isProcessing
      }"
      href="#"
      @click.prevent.stop="submit"
    >
      確認画面へ
    </a>
  </div>
</template>
<script>
import StoreMixin from "../../mixins/StoreMixin";

export default {
  name: "AddressFooter",
  mixins: [StoreMixin],
  computed: {
    staticUrl() {
      return this.state.staticUrl;
    },
  },
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
