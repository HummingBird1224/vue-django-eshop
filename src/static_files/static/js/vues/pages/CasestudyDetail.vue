<template>
  <div class="p-products-main" v-if="!isInitialized">
    <nav class="p-productsNav">
      <CasestudiesNavCategory />
    </nav>
    <section class="p-productsMain">
      <CasestudyDetailView />
      <CasestudyDetailCard />
    </section>
  </div>
  <div
    class="p-product" v-else
  >
    <div class="p-product-wrapper">
      <main class="p-product-main">
        <div id="js-form-left" class="p-product-formLeft">
          <ul class="p-ProductThumbList">
            <li class="p-ProductThumb is-current" :style="{ backgroundImage: 'url(' + staticUrl + 'img/dummy/dummy_product.jpg)' }"></li>
            <li class="p-ProductThumb" :style="{ backgroundImage: 'url(' + staticUrl + 'img/dummy/dummy_product.jpg)' }"></li>
            <li class="p-ProductThumb" :style="{ backgroundImage: 'url(' + staticUrl + 'img/dummy/dummy_product.jpg)' }"></li>
            <li class="p-ProductThumb" :style="{ backgroundImage: 'url(' + staticUrl + 'img/dummy/dummy_product.jpg)' }"></li>
          </ul>
          <div class="p-ProductImage" :style="{ backgroundImage: 'url(' + staticUrl + 'img/dummy/dummy_product.jpg)' }">
          </div>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
import CasestudiesNavCategory from '../components/casestudyList/CasestudiesNavCategory.vue'
import CasestudyDetailView from '../components/casestudyDetail/CasestudyDetailView.vue'
import CasestudyDetailCard from '../components/casestudyDetail/CasestudyDetailCard.vue'
import StoreMixin from "../mixins/StoreMixin"

export default {
  name: 'CasestudyDetail',
  mixins: [StoreMixin],
  components: {CasestudiesNavCategory, CasestudyDetailView, CasestudyDetailCard},
  computed: {
    staticUrl() {
      return this.state.staticUrl;
    },
    sizeImageURL() {
      const p_slug = this.product.slug;
      const c_slug = this.product.category.slug;
      const mc_slug = this.product.main_category.slug;
      if (c_slug == "flatbag" || mc_slug == "flatbag") {
        return "img/product_detail/size_templates/参考サイズ用画像_平袋.jpg"
      }
      else if  (c_slug == "paperbox" || mc_slug == "paperbox") {
        return "img/product_detail/size_templates/参考サイズ用画像_紙器.jpg"
      }
      else if  (~p_slug.indexOf('atype')) {
        return "img/product_detail/size_templates/参考サイズ用画像_A式.jpg"
      }
      else if  (~p_slug.indexOf('ntype-corrugated')) {
        return "img/product_detail/size_templates/参考サイズ用画像_宅配用N式.jpg"
      }
      else if  (~p_slug.indexOf('ntype-mailer')) {
        return "img/product_detail/size_templates/参考サイズ用画像_配送用N式.jpg"
      }
      else if  (~p_slug.indexOf('ttype')) {
        return "img/product_detail/size_templates/参考サイズ用画像_配送用たとう式.jpg"
      }
    }
  },
  methods: {
    removeSlash: function(name, data) {
      if (name.indexOf('/') > -1) {
        return data.replace(/(.*)\//,"$1:")        
      }
      return data;
    }
  },
  mounted() {
    // this.store.fetchProductCategory();
    this.store.fetchCaseStudyCategory();
    this.store.fetchCaseStudy();
    this.store.fetchCaseStudySameTagList(this.state.detailCategory, this.state.detailTag, this.state.detailSlug)
  }
}
</script>

<style scoped>

</style>
