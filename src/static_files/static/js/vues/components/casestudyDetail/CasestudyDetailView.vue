<template>
  <div v-if="caseStudy">
    <ul class="p-ProductGenreList m-b-30">
      <div class="container m-b-30">
        <!-- <div class="image-wrapper  row">
          <div  class="col-md-9" id="imageDiv">
            <img :src="caseStudy.images[0]" />
          </div>
          <div class="col-md-3" >
            <img  :src="image" :alt="caseStudy.title" class="m-b-30" v-for="image in caseStudy.images.slice(1)" />          
          </div>
        </div> -->
        <div class="p-product-formRight" v-if="caseStudy.images.length>0">
          <ThumbViewer/>
        </div>
        <div class="description-wrapper m-t-30">
          <h1>{{ caseStudy.client }} : {{ caseStudy.title }}</h1>
          <pre>{{caseStudy.text}}</pre>
          <a :href="caseStudy.text_url" target="_blank" v-if="caseStudy.text_url">
            {{ caseStudy.text_url }}
          </a>
          <ul class="p-SpecList">
            <li class="p-Spec" v-for="item in caseStudyCategory.results" :key="item.slug">
              <h3 class="g-title-tertiary p-Spec-title">{{ item.name }}</h3>
              <div class="p-Spec-body">
                <a  class="p-Spec-content" 
                  v-for="category in caseStudy[item.slug]" 
                  :key="category.slug"
                  :href="category.URL"
                  target="_blank"
                  style="marginRight:10px"
                >
                  {{ category.name + ' ' }}
                </a>
              </div>
            </li>
          </ul>
        </div>
      </div>
      <div class="p-ProductListWrapper ">
        <h1>
          <img class="p-productsCategoryHeader--new-headerImage " :src="staticUrl+'img/product_category/flatbag/category_flatbag_all.png'" />
          関連する事例
        </h1>

        <VueperSlides
          class="no-shadow"
          ref="slide"
          slide-image-inside
          :visible-slides="5"
          :gap="3"
          :arrows-outside="false"
          :slide-ratio="1/8"
          :arrows="true"
          :bullets="false"          
          @previous="previous($event, $refs.slide)"
          @next="next($event, $refs.slide)"
          >
          <VueperSlide 
            v-for="item in caseStudyList" 
            :key="item.id" 
            :image="item.images[0]" 
            :link="`/casestudies/${category}/${tag}/${item.slug}`"   
          />
        </VueperSlides>
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
import ThumbViewer from "./ThumbViewer.vue";
import { VueperSlides, VueperSlide } from 'vueperslides'
import 'vueperslides/dist/vueperslides.css'
// import SlideShow from "../productDetail/SlideShow";

export default {
  name: "CaseStudyDetailView",
  mixins: [StoreMixin],
  components: {ThumbViewer, VueperSlides, VueperSlide},
  data: () => ({
    isHoverImage: {},
  }),
  computed: {
    caseStudy() {
      return this.state.caseStudy
    },
    staticUrl() {
      return this.state.staticUrl;
    },
    caseStudyCategory() {
      return this.state.caseStudyCategory;
    },
    category(){
      return this.state.detailCategory;
    },
    tag(){
      return this.state.detailTag;
    },
    caseStudyList(){
      return this.state.caseStudySameTagList;
    }
  },
  methods: {
    setIsHoverImage(slug, isHover) {
      this.isHoverImage[slug] = isHover;
    },
    previous(event, ref){
      let c_i=event.currentSlide?event.currentSlide.index:0;
      let s_count=this.caseStudyList.length;
      if(c_i>s_count-3){
        ref.goToSlide(s_count-3)
      }
      else if(c_i<3 ){
        ref.goToSlide(0)
      }
    },
    next(event, ref){
      let c_i=event.currentSlide?event.currentSlide.index:0;
      let s_count=this.caseStudyList.length;
      if(c_i<2){
        ref.goToSlide(2)
      }
      else if(c_i>s_count-4){
        ref.goToSlide(0)
      }
    },
  },
}
</script>

<style scoped>
</style>
