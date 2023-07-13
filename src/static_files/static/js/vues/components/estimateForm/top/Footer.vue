<template>
  <footer class="p-Footer">
    <div class="p-Footer-left">
      <h4
        v-if="product"
        class="p-Footer-title"
      >
        {{ product.name }}
      </h4>
      <p
        v-if="price"
        class="p-FooterPriceDetail"
      >
        <template>
          <span class="p-FooterPriceDetail-label">商品</span>
          <span class="p-FooterPriceDetail-value">{{ $filters.toPriceFormat(price.product_total) }}</span>
          <span class="p-FooterPriceDetail-unit">円</span>
        </template>

        <template
          v-if="price.plate_price"
        >
          <span class="p-FooterPriceDetail-increment">+</span>
          <span class="p-FooterPriceDetail-label">版代</span>
          <span class="p-FooterPriceDetail-value">{{ $filters.toPriceFormat(price.plate_price) }}</span>
          <span class="p-FooterPriceDetail-unit">円</span>
        </template>

        <template
          v-if="price.mold_price"
        >
          <span class="p-FooterPriceDetail-increment">+</span>
          <span class="p-FooterPriceDetail-label">木型代</span>
          <span class="p-FooterPriceDetail-value">{{ $filters.toPriceFormat(price.mold_price) }}</span>
          <span class="p-FooterPriceDetail-unit">円</span>
        </template>

        <template>
          <span class="p-FooterPriceDetail-increment">+</span>
          <span class="p-FooterPriceDetail-label">送料</span>
          <span
            class="p-FooterPriceDetail-value"
            style="font-size: 1.2rem"
          >キャンペーン中 送料無料</span>
        </template>
      </p>
    </div>
    <div class="p-Footer-right">
      <p
        v-if="price"
        class="p-FooterTotalPrice"
      >
        <span class="p-FooterTotalPrice-label">合計 （税込）</span>
        <span class="p-FooterTotalPrice-value">{{ $filters.toPriceFormat(price.total) }}</span>
        <span class="p-FooterTotalPrice-unit">円</span>
      </p>
      <form ref="createOrderForm" action="/billing/create-order/" method="POST">
        <input type="hidden" name="csrfmiddlewaretoken" :value="`${csrfToken}`">
        <button
          class="c-btn c-btn--primary"
          href="#"
          :class="{
            'is-loading': isProcessing
          }"
          @click.prevent.stop="addCart"
        >
          購入する
        </button>
      </form>
    </div>
  </footer>
</template>

<script>
import StoreMixin from "../../../mixins/StoreMixin";

export default {
  name: "Footer",
  mixins: [StoreMixin,],
  data: () => ({
    isProcessing: false,
  }),
  computed: {
    csrfToken() {
      return this.state.csrfToken;
    },
    product() {
      return this.state.product;
    },
    price() {
      return this.state.price;
    }
  },
  methods: {
    addCart() {
      if (this.isProcessing) {
        return;
      }

      this.isProcessing = true;

      this.store.postAddCart()
        .then(() => {
          // location.href = '/cart';
          this.$refs.createOrderForm.submit();
        })
        .finally(() => {
          this.isProcessing = false;
        });
    }
  }
}
</script>

<style scoped>

</style>
