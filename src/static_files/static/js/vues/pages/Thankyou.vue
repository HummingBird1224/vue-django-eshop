<template>
	<div class="p-billing p-billing--complete" v-if="isInitialized">
    <div class="p-billingMessage">
      <div class="p-billingMessage-body">
        <div class="p-billingMessage-top">
          <span class="p-billingMessage-checkIcon">
              <i class="material-icons">done</i>
          </span>
          <h2 class="g-title-secondary">ご注文が完了しました</h2>
        </div>
        <p v-if="thankyou.transaction.type == 'credit_card'">
          まだ配送日は確定しておりません。データ入稿に移りましょう。<br>
          データの確定後、製造を開始します。
          <small>※通常データの入稿が完了後、納期が決定されます</small>
        </p>
        <p v-if="thankyou.transaction.type == 'bank_transfer'">
          まだ製造は確定しておりません。<br>
          【お支払】と【データ入稿】が完了次第、製造を開始します。
          <small>※お振り込み情報は送信したメールをご確認ください</small>
        </p>
        <p v-if="thankyou.has_design_necessary_item" class="p-billingMessage-red">
          デザイン入稿が不要な商品が含まれています。<br>
          デザイン不要商品に関しては手配が完了し次第発送させていただきます。
        </p>
        <div class="p-billingMessage-buttons">
          <a class="c-btn c-btn--primary" href="/orders/history">データ入稿へ</a>
          <a class="c-btn" href="https://same-raft-469.notion.site/canal-50e2a7a156fc4ae498e277996313e977" target="_blank">データ作成ガイドへ</a>
        </div>
      </div>

      <div class="p-billingMessage-flow">
        <h3 class="g-title-tertiary">この後の流れ</h3>

        <div class="p-billingMessage-flow-graph">
          <div class="p-billingMessage-flow-graph-item">
            <img :src="`${staticUrl}img/billing/thankyou/ic_templaete.png`" alt="">
            <p>01</p>
            <p>データ作成</p>
          </div>
          <div class="p-billingMessage-flow-graph-item p-billingMessage-flow-graph-item--arrow">
            <img :src="`${staticUrl}img/billing/thankyou/ic_arrow.png`" alt="">
          </div>
          <div class="p-billingMessage-flow-graph-item">
            <img :src="`${staticUrl}img/billing/thankyou/ic_upload.png`" alt="">
            <p>02</p>
            <p>入稿</p>
          </div>
          <div class="p-billingMessage-flow-graph-item p-billingMessage-flow-graph-item--arrow">
            <img :src="`${staticUrl}img/billing/thankyou/ic_arrow.png`" alt="">
          </div>
          <div class="p-billingMessage-flow-graph-item">
            <img :src="`${staticUrl}img/billing/thankyou/ic_calender.png`" alt="">
            <p>03</p>
            <p>配送日確定</p>
          </div>
          <div class="p-billingMessage-flow-graph-item p-billingMessage-flow-graph-item--arrow">
            <img :src="`${staticUrl}img/billing/thankyou/ic_arrow.png`" alt="">
          </div>
          <div class="p-billingMessage-flow-graph-item">
            <img :src="`${staticUrl}img/billing/thankyou/ic_delivery.png`" alt="">
            <p>04</p>
            <p>配送</p>
          </div>
        </div>
      </div>
    </div>

    <div class="p-billingDetail">
      <h3 class="g-title-tertiary p-billingDetail-header">注文内容</h3>

      <div class="p-billingDetail-content">
        <div class="p-billingDetail-body">
          <div class="p-billingAddress">
            <header class="p-billingAddress-header">
              <h3 class="g-title-tertiary">
                <svg>
                  <use xlink:href='#icons-pin_drop'/>
                </svg>
                配送先
              </h3>
            </header>

            <div class="p-billingAddress-content">
              {{ thankyou.delivery_address.name }} 〒{{ thankyou.delivery_address.postal_code }}<br>
              {{ thankyou.delivery_address.full_address }}<br>
              {{ thankyou.delivery_address.tel }}
            </div>
          </div>
          <div class="p-billingPayment">
            <header class="p-billingPayment-header">
              <h3 class="g-title-tertiary">
                <svg>
                  <use xlink:href='#icons-payment'/>
                </svg>
                支払い方法
              </h3>
            </header>

            <div class="p-billingPayment-content">
              <template v-if="thankyou.transaction.type == 'credit_card'">
                <h4 >クレジットカード</h4>
                <p>{{ thankyou.transaction.card.brand }} **** **** **** {{ thankyou.transaction.card.last4 }}</p>
              </template>
              <h4 v-if="thankyou.transaction.type == 'bank_transfer'">銀行振込</h4>
            </div>
          </div>
          <div class="p-billingOrder">
            <h3 class="g-title-tertiary p-CartHeader">注文した商品</h3>
            <ul class="p-CartList">
              <li v-for="item in thankyou.items" :key="item.ref_code" class="p-CartItem">
                <div class="p-CartItemThumb" :style="{'background-image': `url(${item.product_image})`}"></div>
                <div class="p-CartItemBody">
                  <header class="p-CartItemBody-header">
                    <h4 class="g-title-quaternary"><a :href="item.link">{{ item.product_name }}</a></h4>
                    <p>{{ $filters.toPriceFormat(item.prices.total) }}<span>円</span></p>
                  </header>
                  <div class="p-CartItemBody-content">
                    <div class="p-CartItemBody-detail">
                      <h5 class="g-title-quinary">サイズ</h5>
                      <p>{{ item.size }}</p>
                    </div>
                    <div v-for="(value, key) in item.extra_info_str" :key="key" class="p-CartItemBody-detail">
                      <h5 class="g-title-quinary">{{ key }}</h5>
                      <p>{{ value }}</p>
                    </div>
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </div>

        <div class="p-billingDetail-price">
          <div class="p-CartPriceTotal">
            <h4 class="g-title-quaternary p-CartPriceTotal-title">合計</h4>
            <p class="p-CartPriceTotal-body">{{ $filters.toPriceFormat(thankyou.prices.total) }}<span class="p-CartPrice-unit">円</span></p>
          </div>
          <div class="p-CartPriceDetail">
            <div class="p-CartPriceDetail-col">
              <h4 class="g-title-quaternary p-CartPriceDetail-title">商品合計</h4>
              <p class="p-CartPriceDetail-body">{{ $filters.toPriceFormat(thankyou.prices.product_total) }}<span class="p-CartPrice-unit">円</span></p>
            </div>

            <div class="p-CartPriceDetail-col">
              <h4 class="g-title-quaternary p-CartPriceDetail-title">版代</h4>
              <p class="p-CartPriceDetail-body">{{ $filters.toPriceFormat(thankyou.prices.plate_price) }}<span class="p-CartPrice-unit">円</span></p>
            </div>

            <div v-if="thankyou.prices.mold_price != 0" class="p-CartPriceDetail-col">
              <h4 class="g-title-quaternary p-CartPriceDetail-title">木型代</h4>
              <p class="p-CartPriceDetail-body">{{ $filters.toPriceFormat(thankyou.prices.mold_price) }}<span class="p-CartPrice-unit">円</span></p>
            </div>

            <div class="p-CartPriceDetail-col">
              <h4 class="g-title-quaternary p-CartPriceDetail-title">配送料</h4>
              <p class="p-CartPriceDetail-body">{{ $filters.toPriceFormat(thankyou.prices.shipping_price) }}<span class="p-CartPrice-unit">円</span></p>
            </div>

            <div class="p-CartPriceDetail-col">
              <h4 class="g-title-quaternary p-CartPriceDetail-title">消費税</h4>
              <p class="p-CartPriceDetail-body">{{ $filters.toPriceFormat(thankyou.prices.tax) }}<span class="p-CartPrice-unit">円</span></p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import { computed } from "vue";
import { useStore } from "../providers/useStore";

export default {
  name: 'Thankyou',
  setup() {

    // providers
    const { store, state } = useStore();

    // computed
    const isInitialized = computed(()=>state.isInitialized);
    const staticUrl = computed(()=>state.staticUrl);
    const thankyou = computed(()=>state.thankyou);

    store.init();

    return {
      isInitialized,
      staticUrl,
      thankyou,
    }
  }
}
</script>

<style scoped>

</style>
