<template>
  <div>
    <div class="breadcrumbsInternal">
      <div class="breadcrumbsItem">ホーム</div>
      <div class="breadcrumbsArrow">></div>
      <div class="breadcrumbsItem">CUSTOM</div>
      <div class="breadcrumbsArrow">></div>
      <div class="breadcrumbsItem">カスタム商品追加</div>
    </div>

    <h1 class="g-title-primary pageTitleInternal">カスタム商品追加</h1>

    <CreateCustomProductForm />
  </div>
</template>

<script>
import CreateCustomProductForm from '../../../components/internal/custom/CreateCustomProduct'
import {useStore} from "../../../providers/useStore";
import {computed} from 'vue';

export default {
  name: 'CreateCustomProductPage',
  components: {CreateCustomProductForm},
  setup() {
    // providers
    const { store, state } = useStore();
    const csrfToken = computed(()=>state.csrfToken);
    store.init();
    return {
      csrfToken
    }
  }
}
</script>

<style scoped>

</style>
