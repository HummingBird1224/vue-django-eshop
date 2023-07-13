<template>
  <ModalWindow
    :isShow="isShow"
  >
    <div
      class="p-orderAlert p-orderAlert--ok"
      ref="modalContent"
    >
      <svg class="p-orderAlertIcon">
        <use xlink:href='#icons-check'/>
      </svg>
      <h2 class="g-title-secondary p-orderAlertTitle">入稿が完了しました</h2>
      <p class="p-orderAlertBody">
        データを確認して、最終確認のご連絡までお待ち下さい。
      </p>
      <p class="p-orderAlertBody">
        確認に数週間かかる場合もございます。
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
  name: "OrdersUploadedModal",
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
