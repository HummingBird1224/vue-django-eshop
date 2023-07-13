<template>
  <div class="p-Modal-section">
    <div class="p-Modal-sectionLeft">
      <h4 class="g-title-quaternary">{{ section.title }}</h4>
    </div>
    <div class="p-Modal-materialColor">
      <ul class="p-MaterialColorList">
        <li
          :key="content.title"
          v-for="content in contents"
          class="p-MaterialColor"
        >
          <div
            class="p-MaterialColor-thumb"
            :style="{
              'background-image': `url(${staticUrl}${content.image})`
            }"
          ></div>
          <div class="p-MaterialColor-contents">
            <h6 class="g-title-quinary">{{ content.title }}</h6>
            <template
              v-if="content.body"
            >
              <p
                v-for="body in content.body"
                :key="body"
                v-html="sanitize(body)"
              />
            </template>
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
  name: "HelpVerticalListMd",
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
