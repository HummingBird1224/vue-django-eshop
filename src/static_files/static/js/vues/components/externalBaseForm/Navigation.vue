<template>
  <div class="p-externalBaseProducts-wrappedNavi">
    <NavigationItem
      v-for="item in items"
      :key="item.id"
      :item="item"
    />
  </div>
</template>

<script>
import StoreMixin from "../../mixins/StoreMixin";
import NavigationItem from "./NavigationItem";

export default {
  name: "Navigation",
  components: {NavigationItem},
  mixins: [StoreMixin],
  data: () => ({
    items: [
      {
        id: 1,
        name: '宅配用A式クラフト',
        scrollToId: 'base-atype',
        imgUrl: 'img/external/base/navi/atype.png',
      },
      {
        id: 2,
        name: 'テープ付きOPP袋',
        scrollToId: 'base-tape-opp-bag',
        imgUrl: 'img/external/base/navi/tape-opp-bag.png',
      },
      {
        id: 3,
        name: 'ジップ付き袋',
        scrollToId: 'base-zip-bag',
        imgUrl: 'img/external/base/navi/zip-clear-bag.png',
      },
      {
        id: 4,
        name: '前透明アルミ袋',
        scrollToId: 'base-zip-aluminum-clear-bag',
        imgUrl: 'img/external/base/navi/zip-aluminum-clear-bag.png',
      },
      {
        id: 5,
        name: '不透明袋',
        scrollToId: 'base-tape-bag',
        imgUrl: 'img/external/base/navi/tape-bag.png',
      },
      {
        id: 6,
        name: '不透明アルミ袋',
        scrollToId: 'base-zip-aluminum-bag',
        imgUrl: 'img/external/base/navi/zip-aluminum-bag.png',
      },
      {
        id: 7,
        name: 'アルミスタンド袋',
        scrollToId: 'base-zip-aluminum-stand',
        imgUrl: 'img/external/base/navi/zip-aluminum-stand.png',
      }
    ]
  })
}
</script>

<style>

</style>
