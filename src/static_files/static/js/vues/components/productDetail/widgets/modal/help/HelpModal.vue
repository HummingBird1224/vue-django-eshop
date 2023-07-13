<template>
  <Modal
    :isOpen="isOpen"
    @close="close"
  >
    <ModalHeader
      :title="modalBlocks.title"
      @close="close"
    />
    <div class="p-Modal-main p-Modal-main--help">
      <template
        v-for="(section, i) in sections"
      >
        <HelpHorizontalListSm
          :key="i"
          v-if="section.layout_type === 'horizontal-list-sm'"
          :section="section"
        />
        <HelpHorizontalListMd
          :key="i"
          v-if="section.layout_type === 'horizontal-list-md'"
          :section="section"
        />
        <HelpHorizontalListLg
          :key="i"
          v-if="section.layout_type === 'horizontal-list-lg'"
          :section="section"
        />
        <HelpVerticalListSm
          :key="i"
          v-if="section.layout_type === 'vertical-list-sm'"
          :section="section"
        />
        <HelpVerticalListMd
          :key="i"
          v-if="section.layout_type === 'vertical-list-md'"
          :section="section"
        />
        <HelpVerticalListLg
          :key="i"
          v-if="section.layout_type === 'vertical-list-lg'"
          :section="section"
        />
        <HelpGridListMd
          :key="i"
          v-if="section.layout_type === 'grid-list-md'"
          :section="section"
        />
      </template>
    </div>
  </Modal>
</template>

<script>
import Modal from "../Modal";
import ModalHeader from "../ModalHeader";
import HelpHorizontalListSm from "./HelpHorizontalListSm";
import HelpHorizontalListMd from "./HelpHorizontalListMd";
import HelpHorizontalListLg from "./HelpHorizontalListLg";
import HelpVerticalListSm from "./HelpVerticalListSm";
import HelpVerticalListMd from "./HelpVerticalListMd";
import HelpVerticalListLg from "./HelpVerticalListLg";
import HelpGridListMd from "./HelpGridListMd";

import {  computed } from 'vue'

export default {
  name: "HelpModal",
  components: {
    HelpGridListMd,
    HelpVerticalListLg,
    HelpVerticalListMd,
    HelpVerticalListSm,
    HelpHorizontalListLg,
    HelpHorizontalListMd,
    HelpHorizontalListSm,
    ModalHeader,
    Modal
  },
  props: {
    isOpen: {
      type: Boolean
    },
    modalBlocks: {
      type: Object
    }
  },
  emits: ['close'],
  setup(props, context) {
    const close = () => {
      context.emit('close');
    }
    const { modalBlocks } = props;
    const sections = computed(() => {
      if (modalBlocks.hasOwnProperty('sections')) {
        return modalBlocks.sections
      }

      return [];
    })
    return {
      close,
      sections
    }
  }
}
</script>

<style scoped>

</style>
