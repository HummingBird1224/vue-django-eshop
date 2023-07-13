<template>
  <div class="p-Modal-section">
    <div class="p-Modal-sectionLeft">
      <h4 class="g-title-quaternary">{{ section.title }}</h4>
    </div>
    <div class="p-Modal-colorPrice">
      <div
        v-if="summary"
        class="p-ModalSummary"
      >
        <h5 class="g-title-quinary p-ModalSummary-title">{{ summary.title }}</h5>
        <ul
          v-if="summary.body"
          class="p-ModalSummary-contents"
        >
          <li
            v-for="body in summary.body"
            :key="body"
            v-html="`・${sanitize(body)}`"
          />
        </ul>
      </div>
      <ul class="p-ColorPriceList">
        <li
          v-for="content in contents"
          :key="content.title"
          class="p-ColorPrice"
        >
          <div
            class="p-ColorPrice-thumb"
            :style="{
              'background-image': `url(${staticUrl}${content.image})`
            }"
          ></div>
          <div class="p-ColorPrice-contents">
            <h6 class="g-title-quinary">{{ content.title }}</h6>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import StoreMixin from "../../../../../mixins/StoreMixin";
import sanitizeHTML from 'sanitize-html';

export default {
  name: "HelpHorizontalListSm",
  mixins: [StoreMixin],
  props: {
    section: {
      type: Object,
      required: true
    }
  },
  computed: {
    staticUrl() {
      return this.state.staticUrl;
    },
    contents() {
      return this.section.contents;
    },
    summary() {
      return this.section.summary;
    }
  },
  methods: {
    sanitize(html) {
      return sanitizeHTML(html, {
        allowedTags: ['span'],
        allowedAttributes: {
          span: ['class', 'data-link']
        },
      });
    }
  }
}
</script>

<style scoped>

</style>
