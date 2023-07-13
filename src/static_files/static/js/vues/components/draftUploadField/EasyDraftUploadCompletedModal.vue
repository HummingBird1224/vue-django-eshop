<template>
  <ModalWindow :isShow="isShow">
    <div ref="modalContent" class="contentWrapper">
      <div class="contentBody">
        <div class="left-container">
          <img :src="staticUrl + 'img/easy_draft/modals/draftUploadConfirmationThumbnail.png'" />
        </div>
        <div class="right-container">
          <img :src="staticUrl + 'img/icon_ok.png'" class="icon-ok" />
          <h3 class="g-title-tertiary">データ入稿が完了しました!</h3>
          <div class="buttonContent">
            <!-- <div class="buttonContainer action" @click="shareImage">イメージ画像をシェア</div> -->
            <div class="buttonContainer ok" @click="confirmed">閉じる</div>
          </div>
        </div>
      </div>
    </div>
  </ModalWindow>
</template>

<script>
import ModalWindow from "../common/ModalWindow";

export default {
  name: "EasyDraftUploadCompletedModal",
  mixins: [],
  components: { ModalWindow },
  props: {
    isShow: {
      type: Boolean,
    },

    staticUrl: {
      type: String,
    },
  },
  emits: ['close', 'confirmed'],
  data() {
    return {};
  },
  methods: {
    confirmed() {
      this.$emit("confirmed");
      this.$emit("close");
    },
    shareImage() {
      this.$emit("shareImage");
      this.$emit("close");
    },
  },
};
</script>

<style scoped>
.c-modal {
  background: rgba(255, 255, 255, 0.64) !important;
}
.icon-ok {
  padding: 20px;
}

.right-container {
  flex: 50%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.left-container {
  flex: 50%;
}
.contentWrapper {
  position: absolute;
  left: 0;
  right: 0;
  padding: 48px 46px 64px;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
}
.contentBody {
  padding: 24px;
  background: white;
  margin: 0 auto;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  box-shadow: 2px 2px 20px rgba(0, 0, 0, 0.08);
}

.buttonContent {
  display: flex;
  flex-direction: row;
  margin-top: 24px;
}

.buttonContainer {
  width: 180px;
  padding: 8px;
  border-radius: 200px;
  margin: 0 14px;
  display: flex;
  justify-content: center;
  border: 1px solid #205efb;
  cursor: pointer;
}

.ok {
  background-color: #205efb;
  color: white;
  font-weight: bold;
}

.action {
  color: #205efb;
  font-weight: bold;
}
</style>
