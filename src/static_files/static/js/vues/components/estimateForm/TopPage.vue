<template>
  <div>
    <PageBackButton
      @onClick="onClickPageBack"
    />

    <main class="p-Main">
      <div class="p-Main-left">
        <header class="p-Header">
          <h2 class="g-title-secondary p-Header-title">見積もり / 購入</h2>
          <p class="p-Header-body">選んだ項目によって値段が変化します。注文したい商品の詳細を選びましょう。</p>
        </header>

        <MenuList
          v-if="product"
        />
      </div>

      <div class="p-Main-right">
        <EstimateInfo
          v-if="product"
        />
      </div>
    </main>

    <Footer />
  </div>
</template>

<script>
import EstimateInfo from "./top/EstimateInfo.vue";
import MenuList from "./top/MenuList.vue";
import PageBackButton from "./PageBackButton.vue";
import Footer from "./top/Footer.vue";
import StoreMixin from "../../mixins/StoreMixin";

export default {
  name: "TopPage",
  mixins: [StoreMixin],
  components: {Footer, PageBackButton, MenuList, EstimateInfo},
  computed: {
    product() {
      return this.state.product;
    }
  },
  methods: {
    onClickPageBack() {
      location.href = this.state.absoluteUrl;
    }
  }
}
</script>

<style scoped>

</style>
