<template>
  <li class="p-CartItem">
    <div
      class="p-CartItemThumb"
      :style="thumbStyle"
    ></div>
    <div class="p-CartItemBody">
      <header class="p-CartItemBody-header">
        <h4 class="g-title-quaternary"><a :href="item.url">{{ item.product_name }}</a></h4>
        <p>{{ $filters.toPriceFormat(item.total) }}<span>円</span></p>
      </header>
      <div class="p-CartItemBody-content">
        <div
          class="p-CartItemBody-detail"
          v-for="info in item.extra"
        >
          <h5 class="g-title-quinary">{{ info.label }}</h5>
          <p>{{ info.value }}</p>
        </div>
      </div>
    </div>
  </li>
</template>

<script>
export default {
  name: "CartListItem",
  props: {
    item: {
      type: Object,
      required: true,
    }
  },
  computed: {
    thumbStyle() {
      const style = {};

      if (this.item.thumbnail) {
        style['background-image'] = `url(${this.item.thumbnail})`;
      }

      return style;
    }
  }
}
</script>

<style scoped>

</style>
