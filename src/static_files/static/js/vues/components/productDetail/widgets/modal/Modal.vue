<template>
  <ModalWindow
    class="p-Modal"
    :isShow="isOpen"
  >
    <div
      class="c-modal-content p-Modal-content"
      ref="modalContent"
    >
      <slot/>
    </div>
  </ModalWindow>
</template>

<script>
import ModalWindow from "../../../common/ModalWindow";

export default {
  name: "Modal",
  components: {ModalWindow},
  props: {
    isOpen: {
      type: Boolean
    }
  },
  emits: ['close'],
  methods: {
    close() {
      this.$emit('close');
    }
  },
  mounted() {
    document.addEventListener("click", e => {
      const target = (e.target || e.srcElement).closest(".p-Modal-content");
      if (!this.isOpen || target === this.$refs.modalContent) return;

      this.close();
    });
  }
}
</script>

<style scoped>

</style>
