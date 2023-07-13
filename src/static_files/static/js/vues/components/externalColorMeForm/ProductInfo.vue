<template>
  <div class="p-externalColorMeProducts-product-content-info">
    <h2 class="g-title-secondary">{{ product.name }}</h2>
    <p>{{ product.overview }}</p>
    <ul>
      <li>
        <svg>
          <use xlink:href='#icons-access_time'/>
        </svg>
        <h6 class="g-title-quinary">納期</h6>
        <p>{{ shippingInfo }}</p>
      </li>
      <li>
        <svg>
          <use xlink:href="#icons-airport_shuttle"/>
        </svg>
        <h6 class="g-title-quinary">送料</h6>
        <p>無料</p>
      </li>
      <li>
        <svg>
          <use xlink:href='#icons-color_lens_24px_outlined'/>
        </svg>
        <h6 class="g-title-quinary">印刷できる色</h6>
        <ul>
          <template v-if="hasColorSelect">
            <li
              v-for="color in choosableColor"
              class="p-externalColorMeProducts-product-content-info-color-item"
            >
              <div class="p-externalColorMeProducts-product-content-info-color-image">
                <img :src="staticUrl + color.image">
              </div>
              <a v-if="color.link" :href="color.link" target="_blank">{{ `${color.name}　` }}</a>
              <p v-else>{{ `${color.name}　` }}</p>
            </li>
          </template>
          <template
            v-else
          >
            <li>
            <div
              class="p-externalColorMeProducts-product-content-info-color p-externalColorMeProducts-product-content-info-color--black"></div>
            <p>黒</p>
          </li>
          <li>
            <div
              class="p-externalColorMeProducts-product-content-info-color p-externalColorMeProducts-product-content-info-color--white"></div>
            <p>白</p>
          </li>
          </template>
        </ul>
      </li>
      <li v-if="hasNotes">
        <svg>
          <use xlink:href='#icons-remarks'/>
        </svg>
        <h6 class="g-title-quinary">備考</h6>
        <p v-for="note in notes">{{ note.key }}:{{ note.value }}</p>
      </li>
      <li v-if="isNotPlain">
        <svg>
          <use xlink:href='#icons-ic_han'/>
        </svg>
        <h6 class="g-title-quinary">版代</h6>
        <p>・原則、初回のみ費用が発生</p>
        <p>・サイズごとに必要です。</p>
      </li>
    </ul>
  </div>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin";

export default {
  name: "ProductInfo",
  mixins: [StoreMixin],
  props: {
    product: {
      type: Object,
      required: true
    }
  },
  computed: {
    isNotPlain() {
      return this.product.slug !== 'colorme-atype-plain';
    },
    shippingInfo() {
      if (this.product.info.estimated_shipping_date_first < 22) {
        return "データ確定後２〜３週間"
      } else {
        return "データ確定後１ヶ月"
      }
    },
    hasColorSelect() {
      return this.product.info.choosable_color;
    },
    hasNotes() {
      return this.product.info.notes.extra.length > 0;
    },
    notes() {
       return this.product.info.notes.extra;
    },
    // colorNums() {
    //   return Object.entries(this.product.extra_info.color_num.options)
    //   .map(x => x[1].name);
    // },
    choosableColor() {
      return this.product.info.choosable_color;
    },
    staticUrl() {
      return this.state.staticUrl;
    }
  }
}
</script>

<style>

</style>
