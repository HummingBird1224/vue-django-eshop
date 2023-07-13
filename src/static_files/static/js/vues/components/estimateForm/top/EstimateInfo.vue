<template>
  <div class="p-Product">
    <header class="p-Product-header">
      <div
        class="p-Product-thumb"
        :style="{
          'background-image': `url(${product.thumbnail})`
        }"
      ></div>
      <div class="p-Product-content">
        <span class="p-Product-label">選択中の商品</span>
        <h3 class="g-title-tertiary p-Product-title">{{ product.name }}</h3>
      </div>
    </header>
    <div class="p-Product-main">
      <ul class="p-ProductInfoList">
        <li class="p-ProductInfo">
          <h4 class="g-title-quaternary">サイズ</h4>
          <p>{{ sizeValue }}</p>
        </li>
        <li class="p-ProductInfo">
          <h4 class="g-title-quaternary">注文数</h4>
          <p>{{ quantityValue }}</p>
        </li>
        <li
          v-if="surfaceHtml"
          v-html="surfaceHtml"
          class="p-ProductInfo"
        >
        </li>
        <li
          v-if="printAreaHtml"
          v-html="printAreaHtml"
          class="p-ProductInfo"
        >
        </li>
        <li
          v-if="colorHtml"
          v-html="colorHtml"
          class="p-ProductInfo"
        >
        </li>
        <li
          v-if="materialHtml"
          v-html="materialHtml"
          class="p-ProductInfo"
        >
        </li>
        <li
          v-if="processHtml"
          v-html="processHtml"
          class="p-ProductInfo"
        >
        </li>
        <li
          v-if="bottomHtml"
          v-html="bottomHtml"
          class="p-ProductInfo"
        >
        </li>
        <li
          v-if="embossHtml"
          v-html="embossHtml"
          class="p-ProductInfo"
        >
        </li>
        <li
          v-if="specialPrintHtml"
          v-html="specialPrintHtml"
          class="p-ProductInfo"
        >
        </li>
      </ul>
      <EstimateInfoFooter/>
    </div>
  </div>
</template>

<script>
import StoreMixin from "../../../mixins/StoreMixin";
import EstimateInfoFooter from "./EstimateInfoFootetr";
import EstimateProductCategory from "../../../../constants/EstimateProductCategory";

export default {
  name: "EstimateInfo",
  components: {EstimateInfoFooter},
  mixins: [StoreMixin],
  computed: {
    product() {
      return this.state.product;
    },
    extraInfo() {
      return this.product.extra_info;
    },
    productCategory() {
      return this.state.productCategory;
    },
    form() {
      return this.state.form;
    },
    sizeValue() {
      const selected = this.extraInfo.size.options[this.form.size];

      if (selected) {
        return `${selected.name} ${selected.value.map(x => x.value).join(' x ')} mm`;
      } else if (this.form.freeSize) {
        return `${Object.entries(this.form.freeSize).map(x => x[1]).join(' x ')} mm`;
      }

      return '';
    },
    quantityValue() {
      return $filters.toPriceFormat(this.form.quantity);
    },
    colorHtml() {
      const colorNum = this.store.selectColorInfo();

      if (!colorNum) {
        return '';
      }

      const selected = colorNum.options[this.form.color_num];
      return selected ? `<h4>色数</h4><p>${selected.name}</p>` : '';
    },
    materialHtml() {
      const material = this.store.selectMaterialInfo();

      if (!material) {
        return '';
      }

      const selected = material.options[this.form.material];
      return selected ? `<h4>材質</h4><p>${selected.name}</p>` : '';
    },
    processHtml() {
      const processValue = this.store.getProcessValueStr(this.form);
      return processValue ? `<h4>加工</h4><p>${processValue}</p>` : '';
    },
    surfaceHtml() {
      const surfaceValue = this.store.getSurfaceValueStr(this.form);
      return surfaceValue ? `<h4>表面</h4><p>${surfaceValue}</p>` : '';
    },
    printAreaHtml() {
      switch (this.productCategory) {
        case EstimateProductCategory.CARD_BOARD:
          return `<h4>印刷面数</h4><p>外面 ${this.form.print_area.outside.length}</p>`;
        case EstimateProductCategory.PAPER_BOX:
          return `<h4>印刷面数</h4><p>外面 ${this.form.print_area.outside.length} / 内面 ${this.form.print_area.inside.length}</p>`;
        default:
          return '';
      }
    },
    bottomHtml() {
      const bottom = this.store.selectBottomInfo();

      if (!bottom) {
        return '';
      }

      const selected = bottom.options[this.form.bottom];
      return selected ? `<h4>底</h4><p>${selected.name}</p>` : '';
    },
    embossHtml() {
      const emboss = this.store.selectEmbossInfo();

      if (!emboss) {
        return '';
      }

      const selected = emboss.options[this.form.emboss];
      return selected ? `<h4>凹凸加工</h4><p>${selected.name}</p>` : '';
    },
    specialPrintHtml() {
      const specialPrint = this.store.selectSpecialPrintInfo();

      if (!specialPrint) {
        return '';
      }

      const selected = specialPrint.options[this.form.special_print];
      return selected ? `<h4>特殊印刷</h4><p>${selected.name}</p>` : '';
    }
  }
}
</script>

<style scoped>

</style>
