<template>
  <ul class="p-Modal-selections">
    <li
      v-for="item in items"
      :key="item.name"
      class="p-Modal-selection p-Modal-selection--radio"
      :class="{
        'is-active': selectingItem && item === selectingItem
      }"
      @click.prevent.stop="onClick(item)"
    >
      <span class="p-Modal-selectionIcon"/>
      <span class="p-Modal-selectionLabel">{{ item.name }}<span class="p-Modal-selectionSupplement">{{ item.detail }}</span></span>
    </li>
  </ul>
</template>

<script>
export default {
  name: "FormModalRadioSelections",
  props: {
    items: {
      type: Array,
      required: true,
    },
    selectingItem: {
      type: Object
    },
  },
  emits: ['onClick'],
  methods: {
    onClick(item) {
      this.$emit('onClick', item);
    }
  }
}
</script>

<style scoped>

</style>
