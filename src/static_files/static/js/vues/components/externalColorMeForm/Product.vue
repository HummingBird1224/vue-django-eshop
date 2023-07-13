<template>
  <div class="p-externalColorMeProducts-product" :id="product.slug">
    <div class="p-externalColorMeProducts-product-wrapper">
      <Slider
        :images="product.images"
      />

      <div class="p-externalColorMeProducts-product-content">
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
