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
    <ul class="p-productSelect-ModalButtons">
      <ModalButton
        :key="option.name"
        :parentName="name"
        :parentNameJa="option.name"
        :widgetType="option.widget_type"
        :name="option.slug"
        :option="option"
        @onUpdate="onUpdate"
      />
    </ul>
  </div>
</template>

<script>
import ProductSelectNote from "./ProductSelectNote";
import ModalButton from "./modal/ModalButton";
import { inject } from 'vue';

export default {
  name: "ModalSelect",
  components: {ModalButton, ProductSelectNote},
  props: {
    isActive: {
      type: Boolean,
    },
    optionIndex: {
      type: Number,
    }
  },
  emits: ['FormUpdated'],
  setup(props, context) {
    const options = inject('product_options');
    const { optionIndex } = props;
    const option = options[optionIndex];

    const onUpdate = () => {
      context.emit('FormUpdated');
    }

    const name = option.slug;
    return {
      name,
      option,
      onUpdate,
    }
  }
}
</script>

<style scoped>

</style>
