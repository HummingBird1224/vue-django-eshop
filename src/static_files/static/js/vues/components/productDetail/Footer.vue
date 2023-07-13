<template>
  <footer class="p-ProductFooter">
    <PriceInfo/>
    <a
      class="p-ProductFooter-submit"
      :class="{
        'is-disabled': !canSubmit,
        'is-loading': isSubmitting,
      }"
      @click.prevent.stop="submit"
      href="#"
    >購入へ</a>
  </footer>
</template>

<script>
import PriceInfo from "./PriceInfo";
import { useStore } from "../../providers/useStore";
import { computed } from 'vue';

export default {
  name: "Footer",
  components: { PriceInfo },
  props: {
    canSubmit: {
      type: Boolean,
    }
  },
  setup(props, context) {
    const { canSubmit } = props;
    const { store, state } = useStore();
    const isSubmitting = computed(()=>state.isSubmitting)
    const submit = () => store.postAddCart().then(()=>location.href='/cart/')
    return {
      canSubmit,
      isSubmitting,
      submit
    }
  }
}
</script>

<style scoped>

</style>
