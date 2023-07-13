<template>
  <div class="p-account">
    <header class="p-account-title">
      <h1>
        お届け先の追加・削除&#x1f69a;
      </h1>
    </header>
    <main class="p-account-main">
      <div class="p-account-dataList">
        <div class="p-account-dataList-data" v-for="(address, i) in addresses" :key="address.id">
          <div class="p-account-dataList-data-header">
            <h5 class="g-title-quinary">
              配送先{{ i+1 }}
              <span v-if="address.is_default" class="p-account-dataList-data-header-defaultBadge">デフォルト</span>
            </h5>
            <a class="c-textLink c-textLink--black" :class="{ 'is-loading': currentLoadingId === address.id }" href="#" @click.prevent.stop="() => deleteAddress(address.id)">削除</a>
          </div>
          <div class="p-account-dataList-data-body">
            <div>
              <p>{{ address.name }}</p>
              <p>〒{{ address.postal_code + ' ' + address.address }}</p>
              <p>{{ address.tel }}</p>
            </div>
            <a v-if="!address.is_default" class="c-textLink c-textLink--black" :class="{ 'is-loading': currentLoadingId === address.id }" href="#" @click.prevent.stop="() => changeAddress(address.id)">デフォルトにする</a>
          </div>
        </div>
        <button class="c-btn c-btn--primary" @click.prevent.stop="openModal">お届け先を新規登録する</button>
        <p>※出荷待ちのご注文のお届け先は変更・削除できません。</p>
      </div>
    </main>
    <AddressFormModal
      :isShow="isOpeningModal"
      @close="closeModal"
    />
  </div>
</template>

<script>

import AddressFormModal from "../../components/account/AddressFormModal";
import { useModal } from "../../providers/useModal";
import { useStore } from "../../providers/useStore";
import { ref, computed, onMounted } from 'vue';


export default {
  name: 'AccountAddressManage',
  components: { AddressFormModal },
  setup() {

    // data
    const currentLoadingId = ref(null);

    // providers
    const { store, state } = useStore();

    // computed
    const staticUrl = computed(()=>state.staticUrl);
    const addresses = computed(()=>state.addresses);

    // methods
    const deleteAddress = async (id) => {
      currentLoadingId.value = id;
      await store.deleteAddress({id});
      state.addresses = state.addresses.filter(card => card.id !== id);
      await store.loadAddresses();
      currentLoadingId.value = null;
    }

    const changeAddress = async (id) => {
      currentLoadingId.value = id
      await store.changeAddress({id})
      state.addresses.forEach(card => {
        card.is_default = card.id === id
      })
      currentLoadingId.value = null;
    }

    onMounted(async () => {
      await store.loadAddresses();
    })

    return {
      currentLoadingId,
      staticUrl,
      addresses,
      deleteAddress,
      changeAddress,
      state,
      ...useModal()
    }
  }
}
</script>

<style scoped>

</style>
