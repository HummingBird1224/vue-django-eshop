<template>
  <section
    class="p-externalColorMeProducts-product-content-purchase-size"
    :class="{
      'p-externalColorMeProducts-product-content-purchase--disabled': !canChange
    }"
  >
    <h4 class="g-title-quaternary">素材を選択</h4>
    <ul class="p-externalColorMeProducts-product-content-purchase-options">
      <li
        v-for="option in surfaceMaterial.items"
        :key="option.position"
        class="p-externalColorMeProducts-product-content-purchase-options-option p-externalColorMeProducts-product-content-purchase-options-option--lg"
        :class="{
          'p-externalColorMeProducts-product-content-purchase-options-option--selected': option.value === form.surface_material
        }"
        :style="{
          'background-image': `url(${option.image})`
        }"
        @click.prevent.stop="onClick(option.value)"
      >
        <div>
          <h5 class="g-title-quinary">{{ option.name }}</h5>
        </div>
      </li>
    </ul>

    <hr>
  </section>
</template>

<script>
export default {
  name: "MaterialSelectField",
  props: {
    canChange: {
      type: Boolean
    },
    form: {
      type: Object,
      required: true,
    },
    surfaceMaterial: {
      type: Object,
      required: true,
    }
  },
  emits: ['onClick'],
  methods: {
    onClick(value) {
      this.$emit('onClick', {
        surface_material: value,
      });
    }
  }
}
</script>

<style>

</style>
