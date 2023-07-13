<template>
  <div class="p-externalBaseProducts-product" :id="product.slug">
    <div class="p-externalBaseProducts-product-wrapper">
      <Slider
        :images="product.images"
      />

      <div class="p-externalBaseProducts-product-content">
        <ProductInfo
          :product="product"
        />
        <ProductForm
          :product="product"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Slider from "./Slider";
import ProductInfo from "./ProductInfo";
import ProductForm from "./ProductForm";
export default {
  name: "Product",
  components: {ProductForm, ProductInfo, Slider},
  props: {
    product: {
      type: Object,
      required: true,
    }
  }
}
</script>

<style>

</style>
