<template>
  <ModalWindow :isShow="isShow">
    <div ref="modalContent" class="contentWrapper">
      <div class="contentBody">
        <h3 class="g-title-tertiary">入稿データを破棄して未入稿状態へ戻しますか？</h3>
        <span class="draftDeleteCaustionText">この操作はキャンセルできません</span>
        <div class="buttonContent">
          <div class="buttonContainer cancel" @click="cancelled">破棄しない</div>
          <div class="buttonContainer ok" @click="confirmed">未入稿状態に戻す</div>
        </div>
      </div>
    </div>
  </ModalWindow>
</template>

<script>
import ModalWindow from "../common/ModalWindow";

export default {
  name: "DraftDeleteConfirmationModal",
  mixins: [],
  components: { ModalWindow },
  props: {
    isShow: {
      type: Boolean,
    },
  },
  data() {
    return {};
  },
  emits: ['confirmed', 'close'],
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

.draftDeleteCaustionText {
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
}

.ok {
  color: white;
  background: #205efb;
}

.cancel {
  color: #a0a0aa;
  font-weight: bold;
}
</style>
