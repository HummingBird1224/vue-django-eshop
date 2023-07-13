<template>
  <div class="p-externalFujiLogiProducts-wrappedNavi-item" @click.prevent.stop="scrollTo">
    <div class="p-externalFujiLogiProducts-wrappedNavi-item-image">
      <img
        :src="`${staticUrl}${item.imgUrl}`"
        :alt="item.name"
      >
    </div>
    <div class="p-externalFujiLogiProducts-wrappedNavi-item-text">
      <h4 class="g-title-quaternary">{{ item.name }}</h4>
    </div>
  </div>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin";

export default {
  name: "NavigationItem",
  mixins: [StoreMixin],
  props: {
    item: {
      type: Object,
      required: true
    }
  },
  computed: {
    staticUrl() {
      return this.state.staticUrl;
    }
  },
  methods: {
    scrollTo() {
      this.$smoothScroll({
        scrollTo: document.getElementById(this.item.scrollToId),
        duration: 400,
     })
    }
  }
}
</script>

<style>

</style>
