<template>
  <section
    class="p-product-form"
  >
    <div class="p-product-formLeft" v-if="product.example_images[0]">
      <ThumbViewer />
      <SlideShow
        :example_images="product.example_images"
        :example_urls="product.example_urls"
      />
    </div>
    <div class="p-product-formLeft" v-else>
      <ThumbViewer />
    </div>

    <div class="p-product-formRight" v-if="canOrderOnSite && isContactRequired">
      <ProductInfo />
      <ProductForm/>
      <ProductContact/>
    </div>
    <div class="p-product-formRight" v-else-if="canOrderOnSite">
      <ProductInfo />
      <ProductForm/>
    </div>
    <div class="p-product-formRight is-contact" v-else-if="isContactRequired">
      <ProductInfo />
      <ProductContact/>
    </div>
  </section>
</template>

<script>
import ProductInfo from "./ProductInfo";
import ProductForm from "./ProductForm";
import StoreMixin from "../../mixins/StoreMixin";
import ProductContact from "./ProductContact";
import ThumbViewer from "./ThumbViewer";
import SlideShow from "./SlideShow";

export default {
  name: "ProductDetailForm",
  mixins: [StoreMixin],
  components: {ProductContact, ProductForm, ProductInfo, ThumbViewer, SlideShow},
  computed: {
    product() {
      return this.state.product;
    },
    canOrderOnSite() {
      return this.product.info.can_order_on_site;
    },
    isContactRequired() {
      return this.product.info.is_contact_required;
    }
  }
}
</script>

<style scoped>

</style>
