<template>
  <div class="p-Modal-section">
    <div class="p-Modal-sectionLeft">
      <h4 class="g-title-quaternary">{{ section.title }}</h4>
    </div>
    <div class="p-Modal-printNum">
      <p
        v-if="bodyStr"
        v-html="sanitize(bodyStr)"
      />
      <ul class="p-PrintNumList">
        <li
          v-for="content in contents"
          :key="content.image"
          class="p-PrintNum"
        >
          <div
            class="p-PrintNum-thumb"
            :style="{
              'background-image': `url(${staticUrl}${content.image})`
            }"
          ></div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import StoreMixin from "../../../../../mixins/StoreMixin";
import sanitizeHTML from 'sanitize-html';

export default {
  name: "HelpHorizontalListLg",
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
    },
    bodyStr() {
      if (this.summary && this.summary.body) {
        return this.summary.body.join('\n');
      }

      return null;
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
