<template>
  <ModalWindow
    :isShow="isOpen"
    class="c-modal--white c-colorListModal"
  >
    <div
      ref="modalContent"
      class="c-colorListModal-content"
    >
      <a
        class="c-colorListModalClose"
        href="#"
        @click.prevent.stop="close"
      >
        閉じる
        <span class="c-colorListModalClose-icon">
            <svg><use xlink:href='#icons-cross'/></svg>
          </span>
      </a>

      <header class="c-colorListModalHeader">
        <h2 class="g-title-secondary">印刷に使える色</h2>
        <p>表示の色は、素材に印刷した時の着色に近い表示にしています</p>
      </header>
      <div
        v-if="cardboardColors"
        class="c-colorListModalMain"
      >
        <div
          v-for="cardboardColor in cardboardColors"
          :key="cardboardColor.name"
          class="c-colorListModalRow"
        >
          <h3 class="g-title-tertiary c-colorListModalRow-title">
            {{ cardboardColor.name }}
          </h3>
          <div
            v-if="cardboardColor.data"
            class="c-colorListModalListWrapper"
          >
            <ul class="c-colorListModalList">
              <li
                v-for="color in cardboardColor.data"
                :key="color"
                class="c-colorListModalList-item"
                :style="{
                  'background-image': `url(${color})`
                }"
              />
            </ul>
          </div>
        </div>
      </div>
    </div>
  </ModalWindow>
</template>

<script>
import ModalWindow from "../components/common/ModalWindow";
import StoreMixin from "../mixins/StoreMixin";

export default {
  name: "ColorListModal",
  mixins: [StoreMixin],
  components: {ModalWindow},
  computed: {
    cardboardColors() {
      return this.state.cardboardColors;
    },
    isOpen() {
      return this.state.isOpen;
    }
  },
  methods: {
    close() {
      this.store.closeModal();
    }
  },
  mounted() {
    this.store.fetchColors();

    document.addEventListener("click", e => {
      const target = (e.target || e.srcElement).closest(".p-draftModal");
      if (!this.isShow || target === this.$refs.modalContent) return;

      this.close();
    });
  }
}
</script>

<style scoped>

</style>
