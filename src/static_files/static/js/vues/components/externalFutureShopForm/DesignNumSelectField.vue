<template>
  <section
    class="p-externalFutureShopProducts-product-content-purchase-printarea"
    :class="{
      'p-externalFutureShopProducts-product-content-purchase--disabled': !canChange
    }"
  >
    <h4 class="g-title-quaternary">印刷するデザイン数の選択</h4>
    <ul class="p-externalFutureShopProducts-product-content-purchase-options">
      <li
        v-for="option in designNum.items"
        :key="option.position"
        class="p-externalFutureShopProducts-product-content-purchase-options-option p-externalFutureShopProducts-product-content-purchase-options-option--sm"
        :class="{
          'p-externalFutureShopProducts-product-content-purchase-options-option--selected': option.value === form.design_num
        }"
        @click.prevent.stop="onClick(option.value)"
      >
        <div>
          <h5 class="g-title-quinary">{{ option.name.replace( /つ/g , '' ) }}<span class="p-externalFutureShopProducts-product-content-purchase-options-unit">つ</span></h5>
        </div>
      </li>
    </ul>

    <hr>
  </section>
</template>

<script>
export default {
  name: "DesignNumSelectField",
  props: {
    canChange: {
      type: Boolean
    },
    form: {
      type: Object,
      required: true,
    },
    designNum: {
      type: Object,
      required: true,
    }
  },
  methods: {
    onClick(value) {
      this.$emit('onClick', {
        design_num: value,
      });
    }
  }
}
</script>

<style>

</style>
