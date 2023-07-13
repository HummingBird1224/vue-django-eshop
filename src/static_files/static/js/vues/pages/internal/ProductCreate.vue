<template>
  <div v-if="isInitialized">
    <a href="" class="backButton">
      <span class="backButtonArrow">&lt;</span>
      <span class="backButtonText">戻る</span>
    </a>

    <div class="breadcrumbsInternal">
      <div class="breadcrumbsItem">ホーム</div>
      <div class="breadcrumbsArrow">></div>
      <div class="breadcrumbsItem">商品</div>
    </div>

    <h1 class="g-title-primary pageTitleInternal">新商品追加</h1>

    <div class="p-productInternal">
      <form id="creationForm" action="">

        <div class="p-productInternal-form-item">
          <label for="">商品名</label>
          <input v-model="form.name" class="p-productInternal-form-item-text" type="text" name="name" maxlength="120" required="" id="id_name">
        </div>

        <div class="p-productInternal-form-item">
          <label for="">slug</label>
          <input v-model="form.slug" class="p-productInternal-form-item-text" type="text" name="slug" maxlength="120" required="" id="id_slug">
        </div>

        <div class="p-productInternal-form-item">
          <label for="">カテゴリー</label>
          <select v-model="form.category" class="p-productInternal-form-item-select" name="category" required="" id="id_category">
            <option value="" selected="">---------</option>
            <option v-for="(cat, i) in categories" :value="cat.id" :key="i">{{ cat.name }}</option>
          </select>
        </div>

        <div class="p-productInternal-form-item p-productInternal-form-item-top">
          <label for="">タグ</label>
          <select v-model="form.tags" class="p-productInternal-form-item-selectMulti" name="tags" required="" id="id_tags" multiple="">
            <option v-for="(t, i) in tags" :value="t.id" :key="i">{{ t.name }}</option>
          </select>
        </div>

        <div class="p-productInternal-form-item p-productInternal-form-item-top">
          <label for="">商品説明</label>
          <textarea v-model="form.overview" name="overview" cols="40" rows="10" required="" id="id_overview"></textarea>
        </div>

        <div class="p-productInternal-form-item">
          <label for="">単位</label>
          <input v-model="form.unit" class="p-productInternal-form-item-text" type="text" name="unit" maxlength="12" required="" id="id_unit" placeholder="箱、袋、etc.">
        </div>

        <div class="p-productInternal-form-images">
          <label for="">商品画像</label>
          <div class="p-productInternal-form-images-items">
            <div class="p-productInternal-form-images-item" v-for="i in imageNum" :key="i">
              <input @change="onChangeFile($event, i)" class="p-productInternal-form-item-file" type="file" accept="image/png, image/jpeg" :name="'image_' + i" required="" :id="'id_image_'+i">
              <div class="p-productInternal-form-item-sub">
                <input v-model="form.images_hover[i-1]" class="p-productInternal-form-item-checkbox" type="checkbox" :name="'image_'+ i +'_hover'" required="" :id="'id_image_'+i+'_hover'">
                <label for="">ホバー画像として使う</label>
              </div>
            </div>
            <a @click.prevent.stop="addImage" id="js-add-image-input">＋ 商品画像を追加</a>
          </div>
        </div>

        <div class="p-productInternal-form-item">
          <label for="">サイト注文可能</label>
          <input v-model="form.can_order_on_site" class="p-productInternal-form-item-checkbox" type="checkbox" name="can_order_on_site" required="" id="id_can_order_on_site">
        </div>

        <div class="p-productInternal-form-item">
          <label for="">お問い合わせ商品</label>
          <input v-model="form.is_contact_required" class="p-productInternal-form-item-checkbox" type="checkbox" name="is_contact_required" required="" id="id_is_contact_required">
        </div>

        <div class="p-productInternal-form-item">
          <label for="">サンプル提供可能</label>
          <input v-model="form.can_order_sample" class="p-productInternal-form-item-checkbox" type="checkbox" name="can_order_sample" required="" id="id_can_order_sample">
        </div>

        <div class="p-productInternal-form-item">
          <label for="">最小注文数</label>
          <input v-model="form.min_ordering_quantity" class="p-productInternal-form-item-text" type="number" name="min_ordering_quantity" min="0" required="" id="id_min_ordering_quantity">
        </div>

        <div class="p-productInternal-form-item">
          <label for="">最大注文数</label>
          <input v-model="form.max_ordering_quantity" class="p-productInternal-form-item-text" type="number" name="max_ordering_quantity" min="0" required="" id="id_max_ordering_quantity">
        </div>

        <div class="p-productInternal-form-item">
          <label for="">納期（初回）</label>
          <input v-model="form.estimated_shipping_date_first" class="p-productInternal-form-item-text" type="number" name="estimated_shipping_date_first" min="0" required="" id="id_estimated_shipping_date_first">
        </div>

        <div class="p-productInternal-form-item">
          <label for="">納期（最注文）</label>
          <input v-model="form.estimated_shipping_date_repeat" class="p-productInternal-form-item-text" type="number" name="estimated_shipping_date_repeat" min="0" required="" id="id_estimated_shipping_date_repeat">
        </div>

        <div class="p-productInternal-form-item">
          <label for="">オリジナルサイズ</label>
          <input v-model="form.can_select_original_size" class="p-productInternal-form-item-checkbox" type="checkbox" name="can_select_original_size" required="" id="id_can_select_original_size">
        </div>

        <div class="p-productInternal-form-item">
          <label for="">デザイン入稿必須</label>
          <input v-model="form.is_design_necessary" class="p-productInternal-form-item-checkbox" type="checkbox" name="is_design_necessary" required="" id="id_is_design_necessary">
        </div>

        <div class="p-productInternal-form-item">
          <label for="">色制限</label>
          <input v-model="form.choosable_color" class="p-productInternal-form-item-text" type="text" name="choosable_color" maxlength="300" required="" id="id_choosable_color">
        </div>

        <div class="p-productInternal-form-size">
          <label for="">サイズ制限</label>
          <div class="p-productInternal-form-size-items">
            <div class="p-productInternal-form-size-item">
              <label for="">高さ</label>
              <input v-model="form.sizelimit_height" class="p-productInternal-form-item-size" type="text" name="sizelimit_height" maxlength="300" required="" id="id_sizelimit_height">
            </div>
            <div class="p-productInternal-form-size-item">
              <label for="">幅</label>
              <input v-model="form.sizelimit_width" class="p-productInternal-form-item-size" type="text" name="sizelimit_width" maxlength="300" required="" id="id_sizelimit_width">
            </div>
            <div class="p-productInternal-form-size-item">
              <label for="">奥行き</label>
              <input v-model="form.sizelimit_depth" class="p-productInternal-form-item-size" type="text" name="sizelimit_depth" maxlength="300" id="id_sizelimit_depth">
            </div>
          </div>
        </div>

        <div class="p-productInternal-form-notes">
          <label for="">備考</label>
          <div class="p-productInternal-form-notes-items">
            <div class="p-productInternal-form-notes-item" v-for="i in noteNum" :key="i">
              <input v-model="form.notes[i-1].title" class="p-productInternal-form-item-note-title" type="text" :name="'note_'+ i + '_title'" required="" :id="'id_note_'+i+'_title'" placeholder="タイトル">
              <input v-model="form.notes[i-1].value" class="p-productInternal-form-item-note-content" type="text" :name="'note_'+ i +'_content'" required="" :id="'id_note_'+i+'_content'" placeholder="内容">
            </div>
            <a @click.prevent.stop="addNote" id="js-add-note-input">＋ 備考欄を追加</a>
          </div>
        </div>
        <div class="p-productInternal-form-options">
          <h4>オプション</h4>
          <p class="p-productInternal-form-note">※ サイズ(slug: size)、注文数(slug: quantity)は作成必須です。</p>
          <div class="p-productInternal-form-option" v-for="i in optionNum" :key="i">
            <div class="p-productInternal-form-option-item">
              <label for="">オプション名</label>
              <input v-model="form.options[i-1].name" class="p-productInternal-form-option-item-text" type="text" :name="'option_name_' + i" maxlength="300" required="" :id="'id_option_name_' + i">
            </div>
            <div class="p-productInternal-form-option-item">
              <label for="">説明文</label>
              <input v-model="form.options[i-1].detail" class="p-productInternal-form-option-item-text" type="text" :name="'option_detail_' + i" maxlength="300" required="" :id="'id_option_detail_' + i">
            </div>
            <div class="p-productInternal-form-option-item">
              <label for="">slug</label>
              <input v-model="form.options[i-1].slug" class="p-productInternal-form-option-item-text" type="text" :name="'option_slug_' + i" maxlength="300" required="" :id="'id_option_slug_' + i">
            </div>
            <div class="p-productInternal-form-option-item">
              <label for="">ウィジェット</label>
              <select v-model="form.options[i-1].widget" class="p-productInternal-form-item-select" :name="'option_widget_' + i" required="" :id="'id_option_widget_' + i">
                <option value="modal-radio" selected="">modal-radio</option>
                <option value="slider-sm" selected="">slider-sm</option>
                <option value="slider-lg" selected="">slider-lg</option>
                <option value="radio" selected="">radio</option>
                <option value="modal-check" selected="">modal-check</option>
              </select>
            </div>
            <div class="p-productInternal-form-option-item">
              <label for="">順番</label>
              <input v-model="form.options[i-1].ordering" class="p-productInternal-form-option-item-num" type="number" min="1" :name="'option_ordering_' + i" maxlength="300" required="" :id="'id_option_ordering_' + i">
            </div>

            <div class="p-productInternal-form-option-alternatives">
              <div class="p-productInternal-form-option-alternatives-item" v-for="j in options[i - 1]" :key="j">
                <p>選択肢 {{j}}</p>
                <div class="p-productInternal-form-option-item">
                  <label for="">表示名</label>
                  <input v-model="form.options[i-1].items[j-1].name" class="p-productInternal-form-option-item-text" type="text" :name="'option_name_' + i + '_alter_' + j" maxlength="300" required="" :id="'id_option_name_' + i + '_alter_' + j">
                </div>
                <p class="p-productInternal-form-note">※ 値がサイズのように複数ある場合は「,」のように区切り文字を指定してください</p>
                <div class="p-productInternal-form-option-item">
                  <label for="">Delimiter</label>
                  <input v-model="form.options[i-1].items[j-1].delimiter" class="p-productInternal-form-option-item-text-sm" type="text" :name="'option_delim_' + i + '_alter_' + j" maxlength="300" required="" :id="'id_option_delim_' + i + '_alter_' + j">
                </div>
                <div class="p-productInternal-form-option-item">
                  <label for="">値</label>
                  <input v-model="form.options[i-1].items[j-1].value" class="p-productInternal-form-option-item-text" type="text" :name="'option_val_' + i + '_alter_' + j" maxlength="300" required="" :id="'id_option_val_' + i + '_alter_' + j">
                </div>
                <div class="p-productInternal-form-option-item">
                  <label for="">詳細</label>
                  <input v-model="form.options[i-1].items[j-1].detail" class="p-productInternal-form-option-item-text" type="text" :name="'option_detail_' + i + '_alter_' + j" maxlength="300" required="" :id="'id_option_detail_' + i + '_alter_' + j">
                </div>
                <div class="p-productInternal-form-option-item">
                  <label for="">画像</label>
                  <input @change="onChangeOptionFile($event, i, j)" class="p-productInternal-form-option-item-file" type="file" accept="image/png, image/jpeg" :name="'option_image_' + i + '_alter_' + j" required="" :id="'id_option_image_' + i + '_alter_' + j">
                </div>
                <div class="p-productInternal-form-option-item">
                  <label for="">デフォルト値</label>
                  <input v-model="form.options[i-1].items[j-1].default" class="p-productInternal-form-option-item-checkbox" type="checkbox" :name="'option_default_' + i + '_alter_' + j" required="" :id="'id_option_default_' + i + '_alter_' + j">
                </div>
                <div class="p-productInternal-form-option-item">
                  <label for="">順番</label>
                  <input v-model="form.options[i-1].items[j-1].ordering" class="p-productInternal-form-option-item-text-sm" type="num" :name="'option_ordering_' + i + '_alter_' + j" maxlength="300" required="" :id="'id_option_ordering_' + i + '_alter_' + j">
                </div>
              </div>
              <a @click.prevent.stop="addAlternative(i)" id="js-add-note-input">＋ 選択肢を追加</a>
            </div>
          </div>
          <a @click.prevent.stop="addOption" id="js-add-note-input">＋ オプションを追加</a>
        </div>
        <button @click.prevent.stop="createProduct"  class="p-productInternal-form-submit c-btn c-btn--primary" :class="{'is-loading': isProcessing}">作成</button>
      </form>
    </div>
  </div>
</template>


<script>
import StoreMixin from "../../mixins/StoreMixin";

export default {
  name: "ProductCreate",
  mixins: [StoreMixin],
  components: {},
  data: () => ({
    isProcessing: false,
    imageNum: 1,
    noteNum: 1,
    optionNum: 1,
    options: [1],
    form: {
      name: null,
      slug: null,
      category: null,
      tags: [],
      overview: null,
      unit: null,
      images: [null],
      images_hover: [false],
      can_order_on_site: false,
      is_contact_required: false,
      can_order_sample: false,
      min_ordering_quantity: null,
      max_ordering_quantity: null,
      estimated_shipping_date_first: null,
      estimated_shipping_date_repeat: null,
      can_select_original_size: false,
      is_design_necessary: false,
      choosable_color: null,
      sizelimit_height: null,
      sizelimit_width: null,
      sizelimit_depth: null,
      notes: [{"title":"", "value": ""}],
      options: [
        {
          "name": "",
          "detail": "",
          "slug": "",
          "widget": "",
          "ordering": "",
          "items": [
            {
              "name": "",
              "delimiter": "",
              "value": "",
              "detail": "",
              "image": null,
              "default": false,
              "ordering": "",
            }
          ]
        }
      ]
    },
  }),
  components: {},
  computed: {
    isInitialized() {
      return this.state.isInitialized;
    },
    categories() {
      return this.state.categories;
    },
    tags() {
      return this.state.tags;
    }
  },
  methods: {
    addImage() {
      this.imageNum++;
      this.form.images[this.imageNum - 1] = null;
      this.form.images_hover[this.imageNum - 1] = false;
    },
    addNote() {
      this.form.notes.splice(this.noteNum, 1, {"title":"", "value": ""});
      this.noteNum++;
    },
    addOption() {
      const o = {
        "name": "",
        "detail": "",
        "slug": "",
        "widget": "",
        "ordering": "",
        "items": [
          {
            "name": "",
            "delimiter": "",
            "value": "",
            "detail": "",
            "image": null,
            "default": false,
            "ordering": "",
          }
        ]
      }
      this.form.options.splice(this.optionNum, 1, o);

      this.options.push(1);
      this.optionNum++;
    },
    addAlternative(i) {
      const a = {
        "name": "",
        "delimiter": "",
        "value": "",
        "detail": "",
        "image": null,
        "default": false,
        "ordering": "",
      }
      this.options.splice(i-1, 1, this.options[i - 1] + 1);
      this.form.options[i - 1].items.splice(this.options[i - 1], 1, a)
    },
    createProduct() {
      if (this.isProcessing) {
        return;
      }
      this.isProcessing = true;

      var _form = document.getElementById("creationForm");
      var formData = new FormData(_form);

      this.store.createProduct(formData)
        .then(() => {
          this.isProcessing = false;
        })
        .catch(e => {
          this.isProcessing = false;
          throw e;
        });
    },
    onChangeFile(e, i) {
      const file = e.target.files[0];
      var images = this.form.images;
      images[i - 1] = file;
      this.$delete(this.form, 'images')
      this.$set(this.form, 'images', images);
    },
    onChangeOptionFile(e, i, j) {
      const file = e.target.files[0];
      this.$delete(this.form.options[i-1].items[j-1], 'image')
      this.$set(this.form.options[i-1].items[j-1], 'image', file);
    }
  },
  mounted() {
    this.store.init();
  }
}
</script>
