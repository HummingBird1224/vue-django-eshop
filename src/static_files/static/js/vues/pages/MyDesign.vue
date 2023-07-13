<template>
  <div class="p-mydesign">
    <div class="contents">
      <div class="contents-header">
        <h1>マイデザイン</h1>
        <span>マイデザインの商品をクリックすると、再注文が簡単に行えます。</span>
      </div>
      <ul class="mydesign-list">
        <li v-for="(mydesign, i) in myDesigns" :key="i">
          <div class="mydesign-wrapper">
            <div class="mydesign-photo" @click="showReorderModal(mydesign)" :style="{ backgroundImage: `url(${mydesign.image})` }">
            </div>
            <div class="mydesign-name-editable" @click="startEditAt(i)">
              <label v-if="shouldShowLabel(i)" class="mydesign-name"> {{ mydesign.name || mydesign.product_name }} </label>
              <input type="text" :ref="'tb' + i" v-show="!shouldShowLabel(i)" v-on:keyup.enter="e=>endEditAt(e,i, false)" @blur="e=>endEditAt(e,i, true)"/>
              <svg class="edit-icon" >
                <use xlink:href="#icons-edit" />
              </svg>
            </div>
            <span class="size-label"> {{ mydesign.size }} </span>
          </div>
        </li>
      </ul>
    </div>
    <ReorderMyDesignModal :isShow="isDesignSelected && isShowingReorderModal" @close="closeReorderModal"  @addCart="addCartFromModal" @purchase="showQuickOrderConfirmModal"></ReorderMyDesignModal>
    <QuickOrderConfirmModal :isShow="isDesignSelected && isShowingQuickOrderConfirmModal" @close="closeQuickOrderConfirmModal"></QuickOrderConfirmModal>
  </div>
</template>

<script>
import ReorderMyDesignModal from '../components/myDesign/ReorderMyDesignModal.vue';
import QuickOrderConfirmModal from '../components/myDesign/QuickOrderConfirmModal.vue';
import 'regenerator-runtime';
import { nextTick } from 'vue';

export default {
  name: 'MyDesign',
  data: () => ({
    isHoverPackage: {},
    isEditing: false,
    editingIndex: 0,
  }),
  components: { ReorderMyDesignModal, QuickOrderConfirmModal },
  computed: {
    staticUrl() {
      return this.state.staticUrl;
    },
    isShowingReorderModal() {
      return this.state.isShowingReorderModal;
    },
    isShowingQuickOrderConfirmModal() {
      return this.state.isShowingQuickOrderConfirmModal;
    },
    myDesigns() {
      return this.state.loadedMyDesigns;
    },
    isDesignSelected() {
      return this.state.selectedDesign != null;
    },
    isQuickOrderSelected() {
      return this.state.instantBuyResnpose != null;
    },
    state() {
      return this.store.state;
    }
  },
  methods: {
    startEditAt(i) {
      if (this.isEditing) {
        this.$refs[`tb${i}`].blur()
      }

      this.editingIndex = i;
      this.isEditing = true;
      nextTick(()=> {
        this.$refs[`tb${i}`].value = this.state.loadedMyDesigns[i].name;
        this.$refs[`tb${i}`].focus()
      })
    },
    async endEditAt(e, i, isForced) {
      this.isEditing = false;
      if (isForced) return
      const design = this.state.loadedMyDesigns[i];
      await this.updateDesignName(design.id, e.target.value)
    },
    shouldShowLabel(idx) {
      if (!this.isEditing) {
        return true;
      }

      return this.editingIndex != idx;
    },
    async showReorderModal(design) {
      await this.store.fetchReorderDetail(design.id);
      this.store.selectDesign(design);
      await this.store.estimateOrder();

      nextTick(()=>{
        this.store.showReorderModal();
      })
    },
    closeReorderModal() {
      this.store.deselectDesign();
      this.store.closeReorderModal();
    },
    async showQuickOrderConfirmModal() {
      this.store.closeReorderModal();
      this.store.showQuickOrderConfirmModal();
    },
    closeQuickOrderConfirmModal() {
      this.store.closeQuickOrderConfirmModal();
    },
    async updateDesignName(designId, name) {
      await this.store.updateMyDesignName(designId, name);
    },
    async addCartFromModal() {
      await this.store.addCart();
      this.store.closeReorderModal();
      location.href= "/cart/"
    }
  },
  async mounted() {
    await this.store.getMyDesigns();
    await this.store.fetchAddressList();
    await this.store.fetchCreditCardList();
  }
}
</script>

<style scoped>
</style>
