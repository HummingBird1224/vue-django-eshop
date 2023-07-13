<template>
  <div class="p-orderList" v-if="isInitialized" @click="toggleOpenOrderDocumentDropdown()">
    <header class="p-orderListHeader">
      <h2 class="g-title-secondary">注文一覧</h2>
    </header>

    <ol class="p-orderOrderList">
      <li v-for="order in orders.results" :key="order.ref_code" class="p-orderOrder">
        <header class="p-orderOrder-header">
          <div class="p-orderOrder-date">
            <h6 class="g-title-quinary">注文日時</h6>
            <p>{{ dateFormat(order.created_at, 'yyyy年M月d日') }}</p>
          </div>

          <div class="p-orderOrder-info">
            <div class="p-orderOrder-price">
              <h6 class="g-title-quinary">注文合計金額</h6>
              <p>{{ $filters.toPriceFormat(order.prices.total) }} <span>円(税込)</span></p>
            </div>

            <div class="p-orderOrder-deliverTo">
              <h6 class="g-title-quinary">お届け先</h6>
              <a class="c-textLink">
                {{ order.delivery_address.full_address }}
              </a>
            </div>
          </div>
        </header>

        <ul class="p-orderProductList">
          <li v-for="item in order.items" :key="item.ref_code" class="p-orderProduct">
            <header class="p-orderProduct-header">
              <h5 class="g-title-quinary p-orderProduct-title">
                <a class="c-textLink" :href="item.link">{{ item.product_name }}</a>

              </h5>
              <p><small>注文商品番号：{{ item.ref_code }}</small></p>
              <p><small>サイズ：{{ item.size }}</small></p>

              <template v-if="item.state != 'cancelled'">
                <a class="js-open-order-document-menu p-orderProduct-documents" href="#" @click.prevent.stop="toggleOpenOrderDocumentDropdown(item.ref_code)">
                  <span v-if="order.state != 'new'">請求書</span>
                  <span v-if="order.transaction.is_captured">・領収書</span>
                  <span v-if="item.delivery.state == 'delivered'">・納品書</span>
                  <span>&#8250;</span>
                </a>

                <div v-if="state.isOpenOrderDocumentDropdowns[item.ref_code]" class="js-order-document-menu p-orderProduct-documents-dropdown">
                  <ul class="">
                    <li v-if="order.state != 'new'" class="p-orderProduct-documents-dropdown-item">
                      <svg>
                        <use xlink:href='#icons-invoice'></use>
                      </svg>
                      <a :href="`/orders/documents/download/${item.ref_code}/invoice.pdf`">請求書を見る</a>
                    </li>

                    <hr v-if="order.transaction.is_captured">
                    <li v-if="order.transaction.is_captured" class="p-orderProduct-documents-dropdown-item">
                      <svg>
                        <use xlink:href='#icons-receipt'></use>
                      </svg>
                      <a :href="`/orders/documents/download/${item.ref_code}/receipt.pdf`">領収書を見る</a>
                    </li>

                    <hr v-if="item.delivery.state == 'delivered'">
                    <li v-if="item.delivery.state == 'delivered'" class="p-orderProduct-documents-dropdown-item">
                      <svg>
                        <use xlink:href='#icons-delivery_note'></use>
                      </svg>
                      <a :href="`/orders/documents/download/${item.ref_code}/delivery.pdf`">納品書を見る</a>
                    </li>
                  </ul>
                </div>
              </template>

              <p class="p-orderProduct-price">
                {{ $filters.toPriceFormat(item.prices.total) }}<span class="p-orderProduct-priceUnit">円(税込)</span>
                <span class="p-orderProduct-count">（{{ item.prices.unit_price }}円/個）</span>
              </p>

              <ol class="p-orderProduct-flow">
                <template v-if="item.state == 'not_submitted'">
                  <li class="is-current"><span>1.未入稿</span></li>
                  <li><span>2.確認中</span></li>
                  <li><span>3.最終確認</span></li>
                  <li class="u-sp-none"><span>4.印刷/加工</span></li>
                  <li class="u-sp-none"><span>5.配送中</span></li>
                  <li class="u-sp-none"><span>6.配送済み</span></li>
                </template>

                <template v-if="item.state == 'under_check'">
                  <li><span>1.未入稿</span></li>
                  <li class="is-current"><span>2.確認中</span></li>
                  <li><span>3.最終確認</span></li>
                  <li><span>4.印刷/加工</span></li>
                  <li class="u-sp-none"><span>5.配送中</span></li>
                  <li class="u-sp-none"><span>6.配送済み</span></li>
                </template>

                <template v-if="item.state == 'resubmission_request'">
                  <li><span>1.未入稿</span></li>
                  <li><span>2.確認中</span></li>
                  <li class="is-current is-error"><span>3.再入稿依頼</span></li>
                  <li><span>4.印刷/加工</span></li>
                  <li><span>5.配送中</span></li>
                  <li class="u-sp-none"><span>6.配送済み</span></li>
                </template>

                <template v-if="item.state == 'checked'">
                  <li><span>1.未入稿</span></li>
                  <li><span>2.確認中</span></li>
                  <li class="is-current is-ok"><span>3.最終確認</span></li>
                  <li><span>4.印刷/加工</span></li>
                  <li><span>5.配送中</span></li>
                  <li class="u-sp-none"><span>6.配送済み</span></li>
                </template>

                <template v-if="item.state == 'unassigned' || item.state == 'printing'">
                  <li class="u-sp-none"><span>1.未入稿</span></li>
                  <li><span>2.確認中</span></li>
                  <li><span>3.最終確認</span></li>
                  <li class="is-current"><span>4.印刷/加工</span></li>
                  <li><span>5.配送中</span></li>
                  <li><span>6.配送済み</span></li>
                </template>

                <template v-if="item.state == 'shipped'">
                  <li class="u-sp-none"><span>1.未入稿</span></li>
                  <li class="u-sp-none"><span>2.確認中</span></li>
                  <li><span>3.最終確認</span></li>
                  <li><span>4.印刷/加工</span></li>
                  <li class="is-current"><span>5.配送中</span></li>
                  <li><span>6.配送済み</span></li>
                </template>

                <template v-if="item.state == 'delivered'">
                  <li class="u-sp-none"><span>1.未入稿</span></li>
                  <li class="u-sp-none"><span>2.確認中</span></li>
                  <li class="u-sp-none"><span>3.最終確認</span></li>
                  <li><span>4.印刷/加工</span></li>
                  <li><span>5.配送中</span></li>
                  <li class="is-current"><span>6.配送済み</span></li>
                </template>

                <template v-if="item.state == 'cancelled'">
                  <li class="u-sp-none"><span>1.未入稿</span></li>
                  <li class="u-sp-none"><span>2.確認中</span></li>
                  <li class="u-sp-none"><span>3.最終確認</span></li>
                  <li><span>4.印刷/加工</span></li>
                  <li><span>5.配送中</span></li>
                  <li class="is-current is-error"><span>6.キャンセル</span></li>
                </template>

                <span v-if="order.transaction.type == 'bank_transfer' && !order.transaction.is_captured && item.state != 'cancelled'">
                  <li class="is-current is-error"><span>入金待ち</span></li>
                </span>
              </ol>
            </header>

            <div class="p-orderProductDetail">
              <div class="p-orderProductThumb"
                :style="'background-image: url(' + item.product_image + ')'">
              </div>

              <div class="p-orderProductBody">
                <div class="p-orderProductBody-left">
                  <div class="p-orderProductBody-rowContainer">
                    <div class="p-orderProductBody-row">
                      <div v-for="(value, key) in item.extra_info_str" :key="key" class="p-orderProductInfo">
                        <h6 class="g-title-quinary">{{ key }}</h6>
                        <p>{{ value }}</p>
                      </div>

                      <div class="p-orderProductInfo">
                        <h6 class="g-title-quinary">出荷予定日</h6>
                        <p v-if="item.delivery.shipping_date">{{ item.delivery.shipping_date }}</p>
                        <p v-else>確定次第ご連絡します</p>
                      </div>
                    </div>

                    <div class="p-orderProductBody-row">
                      <div class="p-orderProductInfo">
                        <h6 class="g-title-quinary">商品合計</h6>
                        <p>{{ $filters.toPriceFormat(item.prices.product_total) }}円</p>
                      </div>
                      <div class="p-orderProductInfo">
                        <h6 class="g-title-quinary">版代</h6>
                        <p>{{ $filters.toPriceFormat(item.prices.plate_price) }}円</p>
                      </div>
                      <div v-if="item.prices.mold_price != 0" class="p-orderProductInfo">
                        <h6 class="g-title-quinary">木型代</h6>
                        <p>{{ $filters.toPriceFormat(item.prices.mold_price) }}円</p>
                      </div>
                      <div class="p-orderProductInfo">
                        <h6 class="g-title-quinary">配送料</h6>
                        <p>{{ $filters.toPriceFormat(item.prices.shipping_price) }}円</p>
                      </div>
                      <div class="p-orderProductInfo">
                        <h6 class="g-title-quinary">小計</h6>
                        <p>{{ $filters.toPriceFormat(item.prices.subtotal) }}円</p>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="p-orderProductBody-right">
                  <a v-if="['not_submitted'].includes(item.state)" class="c-btn c-btn--blue ghost" :href="`/orders/history/${item.ref_code}`">
                    データ入稿へ
                  </a>
                  <a v-if="['under_check'].includes(item.state)" class="c-btn c-btn--blue ghost" :href="`/orders/history/${item.ref_code}`">
                    再入稿へ
                  </a>
                  <a v-if="['resubmission_request'].includes(item.state)" class="c-btn c-btn--red ghost" :href="`/orders/history/${item.ref_code}`">
                    再入稿へ
                  </a>
                  <a v-if="['checked'].includes(item.state)" class="c-btn c-btn--green ghost" :href="`/orders/history/${item.ref_code}`">
                    最終確認へ
                  </a>
                  <a v-if="['unassigned', 'printing', 'shipped', 'delivered'].includes(item.state)" class="c-btn c-btn--black ghost" :href="`/orders/history/${item.ref_code}`">
                    注文内容を見る
                  </a>
                  <a v-if="['cancelled'].includes(item.state)" class="c-btn c-btn--red">
                    キャンセル済み
                  </a>
                  <a v-if="item.design.state != 'confirmed' && !order.transaction.is_captured && item.state != 'cancelled'"
                    class="c-textLink c-textLink--negative"
                    @click.prevent.stop="postCancelOrder(item.ref_code)"
                    :class="{'is-loading': state.cancellingBtns.includes(item.ref_code)}"
                    href="#"
                  >
                    注文をキャンセルする
                  </a>
                  <a v-if="item.design.state == 'confirmed' && order.transaction.is_captured && item.is_reorderable"
                    class="c-btn c-btn--blue ghost"
                    :data-ref="item.ref_code"
                    :href="`/orders/reorder/${item.ref_code}`"
                  >
                    再注文する
                  </a>
                </div>
              </div>
            </div>
          </li>
        </ul>
      </li>
    </ol>

    <nav v-if="orders.next" class="p-orderList-pagination">
      <a class="c-btn c-btn--primary" :class="{'is-loading': state.isLoadingNext}" @click="loadNextOrders()">
        <span>もっとみる</span>
      </a>
    </nav>
  </div>
</template>

<script>

import DateUtils from "../../utils/DateUtils.js";
import { useStore } from "../providers/useStore";
import { reactive, computed } from "vue";

export default {
  name: "OrderHistory",
  setup(props, context) {
    const compState = reactive({
      isOpenOrderDocumentDropdowns: {},
      dropdownRenderValue: false,
      isLoadingNext: false,
      cancellingBtns: [],
    });

    const { store, state } = useStore();

    // computed
    const isInitialized = computed(()=>state.isInitialized);
    const orders = computed(()=>state.orders);
    const staticUrl = computed(()=>state.staticUrl);

    // methods
    const loadNextOrders = async () => {
      compState.isLoadingNext = true;
      await store.loadNextOrders();
      compState.isLoadingNext = false;
    }

    const dateFormat = (dateStr, format) => DateUtils.dateFormat(new Date(dateStr), format);

    const toggleOpenOrderDocumentDropdown = (ref_code = '') => {
      for (let code in compState.isOpenOrderDocumentDropdowns) {
        if (code === ref_code) compState.isOpenOrderDocumentDropdowns[code] = !compState.isOpenOrderDocumentDropdowns[code]
        else compState.isOpenOrderDocumentDropdowns[code] = false
      }
      if (!Object.keys(compState.isOpenOrderDocumentDropdowns).includes(ref_code)) {
        compState.isOpenOrderDocumentDropdowns[ref_code] = true;
      }
      compState.isOpenOrderDocumentDropdowns = Object.assign({}, compState.isOpenOrderDocumentDropdowns)
    };

    const postCancelOrder = (ref_code) => {
      compState.cancellingBtns.push(ref_code)
      store.postCancelOrder(ref_code)
      compState.cancellingBtns.pop(ref_code)
    };

    store.init();

    return {
      state: compState,
      isInitialized,
      orders,
      staticUrl,
      loadNextOrders,
      dateFormat,
      toggleOpenOrderDocumentDropdown,
      postCancelOrder
    }
  }
}

</script>

<style scoped>

</style>
