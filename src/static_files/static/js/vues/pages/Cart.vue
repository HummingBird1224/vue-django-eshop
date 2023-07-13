<template>
	<div class="p-cart" v-if="isInitialized">
		<div class="p-cartWrapper">
			<div class="p-cartHeader">
				<h2 class="g-title-secondary">カート</h2>
        <div class="p-cartHeader-nav">
          <ul>
            <li class="selected">1. ショッピングカート</li>
            <li>2. 配送先＆お支払い情報</li>
            <li>3. ご購入内容の/確定</li>
            <li>4. デザインデータの入稿</li>
          </ul>
        </div>
			</div>

      <div v-if="!cart || cart.num_items == 0" class="p-cartEmpty">
        <img :src="staticUrl + 'img/cart.png'" />
        <p>カートが空です</p>
        <a href="/catalog/flatbag"><button class="c-btn c-btn--primary">商品一覧へ</button></a>
      </div>

      <div v-else class="p-cartContainer">
        <ol class="p-cartList">
          <li class="p-cartItem" v-for="item in cart.items" :key="item.id">

            <div class="p-cartItemThumb">
              <img :src="item.product_image" alt="">
            </div>

            <div class="p-cartItemContent">
              <header>
                <h5 class="g-title-quinary p-cartItemContent-title">
                  <a class="c-textLink" :href="item.product_url">{{ item.product_name }}</a>
                  <p><small>サイズ：　{{ item.size_str }}</small></p>
                </h5>
              </header>

              <div class="p-cartItemContent-rowContainer">
                <div class="p-cartItemContent-row">
                  <div class="p-cartItemProductInfo" v-for="(value, key) in item.extra_info_str" :key="key">
                    <h6 class="g-title-quinary">{{ key }}</h6>
                    <p>{{ value }}</p>
                  </div>
                </div>

                <div class="p-cartItemContent-row">
                  <div class="p-cartItemProductInfo">
                    <h6 class="g-title-quinary">商品合計</h6>
                    <p>{{ $filters.toPriceFormat(item.prices.product_total) }}円</p>
                  </div>
                  <div class="p-cartItemProductInfo">
                    <h6 class="g-title-quinary">版代</h6>
                    <p>{{ $filters.toPriceFormat(item.prices.plate_price) }}円</p>
                  </div>
                  <div class="p-cartItemProductInfo" v-if="item.prices.mold_price != 0">
                    <h6 class="g-title-quinary">木型代</h6>
                    <p>{{ $filters.toPriceFormat(item.prices.mold_price) }}円</p>
                  </div>
                  <div class="p-cartItemProductInfo">
                    <h6 class="g-title-quinary">配送料</h6>
                    <p>{{ $filters.toPriceFormat(item.prices.shipping_price) }}円</p>
                  </div>
                  <div class="p-cartItemProductInfo">
                    <h6 class="g-title-quinary">小計</h6>
                    <p>{{ $filters.toPriceFormat(item.prices.subtotal) }}円</p>
                  </div>
                </div>
              </div>
            </div>

            <div class="p-cartItemPrice">
              <p>{{ $filters.toPriceFormat(item.prices.total) }}<span class="p-cartItemPrice-priceUnit">円(税込)</span>
              <p><span class="p-cartItemPrice-unitPrice">(¥{{ $filters.toPriceFormat(item.prices.unit_price) }}/個)</span></p></p>
            </div>
            <div class="p-cartItemCancel">
              <button class="btn delete-from-cart" @click="deleteCartItem(item.id)">×　削除する</button>
            </div>
          </li>
        </ol>

        <div class="p-cartPrice">
          <div class="p-cartPrice-price">
            <h6 class="g-title-quinary">商品合計</h6>
            <p id="product_total">{{ $filters.toPriceFormat(cart.prices.product_total) }} <span>円</span></p>
          </div>
          <div class="p-cartPrice-price">
            <h6 class="g-title-quinary">版代合計</h6>
            <p id="plate_price">{{ $filters.toPriceFormat(cart.prices.plate_price) }} <span>円</span></p>
          </div>
          <div class="p-cartPrice-price" v-if="cart.prices.mold_price != 0">
            <h6 class="g-title-quinary">木型代合計</h6>
            <p id="mold_price">{{ $filters.toPriceFormat(cart.prices.mold_price) }} <span>円</span></p>
          </div>
          <div class="p-cartPrice-price">
            <h6 class="g-title-quinary">配送料合計</h6>
            <p id="shipping_price">{{ $filters.toPriceFormat(cart.prices.shipping_price) }} <span>円</span></p>
          </div>
          <div class="p-cartPrice-price">
            <h6 class="g-title-quinary">消費税</h6>
            <p id="tax_total">{{ $filters.toPriceFormat(cart.prices.tax) }} <span>円</span></p>
          </div>
          <hr>
          <div class="p-cartPrice-price">
            <h6 class="g-title-quinary">合計（税込）</h6>
            <p id="total">{{ $filters.toPriceFormat(cart.prices.total) }} <span>円</span></p>
          </div>
          <form action="/billing/create-order/" method="POST">
            <input type="hidden" name="csrfmiddlewaretoken" :value="`${csrfToken}`">
            <button class="c-btn c-btn--primary p-cartToBilling-cta" type="submit">
              購入手続きへ進む
            </button>
          </form>
          <small>
            ※ご購入手続きに移る前に、デザインの管理のため会員登録が必要となります。
          </small>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import { computed } from "vue";
import { useStore } from "../providers/useStore";

export default {
  name: "Cart",
  setup() {

    // providers
    const { store, state } = useStore();

    // computed
    const isInitialized = computed(()=>state.isInitialized);
    const csrfToken = computed(()=>state.csrfToken);
    const staticUrl = computed(()=>state.staticUrl);
    const cart = computed(()=>state.cart);

    // methods
    const deleteCartItem = (itemId)=>store.postCartItemDelete(itemId);

    // event hooks
    store.init();

    return {
      isInitialized,
      csrfToken,
      staticUrl,
      cart,
      deleteCartItem
    }
  }
}
</script>

<style scoped>

</style>
