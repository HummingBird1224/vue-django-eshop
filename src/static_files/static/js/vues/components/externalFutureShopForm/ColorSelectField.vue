<template>
  <section
    class="p-externalFutureShopProducts-product-content-purchase-printarea"
    :class="{
      'p-externalFutureShopProducts-product-content-purchase--disabled': !canChange
    }"
  >
    <h4 class="g-title-quaternary">色数を選択</h4>
    <ul class="p-externalFutureShopProducts-product-content-purchase-options">
      <li
        v-for="option in colorNum.items"
        :key="option.position"
        class="p-externalFutureShopProducts-product-content-purchase-options-option p-externalFutureShopProducts-product-content-purchase-options-option--sm"
        :class="{
          'p-externalFutureShopProducts-product-content-purchase-options-option--selected': option.value === form.color_num
        }"
        @click.prevent.stop="onClick(option.value)"
      >
        <div>
          <h5 class="g-title-quinary">{{ option.name.replace( /色/g , '' ) }}<span v-if="option.value > 0" class="p-externalFutureShopProducts-product-content-purchase-options-unit">色</span></h5>
        </div>
      </li>
    </ul>

    <hr>
  </section>
</template>

<script>
export default {
  name: "ColorSelectField",
  props: {
    canChange: {
      type: Boolean
    },
    form: {
      type: Object,
      required: true,
    },
    colorNum: {
      type: Object,
      required: true,
    }
  },
  emits: ['onClick'],
  methods: {
    onClick(value) {
      this.$emit('onClick', {
        color_num: value,
      });
    }
  }
}
</script>

<style>

</style>
