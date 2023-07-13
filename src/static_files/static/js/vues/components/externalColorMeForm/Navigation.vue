<template>
  <div class="p-externalColorMeProducts-wrappedNavi">
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
        name: 'テープ付きOPP袋',
        scrollToId: 'colorme-tape-opp-bag',
        imgUrl: 'img/external/colorme/navi/tape-opp-bag.png',
      },
      {
        id: 2,
        name: 'ジップ付き袋',
        scrollToId: 'colorme-zip-clear-bag',
        imgUrl: 'img/external/colorme/navi/zip-clear-bag.png',
      },
      {
        id: 3,
        name: '前透明アルミ袋',
        scrollToId: 'colorme-zip-aluminum-clear-bag',
        imgUrl: 'img/external/colorme/navi/zip-aluminum-clear-bag.png',
      },
      {
        id: 4,
        name: '不透明袋',
        scrollToId: 'colorme-tape-bag',
        imgUrl: 'img/external/colorme/navi/tape-bag.png',
      },
      {
        id: 5,
        name: '不透明アルミ袋',
        scrollToId: 'colorme-zip-aluminum-bag',
        imgUrl: 'img/external/colorme/navi/zip-aluminum-bag.png',
      },
      {
        id: 6,
        name: 'アルミスタンド袋',
        scrollToId: 'colorme-zip-aluminum-stand',
        imgUrl: 'img/external/colorme/navi/zip-aluminum-stand.png',
      }
    ]
  })
}
</script>

<style>

</style>
