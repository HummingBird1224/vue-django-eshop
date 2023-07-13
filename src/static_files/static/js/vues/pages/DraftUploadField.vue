<template>
  <div>
    <div class="p-draftMain" v-if="orderInfo && !orderInfo.is_easy_draft_available">
      <div class="p-draftMain-left">
        <h4 class="g-title-quaternary">{{ fieldTitle }}</h4>

        <template v-if="shouldShowProductInfo">
          <ProductInfo />
        </template>

        <template v-else>
          <FileInfo />

          <FileChecking v-if="flow === DraftFlow.UNDER_CHECK" />
          <FileCheckFailed v-else-if="flow === DraftFlow.RE_SUBMITTION_REQUEST" />
          <FileCheckSuccess v-else-if="flow === DraftFlow.CHECKED" />
        </template>
      </div>
      <div class="p-draftMain-right">
        <template v-if="shouldShowUploadField">
          <Uploading v-if="isFileUploading" />
          <UploadInfo v-else-if="isFileUploaded" />
          <UploadField v-else />
        </template>

        <template v-else-if="flow === DraftFlow.UNDER_CHECK">
          <UploadChecking />
        </template>

        <template v-if="flow === DraftFlow.CHECKED">
          <UploadSuccess />
        </template>

        <template v-if="shouldShowUploadCompleted">
          <UploadCompleted />
        </template>
      </div>

      <UploadModal :isShow="isShowUploadModal" @close="closeUploadModal" />
      <CheckDraftModal :isShow="isShowCheckDraftModal" @close="closeCheckDraftModal" />
    </div>

    <div v-else>
      <div v-if="orderInfo" class="p-draftMain">
        <div class="p-draftMainContainer">
          <div class="p-Product">
            <div v-if="orderInfo"
              class="p-ProductThumb"
              :style="'background-image: url(' + orderInfo.thumbnail + ')'"
            ></div>
            <div class="p-ProductInfo">
              <h3 class="g-title-tertiary">{{ orderInfo.product_name }}</h3>
              <div class="p-ProductDetail__row">
                <div class="p-ProductDetail-leftContainer">
                  <div class="p-ProductDetail-column">
                    <h6 class="g-title-quinary">サイズ</h6>
                    <p>{{ sizeStr }}</p>
                  </div>
                  <div class="p-ProductDetail-column">
                    <h6 class="g-title-quinary">色数</h6>
                    <p>{{ orderInfo.extra_info.color_num }} 色</p>
                  </div>
                  <div class="p-ProductDetail-column">
                    <h6 class="g-title-quinary">面数</h6>
                    <p>{{ orderInfo.extra_info.print_area_num }}面</p>
                  </div>
                  <div class="p-ProductDetail-column">
                    <h6 class="g-title-quinary">注文数</h6>
                    <p>{{ orderInfo.quantity }}個</p>
                  </div>
                </div>
                <div class="p-ProductDetail-rightContainer">
                  <div
                    v-for="(label, key) in orderInfoDetailLabels"
                    :key="key"
                    class="p-ProductDetail-column"
                  >
                    <h6 class="g-title-quinary">{{ label[0] }}</h6>
                    <p>{{ $filters.toPriceFormat(label[1]) }}円</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div v-if="flow === DraftFlow.UNDER_CHECK">
        <div class="p-UploadInfo-underCheckContainer" v-if="flow === DraftFlow.UNDER_CHECK">
          <div class="p-UploadInfo-underCheckStatusHeader">
            <h4 class="g-title-quaternary">入稿が完了しています。ただいまデータのチェック中です....</h4>
            <span>{{ uploadedFileName }}</span>
            <a :href="uploadedUrl" target="_blank">データを確認する</a>
          </div>
          <div class="p-UploadInfo-underCheckStatusDescription">
            <div class="p-UploadInfo-underCheckDescription">
              <span>確認が終わるまでしばらくお待ちください。</span>
              <span>データを修正ずる場合は未入稿状態に戻して別のデータを入稿しなおしてください</span>
            </div>
            <div class="p-UploadInfo-withdrawUploadedDesign" @click="showWithDrawConfirmationModal">
              <span>別のデータを入稿する</span>
            </div>
          </div>
        </div>
      </div>
      <div class="p-UploadInfo-draftCheckedContainer" v-else-if="flow === DraftFlow.CHECKED">
        <FileCheckSuccess />
        <UploadSuccess />
      </div>
      <FileCheckFailed v-else-if="flow === DraftFlow.RE_SUBMITTION_REQUEST" />
      <div v-if="flow === DraftFlow.RE_SUBMITTION_REQUEST || flow === DraftFlow.NOT_SUBMITTED">
        <div class="p-UploadInfo-draftModeSwitch">
          <div
            :class=" easyUploadSelected ? 'enabled selection' : 'disabled selection' "
            @click="e=> { easyUploadSelected = true }"
          >
            <span>カンタン入稿</span>
          </div>
          <div
            :class="!easyUploadSelected ? 'enabled selection' : 'disabled selection' "
            @click="e=> { easyUploadSelected = false }"
          >
            <span>自分でデータ作成して入稿</span>
          </div>
        </div>
        <div  v-if="orderInfo && easyUploadSelected" class="p-draftEasyInput">
          <h3 class="g-title-tertiary">カンタン入稿</h3>
          <span class="p-draftEasyInput-HeaderDescription">画像データをアップロードするだけで入稿データを作成する方法です。</span>
          <div class="p-draftEasyInput-Container">
            <img :src="orderInfo.thumbnail " class="p-draft-CategoryImage" />
            <div class="p-draftDescriptionWrapper">
              <h3 class="g-title-tertiary">入稿データ内容</h3>
              <div class="p-draftInputInfoContainer">
                <div class="p-draftInputInfoLabelWrapper">
                  <h6 class="g-title-quinary">印刷面数</h6>
                  <span>
                    <strong>{{ orderInfo.extra_info.print_area_num }}</strong>面
                  </span>
                </div>
                <div class="p-draftInputInfoLabelWrapper">
                  <h6 class="g-title-quinary">色数</h6>
                  <span>
                    <strong>{{ orderInfo.extra_info.color_num }}</strong>色
                  </span>
                </div>
              </div>
              <div class="p-draftInputInfoContainer">
                <div class="p-draftInputInfoLabelWrapper">
                  <h6 class="g-title-quinary">印刷内容</h6>
                  <span>
                    <strong>{{ orderInfo.extra_info.design_num }}</strong>パターン
                  </span>
                </div>
                <div class="p-draftInputInfoLabelWrapper">
                  <h6 class="g-title-quinary">使用可能な色</h6>
                  <span>白 / 黒</span>
                </div>
              </div>
              <div @click="openEasyUploadModal">
                <div class="p-draftInputDataLinkButton">
                  <span>データ作成へ</span>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div v-else>
          <h3 class="g-title-tertiary">自分でデータ作成して入稿</h3>
          <span class="p-draftEasyInput-HeaderDescription">ご自身でデータを作成する方法です。自由に位置を調整することができます。</span>
          <template v-if="shouldShowUploadField">
            <Uploading v-if="isFileUploading" />
            <UploadInfo v-else-if="isFileUploaded" />
            <UploadField v-else />
          </template>
          <template v-else-if="flow === DraftFlow.UNDER_CHECK">
            <UploadChecking />
          </template>
          <template v-if="flow === DraftFlow.CHECKED">
            <UploadSuccess />
          </template>
          <template v-if="shouldShowUploadCompleted">
            <UploadCompleted />
          </template>
        </div>
        <UploadModal :isShow="isShowUploadModal" @close="closeUploadModal" />
        <EasyUploadModal
          v-if="isEasyDraftAvailable"
          :productInfo="productInfo"
          :isShow="isShowEasyUploadModal"
          @close="closeEasyUploadModal"
          @refetch="fetchOrderInfo"
        />
      </div>
      <CheckDraftModal :isShow="isShowCheckDraftModal" @close="closeCheckDraftModal" />
      <DraftDeleteConfirmationModal
        :isShow="isShowingWithDrawConfirmation"
        @close="isShowingWithDrawConfirmation = false"
        @confirmed="withDrawUploadedDesign"
      ></DraftDeleteConfirmationModal>
    </div>
  </div>
</template>

<script>
import StoreMixin from "../mixins/StoreMixin";
import DraftFlow from "../../constants/DraftFlow";
import ProductInfo from "../components/draftUploadField/ProductInfo";
import FileInfo from "../components/draftUploadField/FileInfo";
import UploadField from "../components/draftUploadField/UploadField";
import Uploading from "../components/draftUploadField/Uploading";
import UploadSuccess from "../components/draftUploadField/UploadSuccess";
import UploadModal from "../components/draftUploadField/UploadModal";
import CheckDraftModal from "../components/draftUploadField/CheckDraftModal";
import UploadChecking from "../components/draftUploadField/UploadChecking";
import FileCheckFailed from "../components/draftUploadField/FileCheckFailed";
import FileChecking from "../components/draftUploadField/FileChecking";
import FileCheckSuccess from "../components/draftUploadField/FileCheckSuccess";
import UploadCompleted from "../components/draftUploadField/UploadCompleted";
import UploadInfo from "../components/draftUploadField/UploadInfo";
import EasyUploadModal from "../components/draftUploadField/EasyUploadModal";
import DraftDeleteConfirmationModal from "../components/draftUploadField/DraftDeleteConfirmationModal";

export default {
  name: "DraftUploadField",
  components: {
    UploadInfo,
    UploadCompleted,
    FileCheckSuccess,
    FileChecking,
    FileCheckFailed,
    UploadChecking,
    CheckDraftModal,
    UploadModal,
    UploadSuccess,
    Uploading,
    UploadField,
    FileInfo,
    ProductInfo,
    EasyUploadModal,
    DraftDeleteConfirmationModal,
  },
  mixins: [StoreMixin],
  data: () => ({
    DraftFlow,
    easyUploadSelected: true,
    isShowingWithDrawConfirmation: false,
  }),
  computed: {
    orderInfo() {
      return this.state.orderInfo;
    },
    productInfo() {
      return this.state.productInfo;
    },
    orderInfoDetailLabels() {
      const keyAndLabels = {
        product_total: "商品代",
        plate_price: "版代",
        mold_price: "木型代",
        // unit_price: "単価",
        subtotal: "小計",
        shipping_price: "送料",
        tax: "消費税",
        total: "合計(税込)",
      };
      const prices = this.orderInfo.prices;
      return Object.keys(keyAndLabels)
        .filter((k) => prices[k] != 0)
        .map((k) => [keyAndLabels[k], prices[k]]);
    },
    sizeStr() {
      if (!this.orderInfo) {
        return "";
      }

      const { depth, height, width } = this.orderInfo.extra_info.size;

      let size = `${width}cm×${height}cm`;

      if (depth) {
        size = size + `×${depth}cm`;
      }
      return size;
    },
    uploadedUrl() {
      return this.state.orderInfo ? this.state.orderInfo.design.data : '';
    },
    cancelEasyDraftData() {},
    uploadedFileName() {
      return  this.state.orderInfo ? this.state.orderInfo.design.filename : '';
    },
    flow() {
      return this.state.flow;
    },
    isFileUploading() {
      return this.state.isFileUploading;
    },
    isFileUploaded() {
      return this.state.isFileUploaded;
    },
    isShowUploadModal() {
      return this.state.isShowUploadModal;
    },
    isShowCheckDraftModal() {
      return this.state.isShowCheckDraftModal;
    },
    isShowEasyUploadModal() {
      return this.state.isShowEasyUploadModal;
    },
    isEasyDraftAvailable() {
      if (this.state.productInfo) {
        return this.state.productInfo.is_easy_draft_available
      }
      return false;
    },
    fieldTitle() {
      switch (this.flow) {
        case DraftFlow.NOT_SUBMITTED:
          return this.isFileUploaded
            ? "注文している商品"
            : "作成したデータをアップロード";
        case DraftFlow.UNDER_CHECK:
        case DraftFlow.RE_SUBMITTION_REQUEST:
        case DraftFlow.CHECKED:
          return "入稿したデータ";
        case DraftFlow.PRINTING:
        case DraftFlow.SHIPPED:
        case DraftFlow.DELIVERED:
          return "注文している商品";
        default:
          return "";
      }
    },
    shouldShowProductInfo() {
      return (
        this.flow === DraftFlow.NOT_SUBMITTED ||
        this.flow === DraftFlow.PRINTING ||
        this.flow === DraftFlow.SHIPPED ||
        this.flow === DraftFlow.DELIVERED
      );
    },
    shouldShowUploadField() {
      return (
        this.flow === DraftFlow.NOT_SUBMITTED ||
        this.flow === DraftFlow.RE_SUBMITTION_REQUEST
      );
    },
    shouldShowUploadCompleted() {
      return (
        this.flow === DraftFlow.PRINTING ||
        this.flow === DraftFlow.SHIPPED ||
        this.flow === DraftFlow.DELIVERED
      );
    },
  },
  methods: {
    closeUploadModal() {
      this.store.closeUploadModal();
    },
    closeCheckDraftModal() {
      this.store.closeCheckDraftModal();
    },
    openUploadModal() {
      this.store.openUploadModal();
    },
    openEasyUploadModal() {
      this.store.openEasyUploadModal();
    },
    closeEasyUploadModal() {
      this.store.closeEasyUploadModal();
    },
    showWithDrawConfirmationModal() {
      this.isShowingWithDrawConfirmation = true;
    },
    async withDrawUploadedDesign() {
      this.resetUploadStatus();
      await this.store.withDrawUploadedDesign()
      await this.fetchOrderInfo();
    },
    async fetchOrderInfo() {
      return this.store.fetchOrderInfo();
    },
    async fetchProductInfo() {
      return this.store.fetchProductInfo();
    },
    resetUploadStatus() {
      this.store.resetUploadStatus();
    },
  },
  async mounted() {
    await this.fetchOrderInfo()
    await this.fetchProductInfo()
  },
};
</script>

<style scoped>
</style>
