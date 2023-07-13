<template>
  <ModalWindow
    :isShow="isShow"
    class="c-modal--white">
    <div
      ref="modalContent"
      class="p-reorderModal"
    >
     <div
      ref="modalContent"
      class="p-reorderModal-contents"
      v-if="isDesignSelected"
    >
      <div class="contents-header">
        <h1> {{ selectedDesign.name }}  </h1>
        <div class="close-button" @click="close">
          <svg>
            <use xlink:href='#icons-cross'/>
          </svg>
        </div>
      </div>
      <div class="contents-wrapper">
        <div class="leftside pane">
          <div class="mydesign-photo" :style="{ backgroundImage: `url(${selectedDesign.image})`}">
          </div>
          <div class="mydesign-spec">
            <h1> 商品詳細</h1>
            <ul>
              <li v-for="(label, i) in strippedLabels" :key="i">
                <div>
                  <svg class="attribute-icon">
                    <use :xlink:href='"#icons-" + label.icon'/>
                  </svg>
                  <span> {{ label.text }} </span>
                </div>
              </li>
            </ul>
          </div>
        </div>
        <div class="rightside pane">
          <div class="order-selection">
            <div class="order-number_header">
              <svg class="icon">
                <use xlink:href="#icons-recipe" />
              </svg>
              <h3>注文数</h3>
            </div>
            <ul class="order-number_contents">
              <li v-for="(selection, i) in orderSelection" :key="i" @click="selectPosition(selection.position)">
                <div>
                  <input type="radio" :checked="selection.position == selectedPosition" @change="selectPosition(selection.position)"/>
                  <span class="amount-label"> {{ selection.name }} </span>
                </div>
                <span class="price-label"> {{ $filters.toPriceFormat(estimatedTotalPrice(selection.value)) }}円   </span>
              </li>
            </ul>
            <div class="price-detail" v-if="currentSelectPrice">
              <span class="price-title">商品価格</span>
              <span class="price-value"> {{ $filters.toPriceFormat(currentSelectPrice.product_total) }}円 </span>
            </div>
            <div class="price-detail" v-if="currentSelectPrice">
              <span class="price-title">版代</span>
              <span class="price-value"> {{ $filters.toPriceFormat(currentSelectPrice.plate_price) }}円 </span>
            </div>
            <div class="price-detail" v-if="currentSelectPrice">
              <span class="price-title">木型代</span>
              <span class="price-value"> {{ $filters.toPriceFormat(currentSelectPrice.mold_price)}}円 </span>
            </div>
            <div class="price-detail" v-if="currentSelectPrice">
              <span class="price-title">送料</span>
              <span class="price-value"> {{ $filters.toPriceFormat(currentSelectPrice.shipping_price) }}円 </span>
            </div>
            <div class="price-detail" v-if="currentSelectPrice">
              <span class="price-title">消費税</span>
              <span class="price-value"> {{ $filters.toPriceFormat(currentSelectPrice.tax) }}円 </span>
            </div>
          </div>
          <div class="total-price" v-if="currentSelectPrice">
            <span class="price-title">合計</span>
            <div>
              <span class="price-detail">
                {{ $filters.toPriceFormat(currentSelectPrice.total) }}
                <span class="price-suffix">円（税込）</span>
              </span>
              <span class="unit-price-label"> {{ currentSelectPrice.unit_price }}円/個</span>
            </div>
          </div>
          <div class="action-buttons">
            <div class="button c-btn blue" @click="addCart">カートに入れる</div>
            <div class="button c-btn red" :class=" isFetchingInstantBuy ?  'is-loading' : '' " @click="instantBuy">
              <span v-show="!isFetchingInstantBuy" >今すぐ買う</span>
            </div>
          </div>
        </div>
      </div>
     </div>
    </div>
  </ModalWindow>
</template>

<script>
import ModalWindow from "../common/ModalWindow";
import { ref, computed, watchEffect } from 'vue';
import { useStore } from '../../providers/useStore';
export default {
  name: "ReorderMyDesignModal",
  components: {ModalWindow},
  props: {
    isShow: {
      type: Boolean,
    },
  },
  setup(props, context) {
    const isFetchingInstantBuy = ref(false);
    const isAddingCart = ref(false);
    const strippedLabels = ref([]);
    const { store, state} = useStore();

    const orderSelection = computed(()=>state.orderSelection);
    const selectedDesign = computed(()=>state.selectedDesign);
    const selectedPosition = computed(()=>state.selectedOrderPosition);
    const isDesignSelected = computed(()=> state.selectedDesign != null)
    const estimatedPriceObject = computed(()=>state.estimatedPriceObject);

    const estimatedTotalPrice = (count)=>{
      const estimatedValues = estimatedPriceObject.value;
      if (!estimatedValues.hasOwnProperty(count)) return ''
      const { product_total } = estimatedValues[count];
      return `${product_total}`
    }

    const currentSelectPrice = computed(()=>{
      if (!isDesignSelected.value) return null;

        const pos = selectedPosition.value;
        const element = orderSelection.value.find(el=>el.position == pos);
        const lot = element.value;
        return estimatedPriceObject.value[lot]
    })

    const selectPosition = position => store.selectPosition(position)
    const close = () => context.emit('close')
    const addCart = () => context.emit('addCart')

    const instantBuy = async () => {
      isFetchingInstantBuy.value = true;
      await store.instantBuy();
      isFetchingInstantBuy.value = false;
      context.emit('purchase')
    }

    const detailObject = computed(()=>state.detailObject);

    const setupStripLabels = ()=>{
      strippedLabels.value = [];

      // 属性ラベル生成
      strippedLabels.value.push({
        icon: "receipt",
        text: `カテゴリー：${detailObject.value.category}`
      })
      strippedLabels.value.push({
        icon: "receipt",
        text: `商品名：${detailObject.value.product_name}`
      })
      strippedLabels.value.push({
        icon: "measure",
        text: `サイズ：${selectedDesign.value.size}`
      })
      strippedLabels.value.push({
        icon: "color_lens",
        text: `印刷色数：${detailObject.value.read_only_options_str["色数"]}`
      })
      strippedLabels.value.push({
        icon: "paint",
        text: `印刷面数：${detailObject.value.read_only_options_str["印刷する面数"]}`
      })
      strippedLabels.value.push({
        icon: "access_time",
        text: `納期：${detailObject.value.shipping_date}日程度`
      })
    }

    watchEffect(()=>{
      if (selectedDesign.value != null) {
        setupStripLabels()
      }
    })

    return {
      isFetchingInstantBuy,
      isAddingCart,
      strippedLabels,
      state,
      orderSelection,
      selectedDesign,
      isDesignSelected,
      selectedPosition,
      currentSelectPrice,
      estimatedTotalPrice,
      selectPosition,
      close,
      addCart,
      instantBuy
    }
  }
}
</script>

<style scoped>

</style>
