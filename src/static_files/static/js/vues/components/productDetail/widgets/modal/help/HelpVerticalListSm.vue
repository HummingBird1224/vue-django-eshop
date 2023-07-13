<template>
  <div class="p-Modal-section">
    <div class="p-Modal-sectionLeft">
      <h4 class="g-title-quaternary">{{ section.title }}</h4>
    </div>
    <div class="p-Modal-cardBoardMaterial">
      <ul class="p-CardBoardMaterialList">
        <li
          v-for="content in contents"
          :key="content.title"
          class="p-CardBoardMaterial"
        >
          <div class="p-CardBoardMaterial-main">
            <div
              class="p-CardBoardMaterial-thumb"
              :style="{
                    'background-image': `url(${staticUrl}${content.image})`
                  }"
            ></div>
            <div class="p-CardBoardMaterial-contents">
              <h6 class="g-title-quinary">{{ content.title }}</h6>
              <ul
                v-if="content.body"
              >
                <li
                  v-for="body in content.body"
                  :key="body"
                  v-html="sanitize(body)"
                />
              </ul>
            </div>
          </div>
          <!--   TODO: このデータがあるnoteが作られたら実装する〜〜   -->
          <div
            v-if="content.after"
            class="p-CardBoardMaterial-supplement"
          >
            <h6 class="g-title-quinary">※表面加工オプションが選べます</h6>
            <p>特殊な加工のため、注文の際はお問い合わせ扱いになります。</p>

            <ul class="p-CardBoardMaterial-processList">
              <li class="p-CardBoardMaterial-process">
                <div
                  class="p-CardBoardMaterial-processThumb"
                  style="background-image: url('/static/img/product_detail/dummy/cardboard_material_process.png')"
                ></div>
                <div class="p-CardBoardMaterial-processContents">
                  <h6 class="g-title-quinary">マットニス</h6>
                  <p>基本的に合紙はこの加工を使います</p>
                </div>
              </li>
              <li class="p-CardBoardMaterial-process">
                <div
                  class="p-CardBoardMaterial-processThumb"
                  style="background-image: url('/static/img/product_detail/dummy/cardboard_material_process.png')"
                ></div>
                <div class="p-CardBoardMaterial-processContents">
                  <h6 class="g-title-quinary">マットニス</h6>
                  <p>基本的に合紙はこの加工を使います</p>
                </div>
              </li>
            </ul>
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
  name: "HelpVerticalListSm",
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
