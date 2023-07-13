<template>
  <header class="p-Header">
    <h2 class="g-title-secondary p-Header-title">{{ title }}</h2>
    <p class="p-Header-body">選んだ項目によって値段が変化します。注文したい商品の詳細を選びましょう。</p>
  </header>
</template>

<script>
import StoreMixin from "../../../mixins/StoreMixin";
import EstimateFlow from "../../../../constants/EstimateFlow";

export default {
  name: "Header",
  mixins: [StoreMixin],
  computed: {
    flow() {
      return this.state.flow;
    },
    title() {
      switch (this.flow) {
        case EstimateFlow.CARD_BOARD_PROCESS:
          return '加工の追加';
        case EstimateFlow.COLOR:
          return '印刷に使用する色数の選択';
        case EstimateFlow.FLAT_BAG_MATERIAL:
          return '材質の選択';
        case EstimateFlow.FLAT_BAG_PROCESS:
          return '加工の追加';
        case EstimateFlow.PAPER_BOX_BOTTOM:
          return '底の選択';
        case EstimateFlow.PAPER_BOX_ROUGHNESS:
          return '凹凸加工の追加';
        case EstimateFlow.PAPER_BOX_SPECIAL_PRINT:
          return '特殊印刷加工の追加';
        case EstimateFlow.PRINT_AREA:
          return '印刷する面数の選択';
        case EstimateFlow.SURFACE:
          return '素材の選択';
        default:
          return '見積もり / 購入';
      }
    }
  }
}
</script>

<style scoped>

</style>
