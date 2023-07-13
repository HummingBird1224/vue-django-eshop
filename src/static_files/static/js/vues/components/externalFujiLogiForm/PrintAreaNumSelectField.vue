<template>
  <section
    class="p-externalFujiLogiProducts-product-content-purchase-printarea"
    :class="{
      'p-externalFujiLogiProducts-product-content-purchase--disabled': !canChange
    }"
  >
    <h4 class="g-title-quaternary">印刷面数を選択</h4>
    <ul class="p-externalFujiLogiProducts-product-content-purchase-options">
      <li
        v-for="option in printAreaNum.items"
        :key="option.position"
        class="p-externalFujiLogiProducts-product-content-purchase-options-option p-externalFujiLogiProducts-product-content-purchase-options-option--sm"
        :class="{
          'p-externalFujiLogiProducts-product-content-purchase-options-option--selected': option.value === form.print_area_num
        }"
        @click.prevent.stop="onClick(option.value)"
      >
        <div>
          <h5 class="g-title-quinary">{{ option.name.replace( /面/g , '' ) }}<span class="p-externalFujiLogiProducts-product-content-purchase-options-unit">面</span></h5>
        </div>
      </li>
    </ul>

    <hr>
  </section>
</template>

<script>
export default {
  name: "PrintAreaNumSelectField",
  props: {
    canChange: {
      type: Boolean
    },
    form: {
      type: Object,
      required: true,
    },
    printAreaNum: {
      type: Object,
      required: true,
    }
  },
  emits: ['onClick'],
  methods: {
    onClick(value) {
      this.$emit('onClick', {
        print_area_num: value,
      });
    }
  }
}
</script>

<style>

</style>
