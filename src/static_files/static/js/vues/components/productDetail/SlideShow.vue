<template>
  <div class="p-slideshow">
    <swiper
      class="p-slideshow-images"
      :slides-per-view="3"
      :options="swiperOption"
      ref="mySwiper"
      @transitionStart="updateSwiperState"
      @swiper="onSwiper"
      @slideChange="onSlideChange"
    >
      <swiper-slide
        v-for="(image, index) in example_images"
        class="p-slideshow-image"
        :key="image + index"
        :data-idx="index"
        :style="{
          backgroundImage: `url(${image})`,
          width: '150px',
          height: '150px',
        }"
      ><a class="p-slideshow-links" :href="example_urls[index]" target="_blank"></a>
      </swiper-slide>
    </swiper>
    <a
      v-if="!isBeginning"
      class="p-slideshow-button p-slideshow-button--left"
      href="#"
      @click.prevent.stop="slidePrev"
    >
      <svg>
        <use xlink:href='#icons-arrow_down'></use>
      </svg>
    </a>
    <a
      v-if="!isEnd"
      class="p-slideshow-button p-slideshow-button--right"
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
  name: "SlideShow",
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
    example_images: {
      type: Array,
      required: true
    },
    example_urls: {
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
