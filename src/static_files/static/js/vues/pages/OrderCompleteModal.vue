<template>
  <ModalWindow
    :isShow="isShow"
  >
    <div
      class="p-orderAlert p-orderAlert--delivery"
      ref="modalContent"
    >
      <svg class="p-orderAlertIcon">
        <use xlink:href='#icons-airport_shuttle'/>
      </svg>
      <h2 class="g-title-secondary p-orderAlertTitle">注文が完了しました！</h2>
      <p class="p-orderAlertBody">
        配送日が決まったらご連絡します。
      </p>
      <a
        class="c-btn"
        href="#"
        @click.prevent.stop="close"
      >
        閉じる
      </a>
    </div>
  </ModalWindow>
</template>

<script>
import ModalWindow from "../components/common/ModalWindow";

export default {
  name: "OrderCompleteModal",
  components: {ModalWindow},
  data: () => ({
    isShow: true
  }),
  methods: {
    close() {
      this.isShow = false;
    }
  },
  mounted() {
    document.addEventListener("click", e => {
      const target = (e.target || e.srcElement).closest(".p-orderAlert");
      if (!this.isShow || target === this.$refs.modalContent) return;

      this.close();
    });
  }
}
</script>

<style scoped>

</style>
