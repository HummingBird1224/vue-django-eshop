<template>
  <div class="p-Modal-selectionForm">
    <h4 class="g-title-quaternary">サイズを入力</h4>
    <div class="p-Modal-selectionInputs">
      <FormModalSizeInputItem
        v-for="key in Object.keys(originalSizeVal)"
        :key="key"
        :name="key"
        :error="originalSizeErrors[key]"
        v-model="originalSizeVal[key]"
        @blurOriginalSizeInput="blurOriginalSizeInput"
      />
    </div>
  </div>
</template>

<script>
import FormModalSizeInputItem from "./FormModalSizeInputItem";

export default {
  name: "FormModalSizeInputs",
  components: {FormModalSizeInputItem},
  props: {
    originalSizeVal: {
      type: Object,
      required: true,
    },
    originalSizeErrors: {
      type: Object,
      required: true,
    }
  },
  emits: ['blurOriginalSizeInput'],
  setup(props, context) {
    const blurOriginalSizeInput = (key) => {
      context.emit('blurOriginalSizeInput', key)
    };
    return {
      blurOriginalSizeInput
    }
  }
}
</script>

<style scoped>

</style>
