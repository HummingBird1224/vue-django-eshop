<template>
  <div class="p-Modal-section">
    <div class="p-Modal-sectionLeft">
      <h4 class="g-title-quaternary">{{ section.title }}</h4>
    </div>
    <div class="p-Modal-flatBagProcess">
      <ul class="p-FlatBagProcessTypeList">
        <li
          v-for="row in section.rows"
          :key="row.title"
          class="p-FlatBagProcessType"
        >
          <h5 class="g-title-quinary">{{ row.title }}</h5>
          <ul class="p-FlatBagProcessList">
            <li
              v-for="content in row.contents"
              :key="content.title"
              class="p-FlatBagProcess"
            >
              <div
                class="p-FlatBagProcess-thumb"
                :style="{
                  'background-image': `url(${staticUrl}${content.image})`
                }"
              ></div>
              <div class="p-FlatBagProcess-contents">
                <h6 class="g-title-quinary">{{ content.title }}</h6>
                <p
                  v-for="body in content.body"
                  :key="body"
                  v-html="sanitize(body)"
                />
              </div>
            </li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import StoreMixin from "../../../../../mixins/StoreMixin";
import sanitizeHTML from 'sanitize-html';

export default {
  name: "HelpGridListMd",
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
