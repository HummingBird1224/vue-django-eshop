<template>
  <div class="p-File-checkResult">
    <h5 class="g-title-quinary">
      <svg class="error">
        <use xlink:href='#icons-warning'/>
      </svg>
      チェック結果：データに不備が見つかりました。
    </h5>

    <p>以下の項目を修正して、データを再入稿しましょう。</p>
    <a class="c-textLink" href="#">データの作成方法についてはこちら</a>

    <ul class="p-File-checkResultList" v-if="orderInfo">
      <li v-for="comment in orderInfo.design.comments">
        <label class="c-form-checkbox">
          <input class="c-form-checkboxInput" type="checkbox">
          <span class="c-form-checkboxMark">
                <i class="material-icons">done</i>
              </span>
          {{ comment }}
        </label>
      </li>
    </ul>
  </div>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin";

export default {
  name: "FileCheckFailed",
  mixins: [StoreMixin],
  computed: {
    orderInfo() {
      return this.state.orderInfo;
    }
  }
}
</script>

<style scoped>

</style>
