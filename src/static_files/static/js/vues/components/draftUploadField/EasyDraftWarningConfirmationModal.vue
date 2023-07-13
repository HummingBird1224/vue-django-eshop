<template>
  <ModalWindow :isShow="isShow">
    <div ref="modalContent" class="contentWrapper">
      <div class="contentBody">
        <h3 class="g-title-tertiary">パターンが不足しています</h3>
        <span class="easyDraftPatternWarningText">各面ごとにデザインを入稿することができますが、{{ inputNum }} 面しか入稿されていません<br/>このまま入稿しますか？</span>
        <div class="buttonContent">
          <div class="buttonContainer cancel" @click="cancelled">編集に戻る</div>
          <div class="buttonContainer ok" @click="confirmed">このまま入稿する</div>
        </div>
      </div>
    </div>
  </ModalWindow>
</template>

<script>
import ModalWindow from "../common/ModalWindow";

export default {
  name: "EasyDraftWarningConfirmationModal",
  mixins: [],
  components: { ModalWindow },
  props: {
    isShow: {
      type: Boolean,
    },
    designNum: {
      type: Number
    },
    inputNum: {
      type: Number
    }
  },
  data() {
    return {};
  },
  emits: ['close', 'confirmed'],
  methods: {
    confirmed() {
      this.$emit("confirmed");
      this.$emit("close");
    },
    cancelled() {
      this.$emit("close");
    },
  },
};
</script>

<style scoped>
.c-modal {
  background: rgba(255, 255, 255, 0.64) !important;
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

.easyDraftPatternWarningText {
  margin-top: 24px;
}
.contentBody {
  padding: 44px;
  background: white;
  width: 600px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  box-shadow: 2px 2px 20px rgba(0, 0, 0, 0.08);
  border-radius: 8px;
}

.buttonContent {
  display: flex;
  width: 100%;
  justify-content: flex-end;
  flex-direction: row;
  margin-top: 24px;
}

.buttonContainer {
  padding: 8px 16px;
  font-weight: bold;
  border-radius: 20px;
  margin: 0 14px;
  cursor: pointer;
  color: #205efb;
}

.ok {
}

.cancel {
  font-weight: bold;
}
</style>
