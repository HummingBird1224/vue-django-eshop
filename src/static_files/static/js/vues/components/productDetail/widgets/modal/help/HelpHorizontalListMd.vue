<template>
  <div class="p-Modal-section">
    <div class="p-Modal-sectionLeft">
      <h4 class="g-title-quaternary">{{ section.title }}</h4>
    </div>
    <div class="p-Modal-flatBagMaterial">
      <h5
        v-if="summary"
        class="p-Modal-flatBagMaterialTitle"
      >
        {{ summary.title }}
      </h5>

      <ul class="p-FlatBagMaterialList">
        <li
          v-for="content in contents"
          :key="content.title"
          class="p-FlatBagMaterial"
        >
          <div
            class="p-FlatBagMaterial-thumb"
            :style="{
              'background-image': `url(${staticUrl}${content.image})`
            }"
          ></div>
          <div class="p-FlatBagMaterial-contents">
            <h6 class="g-title-quinary">{{ content.title }}</h6>
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
  name: "HelpHorizontalListMd",
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
