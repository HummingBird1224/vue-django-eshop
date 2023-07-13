<template>
  <Modal
    :isOpen="isOpen"
    @close="close"
  >
    <ModalHeader
      :title="title"
      @close="close"
    />

    <div class="p-Modal-main p-Modal-main--form">
      <div class="p-Modal-mainLeft">
        <div class="p-Modal-selectionWrapper">
          <h4 class="g-title-quaternary p-Modal-selectionTitle">{{ selectionTitle }}</h4>
          <template
            v-if="widgetType === 'modal-check'"
          >
            <FormModalCheckBoxSelections
              :items="items"
              :selectingItem="selectingItem"
              @onClick="updateForm"
            />
          </template>
          <template
            v-if="widgetType === 'modal-radio'"
          >
            <FormModalRadioSelections
              :items="items"
              :selectingItem="selectingItem"
              @onClick="updateForm"
            />
          </template>
        </div>
      </div>
      <FormModalDetail
        :displayImage="displayImage"
        :displayStr="displayStr"
        :widgetType="widgetType"
        :selectingItem="selectingItem"
        :originalSizeVal="originalSizeVal"
        :originalSizeErrors="originalSizeErrors"
        :isSelectedOriginalSize="isSelectedOriginalSize"
        @blurOriginalSizeInput="blurOriginalSizeInput"
      />
    </div>
    <ModalFooter
      :canSubmit="canSubmit"
      @submit="submit"
      @close="close"
    />
  </Modal>
</template>

<script>
import Modal from "../Modal";
import ModalHeader from "../ModalHeader";
import ModalFooter from "../ModalFooter";
import FormModalDetail from "./FormModalDetail";
import FormModalRadioSelections from "./FormModalRadioSelections";
import FormModalCheckBoxSelections from "./FormModalCheckBoxSelections";
import deepCopy from "../../../../../../helpers/deepCopy";
import { useStore } from "../../../../../providers/useStore"
import { useProductDetailForm } from "../../../../../providers/productDetail/useProductDetailForm"
import { ref, computed, watch, onMounted } from 'vue';


const isSameArray = (a, b) => {
  return JSON.stringify(a.sort()) === JSON.stringify(b.sort());
};

export default {
  name: "FormModal",
  components: {FormModalCheckBoxSelections, FormModalRadioSelections, FormModalDetail, ModalFooter, ModalHeader, Modal},
  props: {
    title: {
      type: String,
      required: true
    },
    isOpen: {
      type: Boolean,
      default: true
    },
    widgetType: {
      type: String,
      required: true
    },
    name: {
      type: String,
      required: true
    },
    option: {
      type: Object,
      required: true
    },
    currentSelectedOption: {
      required: true
    }
  },
  emits: ['updateFormValue', 'close'],
  setup(props, context) {
    const originalSizeVal = ref(null);
    const selectingItem = ref(null);
    const blurOriginalSizeKeys = ref([])
    const { name } = props;
    const { widget_type: widgetType, name: formName } = props.option;
    const { store, state } = useStore();
    const { form } = useProductDetailForm(store, formName)

    const selectionTitle = computed(()=>formName+"を選択しましょう")
    const isSelectedOriginalSize = computed(()=> {
      return name === 'size'
        && selectingItem.value
        && selectingItem.value.position === 0;
    })

    const sizeLimit = computed(()=>state.product.info.size_limit)

    const originalSizeErrors = computed(() => {
      if (!isSelectedOriginalSize.value) {
        return {};
      }

      return Object.entries(sizeLimit.value)
        .map(x => {
          let key = x[0];
          let hasBlur = blurOriginalSizeKeys.value.includes(key);

          let minVal = x[1].min;
          let maxVal = x[1].max;

          let formVal = originalSizeVal.value[key];

          // 数値判定.
          if (isNaN(formVal) || formVal === '' || formVal === null) {
            return [key, {
              msg: '数値を入力してください。',
              hasBlur,
            }];
          }

          formVal = Number(formVal);

          // 範囲判定.
          if (formVal > maxVal) {
            return [key, {
              msg: `${maxVal}以下の数値を入力してください。`,
              hasBlur,
            }];
          } else if (formVal < minVal) {
            return [key, {
              msg: `${minVal}以上の数値を入力してください。`,
              hasBlur,
            }];
          }

          return null;
        })
        .filter(x => x) // null削除.
        .reduce((obj, cur) => ({...obj, [cur[0]]: cur[1]}), {});
    })

    const hasOriginalSizeError = computed(()=>{
       if (!isSelectedOriginalSize.value) {
        return false;
      }
      return !!Object.keys(originalSizeErrors.value).length;
    })

    const canSubmit = computed(() => {
      if(!selectingItem.value || selectingItem.value.length == 0) {
        if (name == 'print_area_inside') return true;
        return false;
      }

      if (hasOriginalSizeError.value) return false;

      return true;
    })

    const items = computed(() => {

      const optionItems = props.option.items;
      // サイズの時はoriginalSizeの情報を追加する.
      if (name === 'size' && store.canSelectOriginalSize() && optionItems[0].position !== 0) {
        originalSizeVal.value = {
          width: '',
          height: ''
        };
        if (store.getSizeOptionHasDepth()) {
          originalSizeVal.value.depth = '';
        }
        optionItems.unshift({
          name: 'オリジナルサイズ',
          detail: null,
          image: props.option.image,
          value: originalSizeVal.value,
          position: 0
        })
      }

      return optionItems.sort((a, b) => a.position - b.position).filter(item => store.isMeetCondition(item.condition));
    });

    const defaultItem = computed(()=>store.getDefaultItem(props.option))
    const displayImage = computed(()=> {
      if (widgetType === 'modal-radio') {
        if (!selectingItem.value || !selectingItem.value.hasOwnProperty('image')) {
          return '';
        }
        return selectingItem.value.image;
      } else if (widgetType === 'modal-check') {
        return props.option.image;
      }
    })

    const displayStr = computed(()=>{
      if (name === 'size' && selectingItem.value && !isSelectedOriginalSize.value) {
        return `${selectingItem.value.name} ${selectingItem.value.detail}`;
      }
      return '';
    })

    watch(() => props.isOpen,
      (val)=>{
        if (val && widgetType == 'modal-radio' && selectingItem.value === null) {
          selectingItem.value = defaultItem.value || items.value[0]
        }
      }
    )

    const updateForm = (item)=>{
      switch(widgetType) {

        case 'modal-radio':
          selectingItem.value = item
          return
        case 'modal-check':
          if (selectingItem.value.includes(item)) {
            selectingItem.value = selectingItem.value.filter(x => x!== item)
          } else {
            selectingItem.value = [...selectingItem.value, item];
          }
      }
    }

    const blurOriginalSizeInput = (key) => {
      if (blurOriginalSizeKeys.value.includes(key)) {
        return
      }
      blurOriginalSizeKeys.value = [...blurOriginalSizeKeys.value, key];
    }

    const close = ()=>context.emit('close');
    const submit = () => {
      let formVal = null;

      if (widgetType == 'modal-radio') {
        if (name === 'size') {
          formVal = store.getSizeFormVal(selectingItem.value)
        }
      } else if (widgetType === 'modal-check') {
        formVal = selectingItem.value;
      }
      context.emit('updateFormValue', formVal);
      close();
    }

    onMounted(()=>{
      selectingItem.value = props.currentSelectedOption
      let formVal = null;
      if (widgetType === 'modal-radio') {
        if (name === 'size') {
          formVal = store.getSizeFormVal(defaultItem.value)
        }
        selectingItem.value = defaultItem.value;
      } else if (widgetType === 'modal-check') {
        if (defaultItem.value) {
          selectingItem.value = [defaultItem.value.name];
        } 
        formVal = selectingItem.value;
      }
      context.emit('updateFormValue', formVal, true);
    })

    return {
      originalSizeVal,
      selectingItem,
      blurOriginalSizeKeys,
      form,
      selectionTitle,
      isSelectedOriginalSize,
      originalSizeErrors,
      hasOriginalSizeError,
      canSubmit,
      items,
      defaultItem,
      sizeLimit,
      displayImage,
      displayStr,
      updateForm,
      blurOriginalSizeInput,
      close,
      submit,
    }
  }
}
</script>

<style scoped>

</style>
