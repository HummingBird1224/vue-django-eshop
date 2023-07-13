<template>
  <footer class="p-Modal-footer">
    <a
      class="p-Modal-cancel c-textLink c-textLink--black"
      href="#"
      @click.prevent.stop="close"
    >キャンセル</a>
    <a
      class="p-Modal-submit"
      :class="{
        'is-disabled': !canSubmit
      }"
      href="#"
      @click.prevent.stop="submit"
    >決定する</a>
  </footer>
</template>

<script>
export default {
  name: "ModalFooter",
  props: {
    canSubmit: {
      type: Boolean
    }
  },
  emits: ['submit', 'close'],
  methods: {
    submit() {
      if (!this.canSubmit) {
        return;
      }

      this.$emit('submit');
    },
    close() {
      this.$emit('close');
    }
  }
}
</script>

<style scoped>

</style>
