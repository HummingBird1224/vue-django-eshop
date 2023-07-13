<template>
  <div class="p-Modal-section">
    <div class="p-Modal-sectionLeft">
      <h4 class="g-title-quaternary">{{ section.title }}</h4>
    </div>
    <div class="p-Modal-printRect">
      <ul class="p-PrintRectList">
        <li
          :key="i"
          v-for="(content, i) in contents"
          class="p-PrintRect"
        >
          <div
            class="p-PrintRect-thumb"
            :style="{
              'background-image': `url(${staticUrl}${content.image})`
            }"
          ></div>
          <div class="p-PrintRect-contents">
            <p
              v-for="body in content.body"
              :key="body"
              v-html="sanitize(body)"
            />
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
  name: "HelpVerticalListLg",
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
