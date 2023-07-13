<template>
  <ul class="p-Modal-selections">
    <li
      v-for="item in items"
      :key="item.position"
      class="p-Modal-selection p-Modal-selection--checkbox"
      :class="{
        'is-active': selectingItem && selectingItem.includes(item.value)
      }"
      @click.prevent.stop="onClick(item.value)"
    >
      <span class="p-Modal-selectionIcon">
        <svg><use xlink:href='#icons-check'/></svg>
      </span>
      <span class="p-Modal-selectionLabel">{{ item.name }}</span>
    </li>
  </ul>
</template>

<script>
export default {
  name: "FormModalCheckBoxSelections",
  props: {
    items: {
      type: Array,
      required: true,
    },
    selectingItem: {
      type: Array
    }
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
