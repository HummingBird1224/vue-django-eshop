<template>
  <div class="p-slider">
    <swiper
      class="p-slider-images"
      :slides-per-view="3"
      :options="swiperOption"
      ref="mySwiper"
      @transitionStart="updateSwiperState"
      @swiper="onSwiper"
      @slideChange="onSlideChange"
    >
      <swiper-slide
        v-for="(image, index) in images"
        class="p-slider-image"
        :key="image + index"
        :data-idx="index"
        :style="{
          backgroundImage: `url(${image})`,
          width: '318px',
          height: '318px',
        }"
      >
      </swiper-slide>
    </swiper>
    <a
      v-if="!isBeginning"
      class="p-slider-button p-slider-button--left"
      href="#"
      @click.prevent.stop="slidePrev"
    >
      <svg>
        <use xlink:href='#icons-arrow_down'></use>
      </svg>
    </a>
    <a
      v-if="!isEnd"
      class="p-slider-button p-slider-button--right"
      href="#"
      @click.prevent.stop="slideNext"
    >
      <svg>
        <use xlink:href='#icons-arrow_down'></use>
      </svg>
    </a>
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from 'swiper/vue';
export default {
  name: "Slider",
  components: { Swiper, SwiperSlide },
  data: () => ({
    isBeginning: true,
    isEnd: false,
    swiperOption: {
      slidesPerView: 'auto',
      preventClicks: false,
      preventClicksPropagation: false,
      touchStartPreventDefault: false
    },
    mySwiper: null,
  }),
  props: {
    images: {
      type: Array,
      required: true
    }
  },
  methods: {
    onSwiper(swiper) {
      this.isBeginning = swiper.isBeginning;
      this.isEnd = swiper.isEnd;
      this.mySwiper = swiper;
    },
    onSlideChange() {
      console.log('slide change');
    },
    updateSwiperState() {
      this.isBeginning = this.mySwiper.isBeginning;
      this.isEnd = this.mySwiper.isEnd;
    },
    slideNext() {
      this.mySwiper.slideNext();
    },
    slidePrev() {
      this.mySwiper.slidePrev();
    },
  },
  mounted() {
    this.updateSwiperState();
  }
}
</script>

<style>

</style>
