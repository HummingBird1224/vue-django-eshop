<template>
  <ModalWindow :isShow="isShow" class="c-modal--white" @close="close">
    <div class="modal-contents__wrapper">
      <div class="modal-contents__header">
        <span class="contents-title__label">{{ title }}</span>
        <div class="modal-contents__closeBtn" @click="close()">
          <img :src="staticUrl + 'img/modal-close__btn.png'" />
        </div>
      </div>
      <div class="modal-contents__contents-wrapper">
        <div
          class="modal-contents__contents-container"
          v-for="(content, i) in contents"
          :key="i"
        >
          <div v-if="hasChild(content)">
            <span class="contents-text__headline">{{ content.headline }}</span>
            <span
              v-if="content.description"
              class="contents-text__description"
              >{{ content.description }}</span
            >
          </div>
          <span
            class="contents-text__description"
            v-else-if="
              !hasChild(content) && !isMedia(content) && !isLink(content)
            "
            >{{ content }}</span
          >
          <div
            class="contents-media"
            v-else-if="!hasChild(content) && isMedia(content)"
          >
            <img :src="staticUrl + content.src" />
          </div>
          <div class="contents-link" v-else-if="isLink(content)">
            <a :href="content.link">{{ linkText(content) }}</a>
          </div>
        </div>
      </div>
    </div>
  </ModalWindow>
</template>

<script>
import ModalWindow from "./ModalWindow";
export default {
  name: "ExplanationModal",
  components: {
    ModalWindow,
  },
  props: {
    isShow: {
      type: Boolean,
    },
    title: {
      type: String, //
    },
    contents: {
      type: Array, // コンテンツの実体
    },
    staticUrl: {
      type: String
    }
  },
  emits: ['close'],
  methods: {
    close: function () {
      this.$emit("close");
    },
    hasChild: (content) => {
      return content.hasOwnProperty("headline");
    },
    isMedia: (content) => content.hasOwnProperty("src"),
    isLink: (content) => content.hasOwnProperty("link"),
    linkText: (content) =>
      content.hasOwnProperty("text") ? content.text : content.link,
  },
};
</script>

<style lang="scss" scoped>
.c-modal {
  display: flex;
  justify-content: center;
  align-items: center;
}
.modal-contents {
  &__wrapper {
    width: 680px;
    max-height: 90vh;
    border-radius: 16px;
    background: white;
    padding: 32px;
    box-shadow: 2px 2px 16px rgba(0, 0, 0, 0.12);
  }
  &__header {
    height: 50px;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 16px;
    border-bottom: 1px solid #dadbdd;
    .contents-title__label {
      font-weight: bold;
      font-size: 20px;
      line-height: 28px;
    }
  }
  &__contents-wrapper {
    max-height: calc(90vh - 100px);
    overflow-y: scroll;
    .contents-text__headline {
      display: block;
      width: 100%;
      font-weight: bold;
      font-size: 16px;
      line-height: 28px;
    }
    .contents-text__description {
      white-space: pre-line;
      font-size: 14px;
      line-height: 24px;
      letter-spacing: 0.8px;
    }
    .contents-media {
      display: flex;
      justify-content: center;
      align-items: center;
      width: 100%;
    }
    .contents-link {
    }
  }
  &__contents-container {
    padding: 12px 0px;
  }
  &__closeBtn {
    cursor: pointer;
    width: 24px;
    height: 24px;
  }
}
</style>
