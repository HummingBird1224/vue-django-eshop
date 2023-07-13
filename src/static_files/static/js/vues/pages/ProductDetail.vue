<template>
  <div class="p-product" v-if="isInitialized">
    <div class="p-product-wrapper">
      <header class="p-product-header">
        <ol class="p-Breadcrumb">
          <li class="p-Breadcrumb-text"><a :href="'/'">ホーム</a></li>
          <li class="p-Breadcrumb-icon">
            <svg>
              <use xlink:href='#icons-arrow_down'></use>
            </svg>
          </li>
          <li class="p-Breadcrumb-text"><a :href="'/catalog/'+product.main_category.slug">{{ product.main_category.name }}</a></li>
          <li class="p-Breadcrumb-icon">
            <svg>
              <use xlink:href='#icons-arrow_down'></use>
            </svg>
          </li>
          <li class="p-Breadcrumb-text">{{ product.name }}</li>
        </ol>
      </header>
      <main class="p-product-main">
        <ProductDetailForm />

        <section class="p-product-spec" v-if="product.info.notes.extra && 0 < product.info.notes.extra.length">
          <h2 class="p-product-sectionTitle">商品詳細</h2>
          <ul class="p-SpecList">
            <li class="p-Spec" v-for="item in product.info.notes.extra" :key="item.key">
              <h3 class="g-title-tertiary p-Spec-title">{{ item.key }}</h3>
              <p class="p-Spec-body">{{ item.value }}</p>
            </li>
          </ul>
        </section>

        <section class="p-product-orderToDeliveryFlow">
          <h3 class="p-product-orderToDeliveryFlow-title">ご注文からお届けまでの流れ</h3>
          <div class="p-product-orderToDeliveryFlow-list-wrapper" v-if="isContactRequired">
            <ul class="p-product-orderToDeliveryFlow-list">
              <li class="p-product-orderToDeliveryFlow-list-item">
                <h4 class="p-product-orderToDeliveryFlow-list-item-header">
                  ❶商品を選びお問い合わせ
                </h4>
                <p class="p-product-orderToDeliveryFlow-list-item-text">
                  お問い合わせボタンから、必要な情報を記入しお問い合わせをお送り下さい。
                </p>
              </li>
              <li class="p-product-orderToDeliveryFlow-list-item">
                <h4 class="p-product-orderToDeliveryFlow-list-item-header">
                  ❷仕様調整・お見積もり
                </h4>
                <p class="p-product-orderToDeliveryFlow-list-item-text">
                  いただいた情報を元に、確認事項やお見積りをご連絡させていただきます。<br>
                  仕様の調整やサンプル手配も可能ですので、お気軽にご相談下さい。
                </p>
              </li>
              <li class="p-product-orderToDeliveryFlow-list-item">
                <h4 class="p-product-orderToDeliveryFlow-list-item-header">
                  ❸テンプレートを使用しデータ入稿
                </h4>
                <p class="p-product-orderToDeliveryFlow-list-item-text">
                  仕様が決まりましたら、弊社からデータのテンプレートをお送りします。<br>
                  テンプレートと入稿ルールに従ってご入稿下さい。
                </p>
              </li>
            </ul>
            <ul class="p-product-orderToDeliveryFlow-list">
              <li class="p-product-orderToDeliveryFlow-list-item">
                <h4 class="p-product-orderToDeliveryFlow-list-item-header">
                  ❹印刷内容のご確認・修正
                </h4>
                <p class="p-product-orderToDeliveryFlow-list-item-text">
                  当社よりお送りする確認用の印刷デザインをご確認していただきます。<br>
                  デザインの修正が必要な場合、ご修正いただくことが可能です。
                </p>
              </li>
              <li class="p-product-orderToDeliveryFlow-list-item">
                <h4 class="p-product-orderToDeliveryFlow-list-item-header">
                  ❺ご注文
                </h4>
                <p class="p-product-orderToDeliveryFlow-list-item-text">
                  デザイン修正が必要ない場合は、データを確定しご注文確定となります。<br>
                  請求書などを別途送付しますので、内容のご確認をお願いいたします。
                </p>
              </li>
              <li class="p-product-orderToDeliveryFlow-list-item">
                <h4 class="p-product-orderToDeliveryFlow-list-item-header">
                  ❻納品・再注文
                </h4>
                <p class="p-product-orderToDeliveryFlow-list-item-text">
                  ご注文時に確定した納品先に納品させていただきます。<br>
                  再注文はメールなどでご連絡いただくことで注文いただくことが可能です。
                </p>
              </li>
            </ul>
          </div>
          <div class="p-product-orderToDeliveryFlow-list-wrapper" v-else>
            <ul class="p-product-orderToDeliveryFlow-list">
              <li class="p-product-orderToDeliveryFlow-list-item">
                <h4 class="p-product-orderToDeliveryFlow-list-item-header">
                  ❶注文数量を選択
                </h4>
                <p class="p-product-orderToDeliveryFlow-list-item-text">
                  こちらの商品の数量を選び「印刷内容の指定」ボタンをクリックしてください。
                </p>
              </li>
              <li class="p-product-orderToDeliveryFlow-list-item">
                <h4 class="p-product-orderToDeliveryFlow-list-item-header">
                  ❷デザイン指定・データ入稿
                </h4>
                <p class="p-product-orderToDeliveryFlow-list-item-text">
                  画面上の展開図に、印刷するデザインの配置指定を行います。<br />
                  Illustratorなどの編集ソフトをお持ちの方は、配置用テンプレートをダウンロードしてデータ作成後、当社までメールでデータをお送りください。
                </p>
              </li>
              <li class="p-product-orderToDeliveryFlow-list-item">
                <h4 class="p-product-orderToDeliveryFlow-list-item-header">
                  ❸カートに入れて注文
                </h4>
                <p class="p-product-orderToDeliveryFlow-list-item-text">
                  印刷内容をご確認いただき、商品をカートに入れてご注文ください。<br />
                  カート内の「備考欄」に、このページ下部の「ご注文方法」にある必要事項をご記載ください。
                </p>
              </li>
            </ul>
            <ul class="p-product-orderToDeliveryFlow-list">
              <li class="p-product-orderToDeliveryFlow-list-item">
                <h4 class="p-product-orderToDeliveryFlow-list-item-header">
                  ❹印刷内容のご確認・修正
                </h4>
                <p class="p-product-orderToDeliveryFlow-list-item-text">
                  当社よりお送りする確認用の印刷デザインをご確認していただきます。<br />
                  デザインの修正が必要な場合、1回のみ無料で承ります。<br />
                  2回目以降は、修正1回につき「修正費用：2,000円（税抜）」が必要です。
                </p>
              </li>
              <li class="p-product-orderToDeliveryFlow-list-item">
                <h4 class="p-product-orderToDeliveryFlow-list-item-header">
                  ❺印刷データを承認
                </h4>
                <p class="p-product-orderToDeliveryFlow-list-item-text">
                  当社よりお送りした確認用の印刷デザインが問題ない場合、ご承認をいただくことでご注文確定となります。納期などについてはご注文後に確定し、ご連絡いたします。
                </p>
              </li>
              <li class="p-product-orderToDeliveryFlow-list-item">
                <h4 class="p-product-orderToDeliveryFlow-list-item-header">
                  ❻納品・再注文
                </h4>
                <p class="p-product-orderToDeliveryFlow-list-item-text">
                  ご注文時に確定した納品先に納品させていただきます。<br>
                  再発注はマイページからご注文いただくことが可能です。
                </p>
              </li>
            </ul>
          </div>
        </section>
        <section v-if="sizeOptionItems.length" class="p-product-sizeTemplate">
          <h2 class="p-product-sectionTitle">参考サイズ</h2>
          <div class="p-product-sizeTemplate-wrapper">
            <div class="p-product-sizeTemplate-image">
              <img :src="staticUrl + sizeImageURL" alt="">
            </div>
            <div class="p-product-sizeTemplate-sizes">
              <ul class="p-TemplateList">
                <li class="p-Template" v-for="size in sizeOptionItems" :key="size.name">
                  <div class="p-Template-content">
                    <h3 class="g-title-tertiary p-Template-title">{{ size.name }}</h3>
                    <p class="p-Template-body">{{ size.detail }}</p>
                  </div>
                  <a v-if="size.name != 'オリジナルサイズ'" class="p-Template-link c-textLink" :href="staticUrl + removeSlash(size.name, size.data)">テンプレートをダウンロード</a>
                  <p v-else class="p-Template-link c-textLink" href="">ご注文後こちらからお送りします</p>
                </li>
              </ul>
            </div>
          </div>
        </section>
      </main>
    </div>
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
import ProductDetailForm from '../components/productDetail/ProductDetailForm'

export default {
  name: 'ProductDetail',
  components: {ProductDetailForm},
  computed: {
    isInitialized() {
      return this.state.isInitialized;
    },
    product() {
      return this.state.product;
    },
    staticUrl() {
      return this.state.staticUrl;
    },
    state() {
      return this.store.state;
    },
    canOrderOnSite() {
      return this.product.info.can_order_on_site;
    },
    isContactRequired() {
      return this.product.info.is_contact_required;
    },
    sizeOptionItems() {
      const sizeOption = this.store.getOptionBySlug('size');
      return sizeOption.items;
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
    this.store.init();
  }
}
</script>

<style scoped>

</style>
