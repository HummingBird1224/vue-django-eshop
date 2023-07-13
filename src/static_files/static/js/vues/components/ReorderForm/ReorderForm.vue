<template>
  <div>
    <form v-on:submit.prevent="submit">
      <div class="p-reorderContent">
        <div class="p-reorderContent-left">
          <img :src="itemThumbnail">
        </div>
        <div class="p-reorderContent-right">
          <h2>{{ itemName }}</h2>
          <ul class="p-reorderContent-info">
            <li>色数：　{{ itemColor }}</li>
            <li v-for="(value, name) in renderedInfo" :key="name">
              {{ name }}：　{{ value }}
            </li>
          </ul>
          <SelectInput
            name="quantity"
            label="注文数"
            placeholder="注文数"
            rules="required"
            :isShowLabel="true"
            :options="quantitySelection"
          />
          <div class="p-reorderContent-price">
            <div class="p-reorderContent-price-totalContent">
              <span class="p-reorderContent-price-totalTitle">合計</span>
              <span v-if="priceInfo" class="p-reorderContent-price-totalBody">{{ $filters.toPriceFormat(priceInfo.total) }}</span>
              <span v-else class="p-reorderContent-price-totalBody">-</span>
              <span class="p-reorderContent-price-totalUnit">円（税込）</span>
            </div>
            <hr>
            <div class="p-reorderContent-price-orderPrices">
              <ul>
                <li>
                  <span class="p-reorderContent-price-priceTitle">単価</span>
                  <span v-if="priceInfo" class="p-reorderContent-price-priceBody">{{ $filters.toPriceFormat(priceInfo.unit_price) }}</span>
                  <span v-else class="p-reorderContent-price-priceBody">-</span>
                  <span class="p-reorderContent-price-unitPer">円 /</span>
                  <span class="p-reorderContent-price-unitUnit">{{ itemUnit }}</span>
                </li>
                <li>
                  <span class="p-reorderContent-price-priceTitle">消費税</span>
                  <span v-if="priceInfo" class="p-reorderContent-price-priceBody">{{ $filters.toPriceFormat(priceInfo.tax) }}</span>
                  <span v-else class="p-reorderContent-price-priceBody">-</span>
                  <span class="p-reorderContent-price-priceUnit">円</span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <button
        type="submit"
        class="c-btn p-reorderContent-submit"
        :class="{
          'is-disabled': !canSubmit,
          'is-loading': isSubmitting,
        }"
      >再注文</button>
    </form>
   </div>
</template>

<script>
import SelectInput from "../common/SelectInput";
import { reactive, computed, watch, } from "vue";
import { useStore } from "../../providers/useStore";
import { useFormValidation } from "../../providers/formValidation"
import { useForm } from "vee-validate";

export default {
  name: "ReorderForm",
  components: { SelectInput },
  setup() {

    // datas
    const compState = reactive({
      isProcessing: false,
    })

    // providers
    const { store, state } = useStore();
    const { values, errors } = useForm();
    const { hasNoError } = useFormValidation(errors, values, 0)

    store.init();

    // computed
    const canSubmit = computed(() => {
      if (!hasNoError.value) {
        return false;
      }

      return values.quantity !== ""
    })
    const orderInfo = computed(()=>state.orderInfo);
    const itemName = computed(()=>state.orderInfo.product_name);
    const itemThumbnail = computed(()=>state.staticUrl + orderInfo.value.thumbnail);
    const itemUnit = computed(()=>orderInfo.value.unit);
    const renderedInfo = computed(()=>orderInfo.value.rendered_info);
    const itemColor = computed(()=> {
      let color = itemInfo.value.color_num;
      if (color > 0) {
        return color + "色";
      }
      else if (color === 0) {
        return "無職";
      }
      else if (color < 0) {
        return "フルカラー";
      }
    });
    const itemInfo = computed(()=>orderInfo.value.extra_info);
    const quantitySelection = computed(()=>orderInfo.value.choosable_quantity);
    const price = computed(()=>state.price);
    const priceInfo = computed(()=>{
      if (!price.value) return null;

      return price.value;
    })

    const isSubmitting = computed(()=>state.isSubmitting);

    watch(
      ()=> values,
      async (val)=>{
        if (val.quantity === "" || !val.quantity) return
        await store.postEstimate(val.quantity)
      },
      { deep: true }
    )

    const submit = async () => {
      console.log(values.quantity)
      await store.postReorder(values.quantity)
      location.href = '/cart/';
    }

    return {
      state: compState,
      orderInfo,
      itemName,
      itemThumbnail,
      itemUnit,
      renderedInfo,
      itemColor,
      quantitySelection,
      price,
      priceInfo,
      isSubmitting,
      canSubmit,
      submit
    }
  }
}
</script>

<style scoped>
</style>
