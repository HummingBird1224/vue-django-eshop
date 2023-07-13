<template>
  <div class="p-productSelect">
    <div
      v-if="!isActive"
      class="p-productSelect-cover"
    ></div>
    <header class="p-productSelect-header">
      <h3 class="g-title-tertiary p-productSelect-title">{{ option.name }}を選択</h3>
      <ProductSelectNote
        :modalBlocks="option.modal_blocks"
      />
    </header>
    <ul class="p-productSelect-horizontalList">
      <li
        v-for="item in items"
        :key="item.value"
        class="p-productSelect-horizontalItem"
        :class="{
          'is-current': isCurentValue(item.value)
        }"
        @click.prevent.stop="updateFormValue(item.value)"
      >
        <h4 class="g-title-quaternary">
          <span class="p-productSelect-horizontalRadio" />
          <span class="p-productSelect-horizontalTitle">{{ $filters.toPriceFormat(item.value) }}</span>
        </h4>

        <p
          v-if="price && price[item.value]"
          class="p-productSelect-horizontalPrice"
        >
          {{ $filters.toPriceFormat(displayPrice(item)) }}<span class="p-productSelect-horizontalPriceUnit">円</span>
        </p>
      </li>
    </ul>
  </div>
</template>

<script>
import ProductSelectNote from "./ProductSelectNote";
import { useStore } from '../../../providers/useStore';
import { useProductDetailForm } from '../../../providers/productDetail/useProductDetailForm';
import { inject, computed, watch, onBeforeMount, onMounted, reactive } from 'vue';

export default {
  name: "HorizontalSelect",
  components: { ProductSelectNote },
  props: {
    isActive: {
      type: Boolean
    },
    optionIndex: {
      type: Number
    }
  },
  emits: ['FormUpdated'],
  setup(props, context) {
    const options = inject('product_options');
    const { optionIndex, isActive } = props;
    const option = options[optionIndex];
    const { store, state } = useStore();
    const price = computed(()=>state.price);
    const displayPrice = (item)=>{
     return price.value[item.value].product_total
    }
    const name = option.slug;
    const { form, ownFormValue, updateFormValue: updateValue  } = useProductDetailForm(store, name);
    const widgetType = computed(() => option.widget_type)
    const items = computed(()=>option.items.sort((a, b) => a.position - b.position).filter(item => store.isMeetCondition(item.condition)))

    const isCurentValue = value => ownFormValue.value == value;
    const updateFormValue = (value) => {
      updateValue(value);
      context.emit('FormUpdated');
    }

    onMounted(()=> {
      updateFormValue(store.getDefaultItem(option).value);
    })

    return {
      name,
      option,
      form,
      ownFormValue,
      widgetType,
      items,
      updateFormValue,
      isActive,
      isCurentValue,
      state,
      displayPrice,
      price
    }
  },
}
</script>

<style scoped>

</style>
