<template>
  <div class="p-products-main">
    <nav class="p-productsNav">
      <CasestudiesNavCategory />
    </nav>
    <section class="p-productsMain">
      <CasestudiesCategoryHeader :category="category" />
      <CasestudyGenreList />
      <a href="https://docs.google.com/forms/d/1YO31XLGTYHRW7E8Bpe8pZmDCeUudCvf0oMuPFNTvVLk/viewform" target="_blank">
        <footer class="p-products-footer">
          <div class="p-products-footer-contactDescription">
            <h3 class="g-title-tertiary">お求めの商品が見当たらない場合</h3>
            <h4 class="g-title-quaternary">見積もり依頼・問い合わせをする</h4>
            <p>ご希望の材質・形状のパッケージをフォームからお問い合わせください。</p>
          </div>
          <div class="p-products-footer-contactIcon">
            <img :src="staticUrl + 'img/arrow_24.png'"/>
          </div>
        </footer>
      </a>
    </section>
  </div>
</template>

<script>
import CasestudiesNavCategory from '../components/casestudyList/CasestudiesNavCategory.vue'
import CasestudiesCategoryHeader from '../components/casestudyList/CasestudiesCategoryHeader.vue'
import CasestudyGenreList from '../components/casestudyList/CasestudyGenreList.vue'
import StoreMixin from "../mixins/StoreMixin"

export default {
  name: "CasestudyList",
  mixins: [StoreMixin],
  components: {CasestudiesNavCategory, CasestudiesCategoryHeader, CasestudyGenreList},
  computed: {
    staticUrl() {
      return this.state.staticUrl;
    },
    category(){
      return this.state.category;
    }
  },
  mounted() {
    // this.store.fetchProductCategory();
    this.store.fetchCaseStudyCategory();
    this.store.fetchCaseStudyList(this.state.category, this.state.tag);
  }
}
</script>

<style scoped>
</style>
