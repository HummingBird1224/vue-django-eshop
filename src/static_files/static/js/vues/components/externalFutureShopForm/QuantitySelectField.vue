<template>
  <section
    class="p-externalFutureShopProducts-product-content-purchase-quantity"
    :class="{
      'p-externalFutureShopProducts-product-content-purchase--disabled': !canChange
    }"
  >
    <h4 class="g-title-quaternary">注文数を選択</h4>
    <ul class="p-externalFutureShopProducts-product-content-purchase-options">
      <li
        v-for="option in quantity.items"
        :key="option.position"
        class="p-externalFutureShopProducts-product-content-purchase-options-option p-externalFutureShopProducts-product-content-purchase-options-option--sm"
        :class="{
          'p-externalFutureShopProducts-product-content-purchase-options-option--selected': option.value === form.quantity
        }"
        @click.prevent.stop="onClick(option.value)"
      >
        <div>
          <h5 class="g-title-quinary">{{ option.name }}<span class="p-externalFutureShopProducts-product-content-purchase-options-unit">{{ quantity.unit }}</span></h5>
          <p
            v-if="priceList && priceList[option.value]"
          >{{ $filters.toPriceFormat(priceList[option.value]) }}円</p>
        </div>
      </li>
    </ul>

    <hr>
  </section>
</template>

<script>

export default {
  name: "QuantitySelectField",
  props: {
    canChange: {
      type: Boolean
    },
    form: {
      type: Object,
      required: true,
    },
    quantity: {
      type: Object,
      required: true,
    },
    priceList: {
      type: Object,
    }
  },
  emits: ['onClick'],
  methods: {
    onClick(value) {
      this.$emit('onClick', {
        quantity: value,
      });
    }
  }
}
</script>

<style>

</style>
