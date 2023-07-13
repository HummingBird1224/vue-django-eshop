<template>
  <div class="p-externalColorMeProducts-product-content-purchase">
    <div class="p-externalColorMeProducts-product-content-header">
      <svg>
        <use xlink:href='#icons-shopping_bag'/>
      </svg>
      <h3 class="g-title-tertiary">見積もりをして購入確認へ</h3>
    </div>

    <div class="p-externalBaseProducts-product-content-purchase-form">

      <SizeSelectField
        :canChange="canChangeSize"
        :form="form"
        :size="size"
        @onClick="applyFormValue"
      />

      <ColorSelectField
        v-if="colorNum && hasMultipleOptions(colorNum, 'color_num')"
        :canChange="canChangeColor"
        :form="form"
        :colorNum="colorNum"
        @onClick="applyFormValue"
      />

      <MaterialSelectField
        v-if="surfaceMaterial && hasMultipleOptions(surfaceMaterial, 'surfacea_material')"
        :canChange="canChangeMaterial"
        :form="form"
        :surfaceMaterial="surfaceMaterial"
        @onClick="applyFormValue"
      />

      <PrintAreaNumSelectField
        v-if="printAreaNum && hasMultipleOptions(printAreaNum, 'print_area_num')"
        :canChange="canChangePrintAreaNum"
        :form="form"
        :printAreaNum="printAreaNum"
        @onClick="applyFormValue"
      />

      <DesignNumSelectField
        v-if="designNum && doesMeetCondition() && hasMultipleOptions(designNum, 'design_num')"
        :canChange="canChangeDesignNum"
        :form="form"
        :designNum="designNum"
        @onClick="applyFormValue"
      />

      <QuantitySelectField
        :canChange="canChangeQuantity"
        :form="form"
        :quantity="quantity"
        :priceList="quantityPriceList"
        @onClick="applyFormValue"
      />

      <div class="p-externalColorMeProducts-product-content-purchase-footer">
        <PriceInfo
          :price="price"
        />
        <div class="p-externalColorMeProducts-product-content-purchase-footer-button">
          <form ref="createOrderForm" action="/billing/create-order/" method="POST">
            <input type="hidden" name="csrfmiddlewaretoken" :value="`${csrfToken}`">
            <button
              class="c-btn c-btn--primary"
              :class="{
                'is-disabled': !canAddCart
              }"
              @click.prevent.stop="addCart"
            >
              <svg>
                <use xlink:href='#icons-shopping_cart'/>
              </svg>
              購入する
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SizeSelectField from "./SizeSelectField";
import MaterialSelectField from "./MaterialSelectField";
import PrintAreaNumSelectField from "./PrintAreaNumSelectField";
import DesignNumSelectField from "./DesignNumSelectField";
import QuantitySelectField from "./QuantitySelectField";
import PriceInfo from "./PriceInfo";
import ColorSelectField from "./ColorSelectField";
import deepCopy from "../../../helpers/deepCopy";
import StoreMixin from "../../mixins/StoreMixin";

export default {
  name: "ProductForm",
  mixins: [StoreMixin],
  components: {ColorSelectField, PriceInfo, QuantitySelectField, PrintAreaNumSelectField,
               DesignNumSelectField, SizeSelectField, MaterialSelectField},
  data: () => ({
    isProcessing: false,
    form: {
      size: null,
      color_num: null,
      surface_material: null,
      print_area_num: null,
      design_num: null,
      quantity: null,
    },
    quantityPriceList: null,
    price: null
  }),
  props: {
    product: {
      type: Object,
      required: true,
    }
  },
  computed: {
    csrfToken() {
      return this.state.csrfToken;
    },
    canChangeSize() {
      return !this.isProcessing;
    },
    canChangeColor() {
      return !this.isProcessing &&
        this.form.size !== null;
    },
    canChangeMaterial() {
      if (this.isProcessing || this.form.size === null) {
        return false;
      }
      if (this.colorNum && this.form.color_num === null) {
        return false;
      }
      return true;
    },
    canChangePrintAreaNum() {
      if (this.isProcessing || this.form.size === null) {
        return false;
      }
      if (this.colorNum && this.form.color_num === null) {
        return false;
      }
      if (this.surfaceMaterial && this.form.surface_material === null) {
        return false;
      }
      return true;
    },
    canChangeDesignNum() {
      if (this.isProcessing || this.form.size === null) {
        return false;
      }
      if (this.colorNum && this.form.color_num === null) {
        return false;
      }
      if (this.surfaceMaterial && this.form.surface_material === null) {
        return false;
      }
      if (this.printAreaNum && this.form.print_area_num === null) {
        return false;
      }
      return true;
    },
    canChangeQuantity() {
      if (this.isProcessing || this.form.size === null) {
        return false;
      }
      if (this.colorNum && this.form.color_num === null) {
        return false;
      }
      if (this.surfaceMaterial && this.form.surface_material === null) {
        return false;
      }
      if (this.printAreaNum && this.form.print_area_num === null) {
        return false;
      }
      if (this.DesignNum && this.form.design_num === null) {
        return false;
      }
      return true;
    },
    canAddCart() {
      if (this.isProcessing || this.form.size === null) {
        return false;
      }
      if (this.colorNum && this.form.color_num === null) {
        return false;
      }
      if (this.surfaceMaterial && this.form.surface_material === null) {
        return false;
      }
      if (this.printAreaNum && this.form.print_area_num === null) {
        return false;
      }
      if (this.DesignNum && this.form.design_num === null) {
        return false;
      }
      return this.form.quantity !== null;
    },
    requireFields() {
      return this.product.required_fields;
    },
    options() {
      return this.product.options;
    },
    size() {
      return this.options.find(option => option.slug === 'size');
    },
    colorNum() {
      return this.options.find(option => option.slug === 'color_num');
    },
    surfaceMaterial() {
      return this.options.find(option => option.slug === 'surface_material');
    },
    printAreaNum() {
      return this.options.find(option => option.slug === 'print_area_num');
    },
    designNum() {
      return this.options.find(option => option.slug === 'design_num');
    },
    quantity() {
      return this.options.find(option => option.slug === 'quantity');
    },
    postValue() {
      this.doesMeetCondition();

      const postValue = {};

      if (this.form.size) {
        let s_lst = this.form.size.split(',');
        let size_data = {};
        if (s_lst.length === 2) {
          size_data = {'width': parseInt(s_lst[0]), 'height': parseInt(s_lst[1])};
        }
        else {
          size_data = {'width': parseInt(s_lst[0]), 'depth': parseInt(s_lst[1]), 'height': parseInt(s_lst[2])};
        }
        postValue.size = size_data;
      }

      if (!this.colorNum) {
        postValue.color_num = 1;
      } else {
        postValue.color_num = this.form.color_num;
      }

      if (this.surfaceMaterial) {
        postValue.surface_material = this.form.surface_material;
      }

      if (this.printAreaNum) {
        postValue.print_area_num = this.form.print_area_num;
      }

      if (this.designNum) {
        postValue.design_num = this.form.design_num;
      }

      postValue.quantity = this.form.quantity;

      return postValue;
    }
  },
  watch: {
    postValue: {
      handler: function () {
        if (this.canChangeQuantity) {
          this.calcCurrentPriceList();
        }
        if (this.canAddCart) {
          this.estimate();
        }
      },
      deep: true
    }
  },
  methods: {
    applyFormValue(value) {
      this.form = {
        ...this.form,
        ...value,
      };
    },
    doesMeetCondition() {
      const targetFormValue = this.form['print_area_num'];
      if (targetFormValue === '2') {
        return true;
      }
      else {
        this.form['design_num'] = '1';
        return false;
      }
      return true;
    },
    hasMultipleOptions(field, fieldName) {
      if (field.items.length > 1) {
        return true;
      }
      else {
        this.form[field.slug] = field.items[0].value;
        return false;
      }
    },
    calcCurrentPriceList() {
      let priceaVals = deepCopy(this.postValue);

      delete priceaVals.quantity;

      const formValue = {
        product: this.product.slug,
        options: priceaVals
      };

      this.store.postCalcPriceList(formValue)
        .then(res => {
          this.quantityPriceList = res.data.prices;
        });
    },
    estimate() {
      const formValue = {
        product: this.product.slug,
        options: deepCopy(this.postValue),
      };

      this.store.postEstimateProduct(formValue)
        .then(res => {
          this.price = res.data.prices;
        });
    },
    addCart() {
      if (this.isProcessing) {
        return;
      }

      this.isProcessing = true;

      const formValue = {
        product: this.product.slug,
        options: deepCopy(this.postValue),
      };

      this.store.postAddCart(formValue)
        .then(() => {
          // location.href = '/cart';
          this.$refs.createOrderForm.submit();
        })
        .catch(() => {
          this.isProcessing = false;
        });
    }
  }
}
</script>

<style>

</style>
