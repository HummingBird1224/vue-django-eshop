<template>
  <ModalWindow :isShow="isShow">
    <div ref="modalContent" class="p-draftModal p-draftModal--easyUpload">
      <div v-show="isLoading" class="p-draftModal--loadingOverlay">
        <div class="p-draftModal--loadingContainer">
          <span>{{ processingText }}</span>
          <div class="p-draftModal--loading"></div>
        </div>
      </div>
      <div class="p-draftModal--easyUploadContainer">
        <div class="showCaseContainer">
          <div class="p-draftModal--operationOverlay">
              <div class="operation-list" v-if="isDesignableCanvas(selectedIndex)">
                <div class="reset-operation__container" @click="clearAllObjects">
                  <div class="reset__icon">
                    <img :src="staticUrl() + 'img/easy_draft/modals/operation_reset.png'"/>
                  </div>
                  全てやり直す
                </div>
                <div class="operation-element" @click="showCanvasGrid">
                  <img :src="staticUrl() + 'img/easy_draft/modals/operation_grid.png'"/>
                </div>
                <span class="operation-label">グリッド</span>
              </div>
          </div>
          <section id="showCaseHeader" @click="close()">
            <img :src="staticUrl() + 'img/easy_draft/modals/arrow_backward.png'" width="20px" />
            <span>戻る</span>
          </section>
          <section id="showCaseContents">
            <div id="selectedImageFrame" :style="{backgroundImage: 'url(' + selectedImage.image + ')'}">
              <div
                v-for="(area,i) in productInfo.easy_draft.print_area"
                :key="area.name"
                class="canvas-wrapper"
                :id="`canvas-container-element${i}`"
                v-show="i == selectedIndex"
              >
                <canvas v-if="area.is_printable" :id="'imageOverlay' + i"></canvas>
                <span v-if="area.is_printable" class="horizontal-canvas-width__label" :id="'horizontalLabel'+ i">{{ area.position.pdf.end.x -  area.position.pdf.start.x }}mm</span>
                <span v-if="area.is_printable" class="vertical-canvas-height__label" :id="'verticalLabel'+ i">{{ area.position.pdf.end.y -  area.position.pdf.start.y }}mm</span>
              </div>
            </div>
            <div class="selectableImages">
              <div
                v-for="(area, i) in productInfo.easy_draft.print_area"
                :key="area.name"
                class="imageSelection"
                @click="imgSelected(i)"
                :class=" i == selectedIndex ? 'selected' : '' "
              >
                <img :src="area.image" />
                <span>{{ area.name }}</span>
              </div>
            </div>
          </section>
          <section id="showCaseFooter">
            <div v-for="label in labels" :key="label.title" class="packageMetaInfo">
              <span class="meta-title">{{ label.title }}</span>
              <span class="meta-description">{{ label.value }}</span>
            </div>
            <div class="packageMetaInfo">
              <span class="meta-title">使用可能な色</span>
              <span class="meta-description">黒・白</span>
            </div>
          </section>
        </div>
        <div class="uploadFormContainer" id="upload-form__container">
          <div v-show="isDesignableCanvas(selectedIndex)" class="upload-form__wrapper">
            <div class="upload-form__title">
              <h3 class="g-title-tertiary">素材を追加する</h3>
              <div class="file-input-button__container">
                <div class="object-input__button" @click="showImageUploadModal">
                  <svg class="upload__icon">
                    <use xlink:href="#icons-file_upload"/>
                  </svg>
                  <span>ファイルを選択</span>
                </div>
                <div class="object-input__button" @click="inputTextObject">
                  <div class="upload__icon">
                    <img :src="staticUrl() + 'img/easy_draft/modals/input_text-icon.png'" width="20px" />
                  </div>
                  <span>テキスト入力</span>
                </div>
              </div>
            </div>
            <div class="uploaded-images__list" id="uploaded-images__list-container">
              <div v-for="(object, i) in currentObjects" :key="i" class="uploaded-image__container">
                <img v-if="object.type ==  'image'" :src="object._originalElement.currentSrc" class="uploaded-image__thumbnail" />
                <div v-else-if="object.type == 'textbox' ">
                  <span class="add-text__sample"> {{ truncate(object.text, 10) }} </span>
                </div>
                <div class="cancel-image__container">
                  <span v-if="object.type == 'textbox' " @click="setSelectTextBox(object)">書式を編集する</span>
                  <span @click="disposeObject(object)">素材を破棄する</span>
                </div>
              </div>
            </div>
          </div>
          <div class="textbox-edit-form__wrapper" v-if="isShowingTypographyPane">
            <div class="textbox-edit-pane__header">
              <h3 class="g-title-tertiary">フォント編集</h3>
              <div class="close-button" @click="unselectTextObject">
                <span>×</span>
              </div>
            </div>
            <div class="input-text__container">
              <h4 class="g-title-quaternary" :class="{ 'bold-label': isBold, 'italic-label': isItalic }" id="input-text__label" > {{ currentSelectText.text }} </h4>
            </div>
            <div class="textbox-font-family__select">
              <select @change="updateSelectFont" name="font-family">
                <option v-for="(font, i) in availableFontFamilys" :key="i" :value='font'>{{font}}</option>
              </select>
              <div class="select-arrow"></div>
            </div>
            <div class="textbox-font-style__select">
              <div class="font-color-selector" :class="{'is-white': isWhite }" @click="colorChange">
              </div>
              <div class="font-style-selector bold" :class="{'active': isBold }" @click="enableBold">
                B
              </div>
              <div class="font-style-selector italic" :class="{'active': isItalic }" @click="enableItalic">
                I
              </div>
            </div>
          </div>
          <div v-show="!isShowingTypographyPane && !isDesignableCanvas(selectedIndex)" class="unprintableAreaDescription">
            <span> {{ validateDesignableCanvas(selectedIndex) }}</span>
          </div>
          <button
            @click="sendImage"
            class="sendButton"
            v-bind:class="{ isActive: isUploadAvailable }"
          >デザインを入稿する</button>
        </div>
      </div>
    </div>
    <EasyDraftUploadCompletedModal
      :isShow="isShowingConfirmation"
      :staticUrl="staticUrl()"
      @confirmed="confirmed"
    ></EasyDraftUploadCompletedModal>
    <EasyDraftWarningConfirmationModal v-if="didCreatedCanvas"
      :isShow="isShowingWarning"
      :designNum="productInfo.extra_info.design_num"
      :inputNum="currentObjects.length"
      @close="isShowingWarning = false"
      @confirmed="processImage"
    ></EasyDraftWarningConfirmationModal>
    <EasyDraftImageUploadModal
    :isShow='isShowingImageUpload'
    @close="isShowingImageUpload = false"
    @file-uploaded="didFileInput"
    >
    </EasyDraftImageUploadModal>
  </ModalWindow>
</template>

<script>
import ModalWindow from "../common/ModalWindow";
import StoreMixin from "../../mixins/StoreMixin";
import DateUtils from "../../../utils/DateUtils.js";
import FabricjsUtils from "../../../utils/FabricjsUtils.js";
import EasyDraftUploadCompletedModal from "./EasyDraftUploadCompletedModal";
import EasyDraftWarningConfirmationModal from "./EasyDraftWarningConfirmationModal";
import EasyDraftImageUploadModal  from "./EasyDraftImageUploadModal";
import { fabric } from "fabric";
import ImageUtils from '../../../utils/ImageUtils';
import TextUtils from '../../../utils/TextUtils';
import { markRaw, nextTick } from "vue";

export default {
  name: "EasyUploadModal",
  mixins: [StoreMixin],
  components: { ModalWindow, EasyDraftUploadCompletedModal, EasyDraftWarningConfirmationModal, EasyDraftImageUploadModal },
  props: {
    isShow: {
      type: Boolean,
    },
    productInfo: {
      type: Object,
      required: true
    }
  },
  emits: ['refetch', 'close'],
  data() {
    return {
      labels: [],
      selectedIndex: 0,
      currentObjects: [],
      imageCanvas: {},
      didCreatedCanvas: false,
      processingText: "",
      isShowingConfirmation: false,
      isShowingWarning: false,
      isShowingImageUpload: false,
      currentSelectText: null,
      isLoading: false,
      drawnGrids: [],
      isBold: false,
      isItalic: false,
      isWhite: false,
      // https://www.w3schools.com/cssref/css_websafe_fonts.asp
      availableFontFamilys: [
        'Arial',
        'Verdana',
        'Helvetica',
        'Tahoma',
        'Trebuchet',
        'MS',
        'Times New Roman',
        'Georgia',
        'Garamond',
        'Courier New',
        'Brush Script MT'
        ],
    };
  },
  computed: {
    selectedImage() {
      return this.productInfo.easy_draft.print_area[this.selectedIndex];
    },
    isUploadAvailable() {
      return (
        Object.values(this.currentObjects).length > 0 &&
        !this.state.isFileUploading &&
        !this.state.isFileUploaded
      );
    },
    isShowingTypographyPane() {
      return this.currentSelectText != null;
    }
  },
  methods: {
    isDesignableCanvas(index) {
      const productData = this.productInfo.easy_draft.print_area[index];

      // データからそもそも印刷対象出ないもの
      if (!productData.is_printable)  return false;

      // テキスト編集パネルが表示されているなら
      if (this.isShowingTypographyPane) return false;

      if (!this.imageCanvas[index] && this.isSingleDesignMode())  {
        return false;
      }

      return true;
    },
    validateDesignableCanvas(index) {
      const productData = this.productInfo.easy_draft.print_area[index];

      // データからそもそも印刷対象出ないもの
      if (!productData.is_printable)  return "この面には印刷ができません";

      if (!this.imageCanvas[index] && this.isSingleDesignMode())  {
        return "この面には他の面のデザインが適応されます";
      }
    },
    truncate(val) {
      return TextUtils.truncateString(val, 8);
    },
    enableBold() {
      const text = this.currentSelectText;
      if (text.fontWeight == 'bold') {
        text.fontWeight = '';
      } else {
        text.fontWeight = 'bold';
      }
      this.applyTextStyle(text);
      text.canvas.requestRenderAll();
    },
    enableItalic() {
      const text = this.currentSelectText;
      text.fontStyle = text.fontStyle == 'italic' ? '' : 'italic';;
      this.applyTextStyle(text);
      text.canvas.requestRenderAll();
    },
    colorChange() {
      const text = this.currentSelectText;
      let newStyle = text.fill == '#fff' ? '#000' : '#fff';
      text.fill = newStyle;
      text.dirty = true;
      this.applyTextStyle(text);
      text.canvas.requestRenderAll();
    },
    unselectTextObject() {
      this.currentSelectText = null
    },
    updateSelectFont(e) {
      const text = this.currentSelectText;
      text.fontFamily = e.target.value
      text.canvas.requestRenderAll();
      nextTick(()=> this.applyTextStyle(text));
    },
    applyTextStyle(textbox) {
      const sample = document.getElementById('input-text__label')
      sample.style.fontFamily = textbox.fontFamily;
      sample.style.fontWeight = textbox.fontWeight;
      sample.style.fontStyle = textbox.fontStyle;

      this.isBold = textbox.fontWeight == 'bold';
      this.isItalic = textbox.fontStyle == 'italic';
      this.isWhite = textbox.fill == '#fff';
    },
    refetch() {
      this.$emit("refetch");
    },
    close() {
      this.$emit("close");
    },
    onChangeFile(e) {
      const file = e.target.files[0];
      this.didFileInput(file);
    },
    showImageUploadModal() {
      this.isShowingImageUpload = true;
    },
    inputTextObject() {
      const textbox = markRaw(new fabric.Textbox('Text', {
        left: 50,
        top: 50,
        fontSize: 20
      }));

      textbox.textAlign = "center";
      textbox.controls.deleteControl = FabricjsUtils.setupDeletingObjectControl(0, this.controlDisposeObject);
      textbox.controls.alignVerticalCenter = FabricjsUtils.setupVerticalAlignmentObjectControl(2);
      textbox.controls.alignHorizontalCenter = FabricjsUtils.setupHorizontalAlignmentObjectControl(3);
      textbox.controls.showTypographyPane = FabricjsUtils.setupTypographyPaneControl(1,  this.controlSelectTextBox);
      textbox.controls.bringToFront = FabricjsUtils.setupBringFrontControl(4);
      textbox.controls.bringToBack = FabricjsUtils.setupBringBackControl(5);
      this.setupObject(this.selectedIndex, textbox, 'text');
    },
    controlSelectTextBox(_, event, position) {
      this.setSelectTextBox(event.target);
    },
    setSelectTextBox(textBox) {
      if (this.currentSelectText) {
        this.unselectTextObject();
      }
      this.currentSelectText = markRaw(textBox);
      nextTick(()=> this.applyTextStyle(textBox));
    },
    async didFileInput(imgBuffer) {
      if (this.isLoading) {
        return;
      }
      this.isShowingImageUpload = false;
      let image = await ImageUtils.loadImage(imgBuffer).catch(e=>{
          this.processingText = "";
          this.isLoading = false;
      });
      this.applyImage(this.selectedIndex, image);
      this.processingText = "";
      this.isLoading = false;
    },
    applyImage(index, image) {
      let imgObj = markRaw(new fabric.Image(image));
      imgObj.controls.deleteControl = FabricjsUtils.setupDeletingObjectControl(0, this.controlDisposeObject);
      imgObj.controls.alignVerticalCenter = FabricjsUtils.setupVerticalAlignmentObjectControl(1);
      imgObj.controls.alignHorizontalCenter = FabricjsUtils.setupHorizontalAlignmentObjectControl(2);
      imgObj.controls.bringToFront = FabricjsUtils.setupBringFrontControl(3);
      imgObj.controls.bringToBack = FabricjsUtils.setupBringBackControl(4);
      const canvasWidth = this.imageCanvas[index].getWidth();
      const canvasHeight = this.imageCanvas[index].getHeight();
      if (
        image.width / canvasWidth > 1 ||
        image.height / canvasHeight > 1
      ) {
        if (image.width / canvasWidth > image.height / canvasHeight) {
          const newScale = canvasWidth / image.width;
          imgObj.scaleX = newScale;
          imgObj.scaleY = newScale;
        } else {
          const newScale = canvasHeight / image.height;
          imgObj.scaleX = newScale;
          imgObj.scaleY = newScale;
        }
      }
      this.setupObject(index, imgObj);

      return imgObj;
    },
    setupObject(index, object) {
      this.imageCanvas[index].add(object);
      this.currentObjects = FabricjsUtils.getinsertedObject(this.imageCanvas[index])
    },
    imgSelected(idx) {
      this.clearGrids(this.imageCanvas[this.selectedIndex]); // グリッドを削除しておく
      this.currentSelectText = null;
      this.selectedIndex = idx;

      if (this.imageCanvas[idx]) {
        this.currentObjects = FabricjsUtils.getinsertedObject(this.imageCanvas[idx])
      }
    },
    staticUrl() {
      return this.state.staticUrl;
    },
    async sendImage(e) {
      if (!this.isUploadAvailable) return;
      if (!this.isSingleDesignMode() && !this.validateImageCount()) {
        this.isShowingWarning = true;
      } else {
        await this.processImage();
      }
    },
    async processImage() {
      this.isLoading = true;
      this.processingText = "画像を生成しています";

      const { width, height } = this.productInfo.easy_draft.pdf_size;
      const { border, background } = this.productInfo.easy_draft.pdf_color;
      const canvases = Object.values(this.imageCanvas).filter(c=>c!=null)
      const printAreas = this.productInfo.easy_draft.print_area;
      const blob = await FabricjsUtils.processingPDF(canvases, printAreas, width, height, background, border);
      const file = new File([blob], `${DateUtils.millisecFormat(new Date())}.pdf`, { type: "application/pdf" });

      this.processingText = "ファイルをアップロードしています";
      await this.store.postEasyDraftUpload(file)
      this.isLoading = false;
      this.isShowingConfirmation = true;
    },
    validateImageCount() {
      return this.productInfo.extra_info.design_num == Object.values(this.imageCanvas).filter((o)=> o!= null && o._objects.length > 0).length
    },
    confirmed() {
      this.isShowingConfirmation = false;
      this.refetch();
      this.close();
    },
    generateLabels() {
      let { size, color_num, print_area_num, } = this.productInfo.extra_info;
      let { width, height, depth } = size;

      this.labels = [
        { title: "サイズ", value: depth ? `${width}x${height}x${depth}mm` : `${width}x${height}mm`,},
        { title: "色数",   value: `${color_num}色`, },
      ];
      if (print_area_num) {
        this.labels.push({ title: "印刷面数",value: `${print_area_num}面`,});
      }
    },
    showCanvasGrid() {
      let activeCanvas = this.imageCanvas[this.selectedIndex];
      // grid-canvasにグリッドをレンダリングさせる
      if (this.drawnGrids.length > 0) {
        this.clearGrids(activeCanvas);
      } else {
        this.createGrids(activeCanvas);
      }
    },
    clearGrids(canvas) {
      this.drawnGrids.forEach(g=>canvas.remove(g));
      this.drawnGrids = [];
    },
    createGrids(canvas) {
        let area = this.productInfo.easy_draft.print_area[this.selectedIndex];
        let { start, end } = area.position.pdf;
        let pdfWidth = end.x - start.x;
        this.drawnGrids = FabricjsUtils.drawGrid(
          canvas, '#888888', 5 * (canvas.width / pdfWidth), 0.5
        ).concat(FabricjsUtils.drawGrid(canvas, '#888888', 10 * (canvas.width / pdfWidth), 1));
        for (let object of FabricjsUtils.getinsertedObject(canvas)) {
           object.canvas.bringToFront(object);
        }
        this.imageCanvas[this.selectedIndex].requestRenderAll();
    },
    clearAllObjects() {
      // Fabricオブジェクト類も削除
     for (let i = 0; i < this.productInfo.easy_draft.print_area.length; i++) {
        if (!this.productInfo.easy_draft.print_area[i].is_printable) {
          continue;
        }
        if (this.imageCanvas[i] == null) continue;

        for(let object of this.imageCanvas[i]._objects) {
          FabricjsUtils.removeObject(object)
        }
     }

      // フラグ等あればそちらも削除
      this.unselectTextObject();
      this.clearGrids(this.imageCanvas[this.selectedIndex]);
    },
    isSingleDesignMode() {
      return this.productInfo.extra_info.design_num == 1 && this.productInfo.extra_info.print_area_num != 1
    },
    controlDisposeObject(_, event, position) {
      this.disposeObject(event.target)
    },
    disposeObject(object) {
      FabricjsUtils.removeObject(object)
      this.currentObjects = FabricjsUtils.getinsertedObject(this.imageCanvas[this.selectedIndex])
    },
    windowResized() {
      if (!this.didCreatedCanvas) {
        return;
      }

      this.sizingAndPositioningCanvas();
      this.adjustListContainerHeight();
    },
    adjustListContainerHeight() {
      const { offsetHeight } = document.getElementById('upload-form__container');
      if (offsetHeight) {
        const listContainer = document.getElementById('uploaded-images__list-container');
        if (listContainer) {
          const newContainerHeight = offsetHeight - 154;
          listContainer.style.height = `${newContainerHeight - 120}px`;
        }
      }
    },
    sizingAndPositioningCanvas() {
      const imageFrame = document.getElementById(`selectedImageFrame`);
      const { clientWidth, clientHeight } = imageFrame;

      const selectedImageFrame = document.getElementById("selectedImageFrame");
      const { clientWidth: originalWidth } = selectedImageFrame;
      if (originalWidth > 1660) {
        selectedImageFrame.style.width = `1660px`
        selectedImageFrame.style.height = `1040px`
      } else {
        selectedImageFrame.style.height = `${originalWidth * 1040/1660}px`;
      }

      // // 表示領域のサイズを取得
      const imageWidth = 1660; // この情報が事前に欲しい
      const imageHeight = 1040; // この情報が事前に欲しい
      const imageScale = clientWidth > imageWidth ? 1.0 : clientWidth / imageWidth;

      for (let i = 0; i < this.productInfo.easy_draft.print_area.length; i++) {
        let area = this.productInfo.easy_draft.print_area[i];
        if (!area.is_printable) {
          continue;
        }
        let canvas = this.imageCanvas[i];
        // 画像の本来のサイズからスケールさせる
        const cc = document.getElementById(`canvas-container-element${i}`);
        const hl = document.getElementById(`horizontalLabel${i}`);
        const vl = document.getElementById(`verticalLabel${i}`);

        if (canvas) {
          let { start, end } = area.position.image;
          const preHeight = canvas.getHeight();
          canvas.setWidth((end.x - start.x) * imageScale);
          canvas.setHeight((end.y - start.y) * imageScale);
          let ratio = ((end.y - start.y) * imageScale) / preHeight;
          if (this.imageCanvas[i]._objects.length > 0) {
            for (let object of this.imageCanvas[i]._objects) {
              let newScale = object.scaleY * ratio;
              object.scaleX = newScale;
              object.scaleY = newScale;
              object.left = object.left * ratio;
              object.top = object.top * ratio;
              object.setCoords();
            }
          }
          cc.style.position = "absolute";
          cc.style.left = `${start.x * imageScale + imageFrame.offsetLeft}px`;
          cc.style.top = `${start.y * imageScale + imageFrame.offsetTop}px`;

          hl.style.top = `${- canvas.height - 25}px`;
          hl.style.left = `${canvas.width/2 - 20}px`;

          vl.style.top = `${- canvas.height/2 - 20}px`;
          vl.style.right = `${-canvas.width + 60}px`;
        }  else {
            hl.style.visibility = 'hidden';
            vl.style.visibility = 'hidden';
        }

        if (i == this.selectedIndex) {
          if(this.drawnGrids.length > 0) {
            this.clearGrids(canvas);
            this.createGrids(canvas);
          }
        }
      }
    },
    createCanvas() {
      for (let i = 0; i < this.productInfo.easy_draft.print_area.length; i++) {
        if (!this.productInfo.easy_draft.print_area[i].is_printable) continue;

        let c = document.getElementById(`imageOverlay${i}`);
        let canvas = markRaw(new fabric.Canvas(c));
        this.imageCanvas[i] = canvas;
        if (this.isSingleDesignMode()) {
          break;
        }
      }
      this.didCreatedCanvas = true;
    },
  },
  async mounted() {
    this.generateLabels();
    this.imgSelected(0);

    window.addEventListener("resize", this.windowResized);
  },
  updated() {
    // NOTE: 一度APIの結果を受け取ってからマウントして、その結果にたいしてCanvas生成を行うのでこのタイミングで処理をしている
    if (this.didCreatedCanvas) {
      return;
    }

    FabricjsUtils.applyFabricjsSetting();
    this.createCanvas();
    this.sizingAndPositioningCanvas();
    this.adjustListContainerHeight();
  },
};
</script>

<style scoped>
</style>
