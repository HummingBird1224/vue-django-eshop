<template>
  <section
    class="p-externalFutureShopProducts-product-content-purchase-size"
    :class="{
      'p-externalFutureShopProducts-product-content-purchase--disabled': !canChange
    }"
  >
    <h4 class="g-title-quaternary">サイズを選択（単位mm）</h4>
    <ul class="p-externalFutureShopProducts-product-content-purchase-options">
      <li
        v-for="option in size.items"
        :key="option.position"
        class="p-externalFutureShopProducts-product-content-purchase-options-option p-externalFutureShopProducts-product-content-purchase-options-option--lg"
        :class="{
          'p-externalFutureShopProducts-product-content-purchase-options-option--selected': option.value === form.size
        }"
        :style="{
          'background-image': `url(${option.image})`
        }"
        @click.prevent.stop="onClick(option.value)"
      >
        <div>
          <h5 class="g-title-quinary">{{ option.name.replace(/サイズ/g, '') }}</h5>
          <p
            v-if="option.name.indexOf('サイズ') !== -1"
          >サイズ</p>
        </div>
      </li>
    </ul>

    <hr>
  </section>
</template>

<script>
export default {
  name: "SizeSelectField",
  props: {
    canChange: {
      type: Boolean
    },
    form: {
      type: Object,
      required: true,
    },
    size: {
      type: Object,
      required: true,
    }
  },
  emits: ['onClick'],
  methods: {
    onClick(value) {
      this.$emit('onClick', {
        size: value,
      });
    }
  }
}
</script>

<style>

</style>
