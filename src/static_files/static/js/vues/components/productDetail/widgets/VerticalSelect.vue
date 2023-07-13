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
    <ul class="p-productSelect-verticalList">
      <li
        v-for="item in items"
        :key="item.value"
        class="p-productSelect-verticalItem"
        :class="{
          'p-productSelect-verticalItem--sm': widgetType === 'slider-sm',
          'p-productSelect-verticalItem--lg': widgetType === 'slider-lg',
          'is-current': item.value === ownFormValue,
          'no-thumb': !item.image
        }"
        @click.prevent.stop="updateFormValue(item.value)"
      >
        <div
          class="p-productSelect-verticalThumb"
          :style="{
            'background-image': `url(${item.image})`
          }"
        ></div>
        <h4 class="g-title-quaternary p-productSelect-verticalTitle">{{ item.name }}</h4>
      </li>
    </ul>
  </div>
</template>

<script>
import ProductSelectNote from "./ProductSelectNote";
import { inject,ref, computed, watchEffect, onBeforeMount, onMounted } from 'vue';
import { useStore } from '../../../providers/useStore';
import { useProductDetailForm } from '../../../providers/productDetail/useProductDetailForm';

export default {
  name: "VerticalSelect",
  components: {ProductSelectNote},
  props: {
    isActive: {
      type: Boolean,
    },
    optionIndex: {
      type: Number
    }
  },
  emits: ['FormUpdated'],
  setup(props, context) {
    const options = inject('product_options');
    const { optionIndex } = props;
    const option = options[optionIndex];
    const { store, state } = useStore();

    const name = option.slug;
    const { form, ownFormValue, updateFormValue: updateValue } = useProductDetailForm(store, name);
    const widgetType = computed(() => option.widget_type)
    const items = computed(()=>option.items.sort((a, b) => a.position - b.position).filter(item => store.isMeetCondition(item.condition)))

    const updateFormValue = (val)=> {
      updateValue(val)
      context.emit('FormUpdated');
    }

    onBeforeMount(() => {
      updateFormValue(null)
    })

    onMounted(()=> {
      updateFormValue(store.getDefaultItem(option).value)
    })

    return {
      name,
      option,
      form,
      ownFormValue,
      widgetType,
      items,
      updateFormValue
    }
  },
}
</script>

<style scoped>

</style>
