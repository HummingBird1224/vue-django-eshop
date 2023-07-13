<template>
  <div class="p-Modal-mainRight">
    <div
      class="p-Modal-selectionThumb"
      :style="thumbStyle"
    >
    </div>
    <template
      v-if="isSelectedOriginalSize"
    >
      <FormModalSizeInputs
        v-if="originalSizeVal"
        v-bind:originalSizeVal="originalSizeVal"
        :originalSizeErrors="originalSizeErrors"
        @blurOriginalSizeInput="blurOriginalSizeInput"
      />
    </template>
    <template
      v-else-if="widgetType === 'modal-radio'"
    >
      <FormModalSelectionInfo
        :title="displayStr"
      />
    </template>
  </div>
</template>

<script>
import FormModalSelectionInfo from "./FormModalSelectionInfo";
import FormModalSizeInputs from "./FormModalSizeInputs";
import { computed, } from "vue";

export default {
  name: "FormModalDetail",
  components: {FormModalSizeInputs, FormModalSelectionInfo},
  props: {
    displayImage: {
      type: String
    },
    displayStr: {
      type: String
    },
    widgetType: {
      type: String,
    },
    originalSizeVal: {
      type: Object,
    },
    originalSizeErrors: {
      type: Object,
    },
    isSelectedOriginalSize: {
      type: Boolean
    }
  },
  emits: ['blurOriginalSizeInput'],
  setup(props, context) {
    const thumbStyle = computed(()=>{
      const style = {};

      if (props.displayImage) {
        style['background-image'] = `url(${props.displayImage})`;
      }

      return style;
    })

    const blurOriginalSizeInput = (key)=> {
      context.emit('blurOriginalSizeInput', key);
    }

    return {
      thumbStyle,
      blurOriginalSizeInput
    }
  }
}
</script>

<style scoped>

</style>
