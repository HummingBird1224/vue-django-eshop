<template>
  <ModalWindow
    class="p-imageModal"
    :isShow="isShow"
  >
    <div class="p-imageModal-content">
      <a
        class="p-imageModal-close"
        href="#"
        @click.prevent.stop="close"
      >
        <svg>
          <use xlink:href='#icons-cross'/>
        </svg>
        閉じる</a>
      <div
        ref="modalContent"
        class="p-imageModal-wrapper"
      >
        <a
          v-if="isShowPrevButton"
          class="p-imageModal-button p-imageModal-button--left"
          href="#"
          @click.prevent.stop="slidePrev"
        >
          <svg>
            <use xlink:href='#icons-arrow_down'></use>
          </svg>
        </a>
        <img
          v-if="currentImg"
          :src="currentImg"
          alt=""
        >
        <a
          v-if="isShowNextButton"
          class="p-imageModal-button p-imageModal-button--right"
          href="#"
          @click.prevent.stop="slideNext"
        >
          <svg>
            <use xlink:href='#icons-arrow_down'></use>
          </svg>
        </a>
      </div>
    </div>
  </ModalWindow>
</template>

<script>
import ModalWindow from "../../../common/ModalWindow";

export default {
  name: "LargeImageModal",
  components: {ModalWindow},
  data: () => ({
    currentImgIdx: 0,
  }),
  emits: ['close'],
  props: {
    isShow: {
      type: Boolean,
    },
    initImgIdx: {
      type: Number,
      required: true,
    },
    images: {
      type: Array,
      required: true,
    }
  },
  computed: {
    currentImg() {
      return this.images[this.currentImgIdx];
    },
    isShowNextButton() {
      return this.currentImgIdx !== this.images.length - 1;
    },
    isShowPrevButton() {
      return this.currentImgIdx !== 0;
    },
  },
  watch: {
    isShow(val) {
      if (val) {
        this.currentImgIdx = this.initImgIdx;
      }
    }
  },
  methods: {
    close() {
      this.$emit('close');
    },
    slidePrev() {
      if (this.currentImgIdx === 0) {
        return;
      }

      this.currentImgIdx -= 1;
    },
    slideNext() {
      if (this.currentImgIdx >= this.images.length - 1) {
        return;
      }

      this.currentImgIdx += 1;
    }
  },
  mounted() {
    document.addEventListener("click", e => {
      const target = (e.target || e.srcElement).closest(".p-imageModal-wrapper");
      if (!this.isShow || target === this.$refs.modalContent) return;
      this.close();
    });
  }
}
</script>

<style scoped>
</style>
