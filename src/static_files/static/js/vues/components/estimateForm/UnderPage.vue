<template>
  <div>
    <PageBackButton
      @onClick="onClickPageBack"
    />

    <Header/>

    <template
      v-if="product"
    >
      <BottomPage
        v-if="flow === EstimateFlow.BOTTOM"
      />
      <ColorPage
        v-else-if="flow === EstimateFlow.COLOR"
      />
      <EmbossPage
        v-else-if="flow === EstimateFlow.EMBOSS"
      />
      <FlatBagMaterialPage
        v-else-if="flow === EstimateFlow.FLAT_BAG_MATERIAL"
      />
      <PrintAreaPage
        v-else-if="flow === EstimateFlow.PRINT_AREA"
      />
      <ProcessPage
        v-else-if="flow === EstimateFlow.PROCESS"
      />
      <SpecialPrintPage
        v-else-if="flow === EstimateFlow.SPECIAL_PRINT"
      />
      <SurfacePage
        v-else-if="flow === EstimateFlow.SURFACE"
      />
      <Footer/>
    </template>
  </div>
</template>

<script>
import PageBackButton from "./PageBackButton.vue";
import Header from "./under/Header.vue";
import Footer from "./under/Footer";
import ColorPage from "./under/ColorPage";
import FlatBagMaterialPage from "./under/FlatBagMaterialPage";
import ProcessPage from "./under/ProcessPage";
import BottomPage from "./under/BottomPage";
import PrintAreaPage from "./under/PrintAreaPage";
import EmbossPage from "./under/EmbossPage";
import SpecialPrintPage from "./under/SpecialPrintPage";
import EstimateFlow from "../../../constants/EstimateFlow";
import StoreMixin from "../../mixins/StoreMixin";
import SurfacePage from "./under/SurfacePage";

export default {
  name: "UnderPage",
  mixins: [StoreMixin],
  components: {
    ProcessPage,
    SurfacePage,
    SpecialPrintPage,
    EmbossPage,
    PrintAreaPage,
    BottomPage,
    FlatBagMaterialPage,
    ColorPage, Footer, Header, PageBackButton
  },
  data: () => ({
    EstimateFlow
  }),
  computed: {
    product() {
      return this.state.product;
    },
    flow() {
      return this.state.flow;
    }
  },
  methods: {
    onClickPageBack() {
      this.state.flow = EstimateFlow.TOP;
    }
  }
}
</script>

<style scoped>

</style>
