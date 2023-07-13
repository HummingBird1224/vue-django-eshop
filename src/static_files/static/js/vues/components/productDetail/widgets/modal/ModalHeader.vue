<template>
  <header class="p-Modal-header">
    <h3 class="g-title-tertiary p-Modal-title">{{ title }}</h3>
    <a
      class="p-Modal-close"
      href="#"
      @click.prevent.stop="close"
    >
      <svg>
        <use xlink:href='#icons-cross'/>
      </svg>
    </a>
  </header>
</template>

<script>
export default {
  name: "ModalHeader",
  props: {
    title: {
      type: String,
      default: ''
    }
  },
  emits: ['close'],
  methods: {
    close() {
      this.$emit('close');
    }
  }
}
</script>

<style scoped>

</style>
