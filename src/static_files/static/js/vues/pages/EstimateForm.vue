<template>
  <div class="p-estimate-wrapper">
    <TopPage
      v-if="flow === EstimateFlow.TOP"
    />
    <UnderPage
      v-else
    />
  </div>
</template>

<script>
import TopPage from "../components/estimateForm/TopPage.vue";
import UnderPage from "../components/estimateForm/UnderPage.vue";
import StoreMixin from "../mixins/StoreMixin";
import EstimateFlow from "../../constants/EstimateFlow";

export default {
  name: "EstimateForm",
  mixins: [StoreMixin],
  components: {TopPage, UnderPage},
  data: () => ({
    EstimateFlow,
  }),
  computed: {
    form() {
      return this.state.form;
    },
    flow() {
      return this.state.flow;
    }
  },
  watch: {
    form: {
      handler: function () {
        this.store.postCalcEstimate();
      },
      deep: true
    },
    flow() {
      // underPageの前回の編集状況をclear.
      this.store.initEditingForm();
    }
  },
  mounted() {
    this.store.getProductInfo();
  }
}
</script>

<style scoped>

</style>
