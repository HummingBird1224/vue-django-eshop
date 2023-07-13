<template>
  <div v-if="caseStudyList">
    <ul class="p-ProductGenreList">
      <div class="p-ProductListWrapper ">
        <ul class="p-ProductList--new p-CaseStudyList" >
          <li class="p-caseStudy--new" v-for="item in caseStudyList" :key="item.slug" >
            <div class="p-caseStudyListThumb" v-if="item.images.length>0">
              <a :href="`/casestudies/product_category/${item.product_category[0].slug}/${item.slug}`" 
                v-if="isListView" 
                v-on:mouseover="setIsHoverImage(item.slug, true)" 
                v-on:mouseleave="setIsHoverImage(item.slug, false)">
                <div v-show="!isHoverImage[`${item.slug}`]" 
                    :style="{'background-image': `url(${item.images[0]})`}"
                    class="p-caseStudyThumb-back"></div>
                <div v-show="isHoverImage[`${item.slug}`]" 
                    :style="{'background-image': `url(${item.hover_image})`}" 
                    class="p-caseStudyThumb-back"></div>
              </a>
              <a  :href="`/casestudies/${category}/${tag}/${item.slug}`" 
                  v-else                
                  v-on:mouseover="setIsHoverImage(item.slug, true)" 
                v-on:mouseleave="setIsHoverImage(item.slug, false)">
                <div v-show="!isHoverImage[`${item.slug}`]" 
                    :style="{'background-image': `url(${item.images[0]})`}"
                    class="p-caseStudyThumb-back"></div>
                <div v-show="isHoverImage[`${item.slug}`]" 
                    :style="{'background-image': `url(${item.hover_image})`}" 
                    class="p-caseStudyThumb-back"></div>
              </a>
            </div>
            <div class="p-ProductDescriptionWrapper" v-if="item.images.length>0">
              <h4 class="g-title-quaternary p-ProductTitle">
                <a :href="`/casestudies/product_category/${item.product_category[0].slug}/${item.slug}`" 
                    v-if="isListView" >
                    {{ item.client }} : {{ item.title }}
                </a>
                <a :href="`/casestudies/${category}/${tag}/${item.slug}`" 
                    v-else >
                    {{ item.client }} : {{ item.title }}
                </a>
              </h4>
            </div>
          </li>
        </ul>
      </div>
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
              <div class="p-ProductThumb" v-on="hoverImg">
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
  name: "CaseStudyGenreList",
  mixins: [StoreMixin],
  components: {},
  data: () => ({
    isHoverImage: {},
  }),
  computed: {
    caseStudyList() {
      return this.state.caseStudyList
    },
    staticUrl() {
      return this.state.staticUrl;
    },
    category(){
      return this.state.category;
    },
    tag(){
      return this.state.tag;
    },
    isListView(){
      if(this.state.category=='all') return true;
      else false;
    }
  },
  methods: {
    setIsHoverImage(slug, isHover) {
      this.isHoverImage[slug] = isHover;
    }
  },
}
</script>

<style scoped>
</style>
