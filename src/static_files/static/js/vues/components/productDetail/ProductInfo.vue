<template>
  <div class="p-ProductInfo">
    <h2 class="g-title-secondary p-ProductInfo-title">{{ product.name }}</h2>
    <p class="p-ProductInfo-description">{{ product.overview }}</p>
    <ul class="p-ProductInfo-detailList">
      <li class="p-ProductInfo-detail">
        <h3 class="g-title-tertiary">
          <span class="p-ProductInfo-detailIconWrapper">
            <svg
              class="p-ProductInfo-detailIcon p-ProductInfo-detailIcon--time"
            >
              <use xlink:href="#icons-access_time" />
            </svg>
          </span>
          <span class="p-ProductInfo-detailTitle">納期の目安</span>
        </h3>
        <p class="p-ProductInfo-detailBody">{{ estimatedShippingDateStr }}</p>
        <div
          class="p-ProductInfo-questionIcon"
          @click="openExplanation('delivery')"
        >
          <img :src= "staticUrl + 'img/question_icon.png'" />
        </div>
      </li>
      <li class="p-ProductInfo-detail">
        <h3 class="g-title-tertiary">
          <span class="p-ProductInfo-detailIconWrapper">
            <svg
              class="p-ProductInfo-detailIcon p-ProductInfo-detailIcon--note"
            >
              <use xlink:href="#icons-event_note" />
            </svg>
          </span>
          <span class="p-ProductInfo-detailTitle">最小注文数</span>
        </h3>
        <p
          v-if="minOrderingQuantity > 0"
          class="p-ProductInfo-detailBody"
        >
          {{ minOrderingQuantity }}
        </p>
        <p v-else class="p-ProductInfo-detailBody">お問い合わせください</p>
      </li>
      <li class="p-ProductInfo-detail">
        <h3 class="g-title-tertiary">
          <span class="p-ProductInfo-detailIconWrapper">
            <svg
              class="p-ProductInfo-detailIcon p-ProductInfo-detailIcon--shuttle"
            >
              <use xlink:href="#icons-airport_shuttle" />
            </svg>
          </span>
          <span class="p-ProductInfo-detailTitle">送料</span>
        </h3>
        <p class="p-ProductInfo-detailBody">無料キャンペーン中</p>
      </li>
      <li v-if="hasChoosableColor" class="p-ProductInfo-detail">
        <h3 class="g-title-tertiary">
          <span class="p-ProductInfo-detailIconWrapper">
            <svg
              class="p-ProductInfo-detailIcon p-ProductInfo-detailIcon--shuttle"
            >
              <use xlink:href="#icons-color_lens" />
            </svg>
          </span>
          <span class="p-ProductInfo-detailTitle">使える色</span>
        </h3>
        <p class="p-ProductInfo-detailBody">{{ choosableColor.value }}</p>
        <div
          v-if="choosableColor.value !== 'フルカラー'"
          class="p-ProductInfo-questionIcon"
          @click="openExplanation('color')"
        >
          <img :src= "staticUrl + 'img/question_icon.png'" />
        </div>
      </li>
      <li v-if="isDesignNecessary" class="p-ProductInfo-detail">
        <h3 class="g-title-tertiary">
          <span class="p-ProductInfo-detailIconWrapper">
            <svg
              class="p-ProductInfo-detailIcon p-ProductInfo-detailIcon--shuttle"
            >
              <use xlink:href="#icons-brush" />
            </svg>
          </span>
          <span class="p-ProductInfo-detailTitle">入稿形式</span>
        </h3>
        <p v-if="isEasyDraftAvailable" class="p-ProductInfo-detailBody">
          カンタン入稿
        </p>
        <p v-else class="p-ProductInfo-detailBody">データを作成して入稿</p>
        <div
          class="p-ProductInfo-questionIcon"
          @click="openExplanation('draft')"
        >
          <img :src= "staticUrl + 'img/question_icon.png'" />
        </div>
      </li>
      <li class="p-ProductInfo-detail">
        <h3 class="g-title-tertiary">
          <span class="p-ProductInfo-detailIconWrapper">
            <svg
              class="p-ProductInfo-detailIcon p-ProductInfo-detailIcon--shuttle"
            >
              <use xlink:href="#icons-han" />
            </svg>
          </span>
          <span class="p-ProductInfo-detailTitle">版代</span>
        </h3>
        <p
          v-if="choosableColor.value == 'フルカラー'"
          class="p-ProductInfo-detailBody"
        >
          不要
        </p>
        <p v-else class="p-ProductInfo-detailBody">初回のみ必要。同サイズは2回目以降無料。</p>
        <div
          class="p-ProductInfo-questionIcon"
          @click="openExplanation('version_charge')"
        >
          <img :src= "staticUrl + 'img/question_icon.png'" />
        </div>
      </li>
    </ul>
    <ExplanationModal
      :isShow="isShowingExplanation"
      :title="currentSelectedContents.title"
      :contents="currentSelectedContents.description"
      :staticUrl='staticUrl'
      @close="isShowingExplanation = false"
    />
  </div>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin";
import ExplanationModal from "../common/ExplanationModal";
import {
  cardBoardColorExplain,
  flatBagColorExplain,
  cardBoardDraftExplain,
  flatBagDraftExplain,
  flatBagPlateChargeExplain,
  cardboardPlateChargeExplain,
  paperboxPlateChargeExplain,
  howToFixTotalPrice,
  howToFixDeliveryDate,
  printAreaCardboardtypeA,
  printAreaCardboardtypeNHaiso,
  printAreaCardboardtypeNKonpo,
  printAreaCardboardTatou,
  printAreaFlatbagPressBag,
  printAreaFlatbagAlmiClear,
  printAreaFlatbagTapedOPP,
  printAreaFlatbagTapeBag,
  printAreaFlatbagZipClear,
  printAreaFoldingCarton,
  // printAreaCushionEnvelope,
} from "../../../constants/ExplainModalDatas";
import ThumbViewer from "./ThumbViewer";
import SlideShow from "./SlideShow";
export default {
  name: "ProductInfo",
  mixins: [StoreMixin],
  components: {
    ExplanationModal, ThumbViewer, SlideShow,
  },
  methods: {
    openExplanation: function (contentsSelector) {
      switch (contentsSelector) {
        case "version_charge":
          if (this.product.main_category.slug == "cardboard") {
            this.currentSelectedContents = flatBagPlateChargeExplain;
          } else if (this.product.main_category.slug == "flatbag") {
            this.currentSelectedContents = cardboardPlateChargeExplain;
          } else if (this.product.main_category.slug == "paperbox") {
            this.currentSelectedContents = paperboxPlateChargeExplain;
          }
          break;
        case "color":
          if (this.product.main_category.slug == "cardboard") {
            this.currentSelectedContents = cardBoardColorExplain;
          } else if (this.product.main_category.slug == "flatbag") {
            this.currentSelectedContents = flatBagColorExplain;
          } else if (this.product.main_category.slug == "paperbox") {
            this.currentSelectedContents = cardBoardColorExplain;
          }
          break;
        case "draft":
          if (this.product.main_category.slug == "cardboard") {
            this.currentSelectedContents = cardBoardDraftExplain;
          } else if (this.product.main_category.slug == "flatbag") {
            this.currentSelectedContents = flatBagDraftExplain;
          } else if (this.product.main_category.slug == "paperbox") {
            this.currentSelectedContents = cardBoardDraftExplain;
          }

          break;
        case "delivery":
          this.currentSelectedContents = howToFixDeliveryDate;
          break;
        case "print_area":
          this.currentSelectedContents = this.getPrintAreaData(
            this.product.main_category.slug,
            this.product.slug
          );
          break;
      }
      this.isShowingExplanation = true;
    },
    getPrintAreaData: function (mainCategory, slug) {
      if (mainCategory == "cardboard") {
        switch (slug) {
          case "atype":
          case "atype-small-lot":
          case "atype-craft":
          case "atype-craft-small-lot":
          case "atype-white":
          case "atype-white-small-lot":
          case "atype-fullcolor-small-lot":
            return printAreaCardboardtypeA;
          case "ntype-mailer":
          case "ntype-mailer-small-lot":
          case "ntype-mailer-craft":
          case "ntype-mailer-craft-small-lot":
          case "ntype-mailer-white":
          case "ntype-mailer-white-small-lot":
            return printAreaCardboardtypeNHaiso;
          case "ntype-corrugated":
          case "ntype-corrugated-small-lot":
          case "ntype-corrugated-craft":
          case "ntype-corrugated-craft-small-lot":
          case "ntype-corrugated-white":
          case "ntype-corrugated-white-small-lot":
          case "ntype-corrugated-fullcolor":
            return printAreaCardboardtypeNKonpo;
          case "ttype":
          case "ttype-small-lot":
          case "ttype-craft":
          case "ttype-craft-small-lot":
          case "ttype-white":
            return printAreaCardboardTatou;
        }
      } else if (mainCategory == "flatbag") {
        switch (slug) {
          case "tape-opp-bag":
          case "tape-opp-bag-small-lot":
            return printAreaFlatbagTapedOPP;
          case "zip-aluminum-clear-bag":
          case "zip-aluminum-clear-bag-small-lot":
            return printAreaFlatbagAlmiClear;
          case "zip-clear-bag":
          case "zip-clear-bag-small-lot":
            return printAreaFlatbagZipClear;
          case "tape-bag":
          case "tape-bag-small-lot":
            return printAreaFlatbagTapeBag;
          case "aluminum-pouche":
          case "subsection-bag":
          case "zip-aluminum-stand":
          case "zip-aluminum-stand-small-lot":
          case "zip-clear-pressbag":
          case "zip-aluminum-bag":
          case "zip-aluminum-bag-small-lot":
            return printAreaFlatbagPressBag;
        }
      } else if (mainCategory == "paperbox") {
        switch (slug) {
          case "folding-carton":
            return printAreaFoldingCarton;
        }
      //} else if (mainCategory == "envelope") {
      //  switch (slug) {
      //    case "cushion-envelope":
      //      return printAreaCushionEnvelope;
      //  }
      }
    },
  },
  data() {
    return {
      isShowingExplanation: false,
      currentSelectedContents: cardBoardColorExplain,
    };
  },
  computed: {
    staticUrl() {
      return this.state.staticUrl;
    },
    product() {
      return this.state.product;
    },
    info() {
      return this.product.info;
    },
    canOrderOnSite() {
      return this.info.can_order_on_site;
    },
    isContactRequired() {
      return this.info.is_contact_required;
    },
    hasChoosableColor() {
      return this.info.choosable_color !== undefined;
    },
    choosableColor() {
      return this.info.choosable_color;
    },
    estimatedShippingDateStr() {
      const estimatedShippingDateFirst = Math.ceil(this.info.estimated_shipping_date_first / 7)
      const estimatedShippingDateRepeat = Math.ceil(this.info.estimated_shipping_date_repeat / 7)
      if (
        !estimatedShippingDateFirst ||
        !estimatedShippingDateRepeat
      ) {
        return null;
      }

      return (
        "初回：約" +
        estimatedShippingDateFirst +
        "週間\n" +
        "リピート：約" +
        estimatedShippingDateRepeat +
        "週間"
      );
    },
    minOrderingQuantity() {
      return this.info.min_ordering_quantity;
    },
    isDesignNecessary() {
      return this.info.is_design_necessary;
    },
    isEasyDraftAvailable() {
      return this.info.is_easy_draft_available;
    },
    hasVersionCharge() {
      return (
        this.product.main_category.slug == "paperbox" ||
        this.product.main_category.slug == "flatbag"
      );
    },
    isPaperbox() {
      return this.product.main_category.slug == "paperbox";
    },
    sizeOptionItems() {
      const sizeOption = this.store.getOptionBySlug('size');
      return sizeOption.items;
    },
  },
};
</script>

<style scoped></style>
