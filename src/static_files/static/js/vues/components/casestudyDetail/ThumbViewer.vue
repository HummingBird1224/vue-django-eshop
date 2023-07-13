<template>
  <div>
    <LargeImageModal
      :isShow="isOpenModal"
      :initImgIdx="currentImgIdx"
      :images="images"
      @close="closeModal"
    />
    <div class="p-ProductThumbViewer">
      <div
        class="p-caseStudyImage"
        :style="{
            'background-image': `url(${currentImg})`
          }"
        @click.prevent.stop="openModal"
      >
      </div>
      <ul class="p-ProductThumbList">
        <li
          v-for="(img, idx) in images" :key="idx"
          class="p-caseStudyThumb"
          :class="{
              'is-current': idx === currentImgIdx
            }"
          :style="{
              'background-image': `url(${img})`
            }"
          @click.prevent.stop="onClickThumbListItem(idx)"
        />
      </ul>
    </div>
  </div>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin";
import LargeImageModal from "../productDetail/widgets/modal/LargeImageModal";

export default {
  name: "ThumbViewer",
  components: {LargeImageModal},
  mixins: [StoreMixin],
  data: () => ({
    currentImgIdx: 0,
    isOpenModal: false,
  }),
  computed: {
    caseStudy() {
      return this.state.caseStudy;
    },
    images() {
      return this.caseStudy.images;
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
