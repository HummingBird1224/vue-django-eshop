<template>
  <div v-if="productList">
    <ul class="p-ProductGenreList" v-if="productList.categories">
      <li class="p-ProductGenre" v-for="category in productList.categories" :key="category.slug">
        <h3 class="p-ProductGenre-title">{{ category.name }}</h3>
        <span>{{ category.detail }}</span>
        <h4 class="p-ProductGenreTags">
          <span v-for="(tag, index) in category.tags" :key="index">
            <span v-if="index !== 0" class="p-ProductGenreTags-partition">/</span>
            <img :src="staticUrl+tag.icon" />
            {{tag.name}}
          </span>
          </h4>
        <div class="p-ProductListWrapper">
          <ul class="p-ProductList--new">
            <li class="p-Product--new" v-for="product in category.products" :key="product.name">
              <div class="p-ProductThumb">
                <ul class="p-ProductTags p-ProductTags--new">
                  <li v-for="tag in product.tags" :key="tag.name">{{tag.name}}</li>
                </ul>
                <a :href="product.url" v-on:mouseover="setIsHoverImage(product.slug, true)" v-on:mouseleave="setIsHoverImage(product.slug, false)">
                  <img v-show="!isHoverImage[product.slug]" :src="product.images[0]" />
                  <img v-show="isHoverImage[product.slug]" :src="product.hover_image" />
                </a>
              </div>
              <div class="p-ProductDescriptionWrapper">
                <h4 class="g-title-quaternary p-ProductTitle"><a :href="product.url">{{ product.name }}</a></h4>
                <!-- <p class="p-ProductBody" v-if="product.price.value">
                  <span class="p-ProductBody--priceNumber">{{product.price.value}}</span>{{product.price.suffix}} / <span class="p-ProductBody--priceNumber">1</span>{{product.price.unit}}（{{product.price.lot}}{{product.price.unit}}のとき）
                </p>
                <p class="p-ProductBody" v-else>
                  価格に関してはお問い合わせください
                </p>
                <p class="p-ProductBody p-ProductBody--blue">
                  ロットごとのお見積もりへ
                </p> -->
                <div class="p-ProductBody--lots">
                  <ul>
                     <li v-for="(value, key) in product.lots" class="p-ProductBody--lot">
                       <a :href="value" class="c-btn">{{key}}</a>
                     </li>
                  </ul>
                </div>
              </div>
            </li>
          </ul>
        </div>
      </li>
    </ul>
  </div>
  <div v-else>
    <ul class="p-ProductGenreList">
      <li class="p-ProductGenre">
        <h3 class="p-ProductGenre-title">---</h3>
        <span>---</span>
        <div class="p-ProductListWrapper">
          <ul class="p-ProductList--new">
            <li class="p-Product--new">
              <div class="p-ProductThumb">
                <a href="#">
                  <img :src="staticUrl + 'img/dummy/dummy_product.jpg'" />
                </a>
              </div>
              <div class="p-ProductDescriptionWrapper">
                <h4 class="g-title-quaternary p-ProductTitle"><a href="#">---</a></h4>
                <p class="p-ProductInfo"><svg><use xlink:href='#icons-access_time'/></svg>納期: ---</p>
                <p class="p-ProductInfo"><img :src="staticUrl + 'img/product_category/tags/drop.svg'" />色数: ---</p>
              </div>
            </li>
            <li class="p-Product--new">
              <div class="p-ProductThumb">
                <a href="#">
                  <img :src="staticUrl + 'img/dummy/dummy_product.jpg'" />
                </a>
              </div>
              <div class="p-ProductDescriptionWrapper">
                <h4 class="g-title-quaternary p-ProductTitle"><a href="#">---</a></h4>
                <p class="p-ProductInfo"><svg><use xlink:href='#icons-access_time'/></svg>納期: ---</p>
                <p class="p-ProductInfo"><img :src="staticUrl + 'img/product_category/tags/drop.svg'" />色数: ---</p>
              </div>
            </li>
            <li class="p-Product--new">
              <div class="p-ProductThumb">
                <a href="#">
                  <img :src="staticUrl + 'img/dummy/dummy_product.jpg'" />
                </a>
              </div>
              <div class="p-ProductDescriptionWrapper">
                <h4 class="g-title-quaternary p-ProductTitle"><a href="#">---</a></h4>
                <p class="p-ProductInfo"><svg><use xlink:href='#icons-access_time'/></svg>納期: ---</p>
                <p class="p-ProductInfo"><img :src="staticUrl + 'img/product_category/tags/drop.svg'" />色数: ---</p>
              </div>
            </li>
            <li class="p-Product--new">
              <div class="p-ProductThumb">
                <a href="#">
                  <img :src="staticUrl + 'img/dummy/dummy_product.jpg'" />
                </a>
              </div>
              <div class="p-ProductDescriptionWrapper">
                <h4 class="g-title-quaternary p-ProductTitle"><a href="#">---</a></h4>
                <p class="p-ProductInfo"><svg><use xlink:href='#icons-access_time'/></svg>納期: ---</p>
                <p class="p-ProductInfo"><img :src="staticUrl + 'img/product_category/tags/drop.svg'" />色数: ---</p>
              </div>
            </li>
            <li class="p-Product--new">
              <div class="p-ProductThumb">
                <a href="#">
                  <img :src="staticUrl + 'img/dummy/dummy_product.jpg'" />
                </a>
              </div>
              <div class="p-ProductDescriptionWrapper">
                <h4 class="g-title-quaternary p-ProductTitle"><a href="#">---</a></h4>
                <p class="p-ProductInfo"><svg><use xlink:href='#icons-access_time'/></svg>納期: ---</p>
                <p class="p-ProductInfo"><img :src="staticUrl + 'img/product_category/tags/drop.svg'" />色数: ---</p>
              </div>
            </li>
            <li class="p-Product--new">
              <div class="p-ProductThumb">
                <a href="#">
                  <img :src="staticUrl + 'img/dummy/dummy_product.jpg'" />
                </a>
              </div>
              <div class="p-ProductDescriptionWrapper">
                <h4 class="g-title-quaternary p-ProductTitle"><a href="#">---</a></h4>
                <p class="p-ProductInfo"><svg><use xlink:href='#icons-access_time'/></svg>納期: ---</p>
                <p class="p-ProductInfo"><img :src="staticUrl + 'img/product_category/tags/drop.svg'" />色数: ---</p>
              </div>
            </li>
          </ul>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin"

export default {
  name: "ProductGenreList",
  mixins: [StoreMixin],
  components: {},
  data: () => ({
    isHoverImage: {},
  }),
  computed: {
    productList() {
      return this.state.productList
    },
    staticUrl() {
      return this.state.staticUrl;
    }
  },
  methods: {
    setIsHoverImage(slug, isHover) {
      this.isHoverImage[slug] = isHover;
    }
  }
}
</script>

<style scoped>
</style>
