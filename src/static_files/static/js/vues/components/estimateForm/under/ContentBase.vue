<template>
  <main class="p-Main">
    <div class="p-Main-left p-Main-left--under">
      <slot name="left"></slot>
    </div>

    <div class="p-Main-right p-Main-right--under">
      <slot name="right"></slot>
    </div>
  </main>
</template>

<script>
export default {
  name: "ContentBase"
}
</script>

<style scoped>

</style>
