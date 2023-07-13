<template>
  <div class="p-externalFutureShopProducts-product-content-purchase-footer-prices">
    <h5 class="g-title-quinary"><span>合計 </span>{{ $filters.toPriceFormat(totalPrice) }}<span>円（税込） <span>{{ unitPrice }}</span>円/個</span></h5>
    <ul
      v-if="price"
    >
      (
      <li
        v-if="productTotalPrice"
      >商品　<span>{{ $filters.toPriceFormat(productTotalPrice) }}</span>円</li>
      <li
        v-if="platePrice"
      >版代　<span>{{ $filters.toPriceFormat(platePrice) }}</span>円</li>
      <li
        v-if="moldPrice"
      >木型代　<span>{{ $filters.toPriceFormat(moldPrice) }}</span>円</li>
      <li
        v-if="shippingPrice"
      >配送料　<span>{{ $filters.toPriceFormat(shippingPrice) }}</span>円</li>
      <li
        v-if="taxPrice"
      >消費税　<span>{{ $filters.toPriceFormat(taxPrice) }}</span>円</li>
      )
    </ul>
  </div>
</template>

<script>
export default {
  name: "PriceInfo",
  props: {
    price: {
      type: Object,
    }
  },
  computed: {
    totalPrice() {
      if (this.price && this.price.hasOwnProperty('total')) {
        return this.price.total;
      }

      return '-';
    },
    unitPrice() {
      if (this.price && this.price.hasOwnProperty('unit_price')) {
        return this.price.unit_price;
      }

      return '-';
    },
    platePrice() {
      if (this.price && this.price.hasOwnProperty('plate_price')) {
        return this.price.plate_price;
      }

      return null;
    },
    moldPrice() {
      if (this.price && this.price.hasOwnProperty('mold_price')) {
        return this.price.mold_price;
      }

      return null;
    },
    shippingPrice() {
      if (this.price && this.price.hasOwnProperty('shipping_price')) {
        return this.price.shipping_price;
      }

      return null;
    },
    productTotalPrice() {
      if (this.price && this.price.hasOwnProperty('product_total')) {
        return this.price.product_total;
      }

      return null;
    },
    taxPrice() {
      if (this.price && this.price.hasOwnProperty('tax')) {
        return this.price.tax;
      }

      return null;
    },
    subtotalPrice() {
      if (this.price && this.price.hasOwnProperty('subtotal')) {
        return this.price.subtotal;
      }

      return null;
    }
  }
}
</script>

<style>

</style>
