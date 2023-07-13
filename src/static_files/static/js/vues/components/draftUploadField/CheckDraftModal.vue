<template>
  <ModalWindow
    v-if="orderInfo"
    :isShow="isShow"
  >
    <div
      ref="modalContent"
      class="p-draftModal p-draftModal--check"
    >
      <header class="p-draftModalHeader">
        <h2 class="g-title-secondary">データ、ご注文内容、配送先をご確認ください</h2>
        <a
          href="#"
          @click.prevent.stop="close"
        >
          <svg>
            <use xlink:href='#icons-cross'/>
          </svg>
        </a>
      </header>

      <div class="p-ModalCheck">
        <div class="p-ModalOrder">
          <h4 class="g-title-quaternary">注文した商品</h4>

          <div class="p-ModalOrderInfo">
            <h5 class="g-title-quinary"><a class="c-textLink" :href="orderInfo.product_url">{{ orderInfo.product_name }}</a></h5>
            <div class="p-draftOrderDetail__row">
              <div
                class="p-draftOrderThumb"
                :style="thumbStyle"
              ></div>
              <div class="p-draftOrderInfo">
                <div class="p-draftOrderBody">
                  <div class="p-draftOrderBody-rowContainer">
                    <div class="p-draftOrderBody-row">
                      <div class="p-draftOrderBody-info">
                        <h6 class="g-title-quinary">サイズ</h6>
                        <p>{{ sizeStr }}</p>
                      </div>

                      <div class="p-draftOrderBody-info">
                        <h6 class="g-title-quinary">デザイン</h6>
                        <p v-if="orderInfo.extra_info.color_num < 0">フルカラー</p>
                        <p v-else>{{ orderInfo.extra_info.color_num }}色</p>
                      </div>

                      <div class="p-draftOrderBody-info">
                        <h6 class="g-title-quinary">出荷予定日</h6>
                        <p>確定次第ご連絡します</p>
                      </div>
                    </div>

                    <div class="p-draftOrderBody-row">
                      <div class="p-draftOrderBody-info">
                        <h6 class="g-title-quinary">注文数</h6>
                        <p>{{ orderInfo.quantity }}組</p>
                      </div>

                      <div class="p-draftOrderBody-info">
                        <h6 class="g-title-quinary">注文商品番号</h6>
                        <p>{{ orderInfo.ref_code }}</p>
                      </div>
                    </div>
                  </div>
                </div>
                <p class="p-draftOrderPrice">{{ $filters.toPriceFormat(orderInfo.total) }}<span>円</span></p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="p-ModalDeliverTo">
        <h4 class="g-title-quaternary">お届け先情報</h4>
        <p
          v-html="deliveryAddressHtml"
        >
        </p>
      </div>

      <div class="p-ModalData">
        <h4 class="g-title-quaternary">入稿データ</h4>
        <p>
          {{ orderInfo.design.filename }}
          <a
            :href="orderInfo.design.data"
            target="_blank"
          >
            <svg><use xlink:href='#icons-arrow_forward'/></svg>
          </a>
        </p>
      </div>

      <div class="p-ModalCta">
        <p>入稿完了後、canal運営がデータをチェックして、最終データの確定となります</p>
        <a
          class="c-btn c-btn--green"
          :class="{
            'is-loading': isProcessing
          }"
          href="#"
          @click.prevent.stop="completeOrder"
        >
          注文を完了する
        </a>
      </div>
    </div>
  </ModalWindow>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin";
import ModalWindow from "../common/ModalWindow";

export default {
  name: "CheckDraftModal",
  mixins: [StoreMixin],
  components: {ModalWindow},
  data: () => ({
    isProcessing: false,
  }),
  emits: ['close'],
  props: {
    isShow: {
      type: Boolean,
    },
  },
  computed: {
    orderInfo() {
      return this.state.orderInfo;
    },
    sizeStr() {
      if (!this.orderInfo) {
        return '';
      }

      const { depth, height, width } = this.orderInfo.extra_info.size;

      let size = `${width}cm×${height}cm`;

      if (depth) {
        size = size +  `×${depth}cm`;
      }
      return size;
    },
    thumbStyle() {
      const style = {};

      if (this.orderInfo && this.orderInfo.thumbnail) {
        style['background-image'] = `url(${this.orderInfo.thumbnail})`;
      }

      return style;
    },
    deliveryAddressHtml() {
      let html = '';

      if (this.orderInfo && this.orderInfo.delivery) {
        const da = this.orderInfo.delivery;

        html += `${da.full_name} 〒${da.postal_code}<br>`;
        if (da.building)
          html += `${da.prefecture}${da.city} ${da.building}<br>`;
        else
          html += `${da.prefecture}${da.city}<br>`;
        html += `${da.tel}`
      }

      return html;
    }
  },
  methods: {
    close() {
      this.$emit('close');
    },
    completeOrder() {
      if (this.isProcessing) {
        return;
      }

      this.isProcessing = true;

      this.store.postConfirmDesign()
        .then(() => {
          location.href = '/orders/history/?confirmed=true';
        })
        .finally(() => {
          this.isProcessing = false;
        });
    }
  },
  mounted() {
    document.addEventListener("click", e => {
      const target = (e.target || e.srcElement).closest(".p-draftModal");
      if (!this.isShow || target === this.$refs.modalContent) return;

      this.close();
    });
  }
}
</script>

<style scoped>

</style>
