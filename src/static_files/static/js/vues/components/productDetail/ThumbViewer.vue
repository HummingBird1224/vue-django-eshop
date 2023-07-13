<template>
  <div>
    <LargeImageModal
      :isShow="isOpenModal"
      :initImgIdx="currentImgIdx"
      :images="images"
      @close="closeModal"
    />
    <div class="p-ProductThumbViewer">
      <ul class="p-ProductThumbList">
        <li
          v-for="(img, idx) in images" :key="idx"
          class="p-ProductThumb"
          :class="{
              'is-current': idx === currentImgIdx
            }"
          :style="{
              'background-image': `url(${img})`
            }"
          @click.prevent.stop="onClickThumbListItem(idx)"
        />
      </ul>
      <div
        class="p-ProductImage"
        :style="{
            'background-image': `url(${currentImg})`
          }"
        @click.prevent.stop="openModal"
      >
      </div>
    </div>
  </div>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin";
import LargeImageModal from "./widgets/modal/LargeImageModal";

export default {
  name: "ThumbViewer",
  components: {LargeImageModal},
  mixins: [StoreMixin],
  data: () => ({
    currentImgIdx: 0,
    isOpenModal: false,
  }),
  computed: {
    product() {
      return this.state.product;
    },
    images() {
      return this.product.images;
    },
    currentImg() {
      return this.images[this.currentImgIdx];
    }
  },
  methods: {
    onClickThumbListItem(idx) {
      this.currentImgIdx = idx;
    },
    openModal() {
      this.isOpenModal = true;
    },
    closeModal() {
      this.isOpenModal = false;
    }
  },
  mounted() {
  }
}
</script>

<style scoped>

</style>
