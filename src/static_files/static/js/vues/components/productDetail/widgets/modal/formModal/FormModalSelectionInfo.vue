<template>
  <div class="p-Modal-selectionInfo">
    <p>{{ title }}</p>
    <span
      v-if="body"
    >{{ body }}</span>
  </div>
</template>

<script>
export default {
  name: "FormModalSelectionInfo",
  props: {
    title: {
      type: String,
      required: true,
    },
    body: {
      type: String,
    }
  }
}
</script>

<style scoped>

</style>
