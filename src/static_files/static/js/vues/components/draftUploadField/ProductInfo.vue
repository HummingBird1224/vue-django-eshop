<template>
  <div
    class="p-Product"
    v-if="orderInfo"
  >
    <div
      class="p-ProductThumb"
      :style="thumbStyle"
    ></div>
    <div class="p-ProductInfo">
      <h5 class="g-title-quinary">{{ orderInfo.product_name }}</h5>

      <div class="p-ProductDetail__column">
        <div class="p-ProductDetail-column">
          <h6 class="g-title-quinary">サイズ</h6>
          <p>{{ sizeStr }}</p>
        </div>
        <div class="p-ProductDetail-column">
          <h6 class="g-title-quinary">デザイン</h6>
          <p v-if="orderInfo.extra_info.color_num < 0">フルカラー</p>
          <p v-else>{{ orderInfo.extra_info.color_num }}色</p>
        </div>
        <div class="p-ProductDetail-column">
          <h6 class="g-title-quinary">出荷予定日</h6>
          <p>確定次第ご連絡します</p>
        </div>
        <div class="p-ProductDetail-column">
          <h6 class="g-title-quinary">ロット数</h6>
          <p>{{ $filters.toPriceFormat(orderInfo.quantity) }}個</p>
        </div>
        <div class="p-ProductDetail-column">
          <h6 class="g-title-quinary">注文商品番号</h6>
          <p>{{ orderInfo.ref_code }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin";

export default {
  name: "ProductInfo",
  mixins: [StoreMixin],
  computed: {
    orderInfo() {
      return this.state.orderInfo;
    },
    sizeStr() {
      if (!this.orderInfo) {
        return '';
      }
      const { depth, height, width } = this.orderInfo.extra_info.size;

      let size = `${width}cm×${height}cm`;

      if (depth) {
        size = size +  `×${depth}cm`;
      }
      return size;
    },
    thumbStyle() {
      const style = {};

      if (this.orderInfo && this.orderInfo.thumbnail) {
        style['background-image'] = `url(${this.orderInfo.thumbnail})`;
      }

      return style;
    }
  }
}
</script>

<style scoped>
</style>
