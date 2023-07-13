<template>
  <div v-if="modalBlocks.title">
    <a
      href="#"
      class="p-productSelect-help"
      @click.prevent.stop="toggleModal"
    >{{ modalBlocks.title }}</a>
    <HelpModal
      :isOpen="isOpeningModal"
      :modalBlocks="modalBlocks"
      @close="closeModal"
    />
  </div>
</template>

<script>
import HelpModal from "./modal/help/HelpModal";
import { useModal } from "./../../../providers/useModal";
export default {
  name: "ProductSelectNote",
  components: {HelpModal},
  props: {
    modalBlocks :{
      type: Object
    }
  },
  setup(props) {
    const { modalBlocks } = props;
    return {
      modalBlocks,
      ...useModal(),
    }
  }
}
</script>

<style scoped>

</style>
