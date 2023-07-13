<template>
  <div class="customInternal">
    <div class="createCustomProductInternal">
      <div class="sectionContent">
        <form @submit.prevent="createCustomProduct">
          <div class="row">
            <div class="rowTitle">ユーザー</div>
            <div class="rowContent">
              <div class="formInput">
                <v-select id="user" name="user" :options="state.user_options" label="name" v-model="user.id" :reduce="options => options.id"/>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="rowTitle">商品名</div>
            <div class="rowContent">
              <div class="formInput">
                <input id="product_name" v-model="product.product_name" type="text" name="product_name" required/>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="rowTitle">商品説明</div>
            <div class="rowContent">
              <div class="formInput">
                <textarea id="product_detail" v-model="product.product_detail" name="product_detail" rows="5" required/>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="rowTitle">単位</div>
            <div class="rowContent">
              <div class="formInput">
                <input id="product_unit" v-model="product.product_unit" type="text" name="product_unit" required/>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="rowTitle">商品画像</div>
            <div class="rowContent">
              <div class="formInput">
                <label class="form-btn file-label">
                  画像選択
                  <input id="product_image" ref="product_image" type="file" name="product_image" accept="image/jpeg, image/png" @change="onChamgeProductImage" required/>
                </label>
                <span v-html="product_image.name" />
                <div class="formImageWrapper" v-if="product_image.url">
                  <img :src="product_image.url">
                </div>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="rowTitle">最小注文数</div>
            <div class="rowContent">
              <div class="formInput">
                <input id="min_ordering_quantity" v-model="info.min_ordering_quantity" type="number" min="0" name="min_ordering_quantity" required/>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="rowTitle">最大注文数</div>
            <div class="rowContent">
              <div class="formInput">
                <input id="max_ordering_quantity" v-model="info.max_ordering_quantity" type="number" min="0" name="max_ordering_quantity" required/>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="rowTitle">納期（初注文）</div>
            <div class="rowContent">
              <div class="formInput">
                <input id="estimated_shipping_date_first" v-model="info.estimated_shipping_date_first" type="number" min="0" name="estimated_shipping_date_first" required/>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="rowTitle">納期（再注文）</div>
            <div class="rowContent">
              <div class="formInput">
                <input id="estimated_shipping_date_repeat" v-model="info.estimated_shipping_date_repeat" type="number" min="0" name="estimated_shipping_date_repeat" required/>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="rowTitle"><label for="is_design_necessary">デザイン入稿必須</label></div>
            <div class="rowContent">
              <div class="formInput">
                <input id="is_design_necessary" v-model="info.is_design_necessary" type="checkbox" name="is_design_necessary"/>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="rowTitle"><label for="is_easy_draft_available">カンタン入稿商品</label></div>
            <div class="rowContent">
              <div class="formInput">
                <input id="is_easy_draft_available" v-model="info.is_easy_draft_available" type="checkbox" name="is_easy_draft_available"/>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="rowTitle">備考</div>
            <div class="rowContent">
              <div class="formGroup" v-for="(note, i) in notes" :key="i">
                <div class="formInput formInput--small">
                  <input :id="'note_key_'+i" v-model="note.key" type="text" :name="'note_key_'+i" placeholder="タイトル"/>
                </div>
                <div class="formInput">
                  <input :id="'note_value_'+i"  v-model="note.value" type="text" :name="'note_value_'+i" placeholder="内容"/>
                </div>
                <a class="removeListItemButton fas fa-times" href="#!" @click="() => removeNote(i)"></a>
              </div>
              <a class="addListItemButton" href="#!" @click="addNote">
                <i class="fas fa-plus"></i> 備考欄の追加
              </a>
            </div>
          </div>

          <div class="row">
            <div class="rowTitle">サイズ</div>
          </div>

          <div class="row">
            <div class="rowTitle">表示名</div>
            <div class="rowContent">
              <div class="formInput">
                <input id="size_name" v-model="options.size.name" type="text" name="size_name" required/>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="rowTitle">値</div>
            <div class="rowContent">
              <div class="formGroup">
                <div class="formInput formInput--small">
                  <input id="height" v-model="options.size.height" type="number" min="0" name="height" placeholder="高さ" required/>
                </div>
                <div class="formInput formInput--small">
                  <input id="width" v-model="options.size.width" type="number" min="0" name="width" placeholder="幅" required/>
                </div>
                <div class="formInput formInput--small">
                  <input id="depth" v-model="options.size.depth" type="number" min="0" name="depth" placeholder="奥行き"/>
                </div>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="rowTitle">価格CSV</div>
            <div class="rowContent">
              <div class="formInput">
                <label class="form-btn file-label">
                  ファイル
                  <input id="price_csv" ref="price_csv" type="file" name="price_csv" accept=".csv" @change="onChamgePriceCSV" required/>
                </label>
                <span v-html="price_csv.name" />
                <div v-if="price_csv.url">
                  <img :src="price_csv.url">
                </div>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="rowTitle">初期注文</div>
          </div>

          <div class="row">
            <div class="rowTitle">注文数</div>
            <div class="rowContent">
              <div class="formInput">
                <input id="order_quantity" v-model="order.quantity" type="number" min="0" name="order_quantity" required/>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="rowTitle">配送先</div>
            <div class="rowContent">
              <div class="formGroup">
                <div class="formInput formInput--small">
                  <v-select id="delivery_prefecture" name="delivery_prefecture" :options="state.prefecture_options" v-model="order.delivery.prefecture" placeholder="都道府県"/>
                </div>
                <div class="formInput formInput--small">
                  <input id="delivery_postal_code" v-model="order.delivery.postal_code" type="text" name="height" placeholder="郵便番号" required/>
                </div>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="rowTitle"></div>
            <div class="rowContent">
              <div class="formInput">
                <input id="delivery_city" v-model="order.delivery.city" type="text" name="delivery_city" placeholder="市区町村" required/>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="rowTitle"></div>
            <div class="rowContent">
              <div class="formInput">
                <input id="delivery_building" v-model="order.delivery.building" type="text" name="delivery_building" placeholder="建物" required/>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="rowTitle"></div>
            <div class="rowContent">
              <div class="formInput">
                <input id="delivery_tel" v-model="order.delivery.tel" type="tel" name="delivery_tel" placeholder="電話番号" required/>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="rowTitle"></div>
            <div class="rowContent">
              <div class="formInput">
                <label>
                  <input id="billing_is_not_delivery" v-model="billing_is_not_delivery" type="checkbox" name="billing_is_not_delivery"/>
                  請求先を別の住所にする
                </label>
              </div>
            </div>
          </div>

          <div v-if="billing_is_not_delivery">
            <div class="row">
              <div class="rowTitle">請求先</div>
              <div class="rowContent">
                <div class="formGroup">
                  <div class="formInput formInput--small">
                    <v-select id="billing_prefecture" name="billing_prefecture" :options="state.prefecture_options" v-model="order.billing.prefecture" placeholder="都道府県"/>
                  </div>
                  <div class="formInput formInput--small">
                    <input id="billing_postal_code" v-model="order.billing.postal_code" type="text" name="height" placeholder="郵便番号" required/>
                  </div>
                </div>
              </div>
            </div>

            <div class="row">
              <div class="rowTitle"></div>
              <div class="rowContent">
                <div class="formInput">
                  <input id="billing_city" v-model="order.billing.city" type="text" name="billing_city" placeholder="市区町村" required/>
                </div>
              </div>
            </div>

            <div class="row">
              <div class="rowTitle"></div>
              <div class="rowContent">
                <div class="formInput">
                  <input id="billing_building" v-model="order.billing.building" type="text" name="billing_building" placeholder="建物" required/>
                </div>
              </div>
            </div>

            <div class="row">
              <div class="rowTitle"></div>
              <div class="rowContent">
                <div class="formInput">
                  <input id="billing_tel" v-model="order.billing.tel" type="tel" name="billing_tel" placeholder="電話番号" required/>
                </div>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="rowTitle">デザイン</div>
            <div class="rowContent">
              <div class="formInput">
                <label class="form-btn file-label">
                  ファイル
                  <input id="design" ref="design" type="file" name="design" accept="application/pdf, application/postscript" @change="onChamgeDesign" required/>
                </label>
                <span v-html="design.name" />
                <div v-if="design.url">
                  <img :src="design.url">
                </div>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="rowTitle"></div>
            <div class="rowContent">
              <iframe class="js-data-preview" src="" width="1000" height="600"></iframe>
            </div>
          </div>

          <div class="row submitRow">
            <button class="form-btn" type="submit">
              作成
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import StoreMixin from "../../../mixins/StoreMixin"
export default {
  name: "CreateCustomProductForm",
  mixins: [StoreMixin],
  components: {},
  data: function (){
    return {
      errors: [],
      user: {
        id: null
      },
      product: {
        product_name: null,
        product_detail: null,
        product_unit: null,
      },
      product_image: {
        name: null,
        file: null,
        url: null,
      },
      info: {
        min_ordering_quantity: null,
        max_ordering_quantity: null,
        estimated_shipping_date_first: null,
        estimated_shipping_date_repeat: null,
        is_design_necessary: true,
        is_easy_draft_available: false,
      },
      notes: [
        {
          key: null,
          value: null
        }
      ],
      options: {
        size: {
          name: null,
          height: null,
          width: null,
          depth: null,
        }
      },
      price_csv: {
        name: null,
        file: null,
      },
      order: {
        quantity: null,
        delivery: {
          prefecture: null,
          postal_code: null,
          city: null,
          building: null,
          tel: null,
        },
        billing: {
          prefecture: null,
          postal_code: null,
          city: null,
          building: null,
          tel: null,
        },
      },
      billing_is_not_delivery: false,
      design: {
        name: null,
        file: null,
      },
    }
  },
  watch: {
    'user.id': function (userId) {
      if (userId) {
        $('#user input').removeAttr('required')
      } else {
        $('#user input').attr('required', true)
      }
    },
    'order.delivery.postal_code': function (postal_code) {
      new YubinBango.Core(postal_code, (addr) => {
        this.order.delivery.prefecture = addr.region;
        this.order.delivery.city = addr.locality + addr.street + addr.extended;
      });
    },
    'order.billing.postal_code': function (postal_code) {
      new YubinBango.Core(postal_code, (addr) => {
        this.order.billing.prefecture = addr.region;
        this.order.billing.city = addr.locality + addr.street + addr.extended;
      });
    }
  },
  methods: {
    onChamgeProductImage: function() {
      const file = this.$refs.product_image.files[0]
      if (file) {
        $('#product_image').removeAttr('required')
        this.product_image.name = file.name
        this.product_image.file = file
        this.product_image.url = URL.createObjectURL(file)
      }
    },
    addNote: function() {
      this.notes.push({
        key: null,
        value: null
      })
    },
    removeNote: function(index) {
      this.notes.splice(index, 1)
    },
    onChamgePriceCSV: function() {
      const file = this.$refs.price_csv.files[0]
      if (file) {
        $('#price_csv').removeAttr('required')
        this.price_csv.name = file.name
        this.price_csv.file = file
      }
    },
    onChamgeDesign: function() {
      const file = this.$refs.design.files[0]
      if (file) {
        $('#design').removeAttr('required')
        this.design.name = file.name
        this.design.file = file
        const url = window.URL.createObjectURL(file)
        const req = new XMLHttpRequest()
        req.open('GET', url, true)
        req.responseType = 'blob'
        req.onload = function () {
          const $dataPreview = $('.js-data-preview')
          if (this.status === 200) {
            $dataPreview.css({display: 'block'})
            const blobURL = window.URL.createObjectURL(new Blob([this.response], {type: 'application/pdf'}))
            $dataPreview.attr('src', blobURL)
          } else {
            $dataPreview.css({display: 'none'})
          }
        }
        req.send()
      }
    },
    createCustomProduct: function() {
      if (!this.billing_is_not_delivery) {
        this.order.billing = Object.assign({}, this.order.delivery)
      }
      const formValue = {
        user: this.user,
        product: this.product,
        info: this.info,
        options: this.options,
        notes: this.notes,
        order: this.order,
      }
      this.store.addCustomProduct(formValue)
    },
  },
  computed: {
  },
  mounted() {
    $('#user input').attr('required', true)
    $('.js-data-preview').css({display: 'none'})
  }
}
</script>

<style scoped>
</style>
