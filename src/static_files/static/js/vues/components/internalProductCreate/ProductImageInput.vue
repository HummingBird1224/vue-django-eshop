<template>
  <div class="p-productInternal-form-images-item">
    <input class="p-productInternal-form-item-file" type="file" accept="image/png, image/jpeg" :name="'image_' + id" required="" :id="'id_image_'+id">
    <div class="p-productInternal-form-item-sub">
      <input class="p-productInternal-form-item-checkbox" type="checkbox" :name="'image_'+ id +'_hover'" required="" :id="'id_image_'+id+'_hover'">
      <label for="">ホバー画像として使う</label>
    </div>
  </div>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin";

export default {
  name: "ProductImageInput",
  mixins: [StoreMixin],
  components: {},
  props: {
    id: {
      type: String,
      required: true,
    }
  }
}
</script>
