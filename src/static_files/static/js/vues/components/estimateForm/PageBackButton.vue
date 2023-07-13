<template>
  <a
    class="p-PageBack"
    href="#"
    @click.prevent.stop="onClick"
  >
    <span class="p-PageBack-iconWrapper">
      <svg class="p-PageBack-icon p-PageBack-icon--forward">
        <use xlink:href='#icons-arrow_forward'/>
      </svg>
    </span>
    戻る
  </a>
</template>

<script>
export default {
  name: "PageBackButton",
  emits: ['onClick'],
  methods: {
    onClick() {
      this.$emit('onClick');
    }
  }
}
</script>

<style scoped>

</style>
