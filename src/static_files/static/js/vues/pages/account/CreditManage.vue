<template>
  <div class="p-account">
    <header class="p-account-title">
      <h1>
        クレジットカードの追加・削除&#x1f4b3;
      </h1>
    </header>
    <main class="p-account-main">
      <div class="p-account-dataList">
        <div v-if="cards.length > 0" class="p-account-dataList-data" v-for="card in cards" :key="card.id">
          <div class="p-account-dataList-data-header">
            <h5 class="g-title-quinary">
              現在登録されているクレジットカード情報
              <span v-if="card.is_default" class="p-account-dataList-data-header-defaultBadge">デフォルト</span>
            </h5>
            <a class="c-textLink c-textLink--black" :class="{ 'is-loading': nowLoading === card.id }" href="#" @click.prevent.stop="() => deleteCredit(card.id)">削除</a>
          </div>
          <div class="p-account-dataList-data-body">
            <div>
              <p><span class="p-account-dataList-data-body-cardLogo" v-if="cardBrandImages[card.brand]" v-html="cardBrandImages[card.brand]" />****-****-****-{{ card.last4 }}</p>
              <p>{{ card.name }}</p>
              <p>{{ card.exp_year }}年{{ card.exp_month }}月</p>
            </div>
            <a v-if="!card.is_default" class="c-textLink c-textLink--black" :class="{ 'is-loading': nowLoading === card.id }" href="#" @click.prevent.stop="() => changeCredit(card.id)">デフォルトにする</a>
          </div>
        </div>
        <button class="c-btn c-btn--primary" @click.prevent.stop="openModal">利用規約に同意してクレジットカードを追加する</button>
      </div>
    </main>
    <CreditFormModal
      :isShow="isOpeningModal"
      @close="closeModal"
    />
  </div>
</template>

<script>

import CreditFormModal from "../../components/account/CreditFormModal";
import { useModal } from "../../providers/useModal";
import { useStore } from "../../providers/useStore";
import { ref, computed, onBeforeMount } from 'vue';

export default {
  name: 'AccountCreditManage',
  components: {CreditFormModal},
  setup() {
    // data
    const currentLoadingId = ref(null);

    // providers
    const { store, state } = useStore();

    // computed
    const staticUrl = computed(()=> state.staticUrl);
    const cards = computed(()=> state.cards);
    const cardBrandImages = computed(()=> {
      const staticUrlValue = staticUrl.value
      return {
        Visa: `<img src="${staticUrlValue}img/card_logos/icon_visa.png">`,
        MasterCard: `<img src="${staticUrlValue}img/card_logos/icon_mastercard.png">`,
        'American Express': `<img src="${staticUrlValue}img/card_logos/icon_americanexpress.png">`,
        'Diners Club': `<img src="${staticUrlValue}img/card_logos/icon_dinersclub.png">`,
        JCB: `<img src="${staticUrlValue}img/card_logos/icon_jcb.png">`,
        Discover: `<img src="${staticUrlValue}img/card_logos/icon_discover.png">`,
      }
    })

    // methods
    const deleteCredit = async (id) => {
      currentLoadingId.value = id;
      await store.deleteCredit({id});
      state.cards = state.cards.filter(card => card.id !== id);
      await store.loadCredits();
      currentLoadingId.value = null;
    }

    const changeCredit = async (id) => {
      currentLoadingId.value = id
      await store.changeCredit({id})
      state.cards.forEach(card => {
        card.is_default = card.id === id
      })
      currentLoadingId.value = null;
    }

    onBeforeMount(async ()=>await store.loadCredits())


    return {
      currentLoadingId,
      staticUrl,
      cards,
      cardBrandImages,
      deleteCredit,
      changeCredit,
      state,
      ...useModal()
    }
  }
}
</script>

<style scoped>

</style>
