<template>
  <section
    class="p-externalBaseProducts-product-content-purchase-printarea"
    :class="{
      'p-externalBaseProducts-product-content-purchase--disabled': !canChange
    }"
  >
    <h4 class="g-title-quaternary">印刷色を選択</h4>
    <ul class="p-externalBaseProducts-product-content-purchase-options">
      <li
        v-for="option in colorName.items"
        :key="option.position"
        class="p-externalBaseProducts-product-content-purchase-options-option p-externalBaseProducts-product-content-purchase-options-option--sm"
        :class="{
          'p-externalBaseProducts-product-content-purchase-options-option--selected': option.value === form.color_name
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
  name: "ColorNameSelectField",
  props: {
    canChange: {
      type: Boolean
    },
    form: {
      type: Object,
      required: true,
    },
    colorName: {
      type: Object,
      required: true,
    }
  },
  emits: ['onClick'],
  methods: {
    onClick(value) {
      this.$emit('onClick', {
        color_name: value,
      });
    }
  }
}
</script>

<style>

</style>
