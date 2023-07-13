<template>
  <div class="p-product-formRight-form">
    <div class="p-ProductContact">
      <div class="p-ProductContact-content">
        <h3 class="g-title-tertiary p-ProductContact-title" v-if="canOrderOnSite && isContactRequired">
          <svg>
            <use xlink:href="#icons-textsms"></use>
          </svg>
          ご希望の注文数が選択肢にない場合はお問い合わせください
        </h3>
        <h3 class="g-title-tertiary p-ProductContact-title" v-else>
          <svg>
            <use xlink:href="#icons-textsms"></use>
          </svg>
          この商品はお問い合わせで相談してからの発注になります
        </h3>
        <p class="p-ProductContact-body">内容によっては変更をご相談する部分があるかもしれません</p>
        <a
          class="p-ProductContact-cta c-btn c-btn--primary"
          target="_blank"
          :href="contactUrl"
        >
          注文のお問い合わせへ
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin";
import Product from "../externalBaseForm/Product";

export default {
  name: "ProductContact",
  components: {Product},
  mixins: [StoreMixin],
  computed: {
    contactUrl() {
      return this.state.contactUrl;
    },
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
