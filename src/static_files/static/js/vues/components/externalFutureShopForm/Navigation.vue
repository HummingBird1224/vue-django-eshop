<template>
  <div class="p-externalFutureShopProducts-wrappedNavi">
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
        scrollToId: 'futureshop-tape-opp-bag',
        imgUrl: 'img/external/futureshop/navi/tape-opp-bag.png',
      },
      {
        id: 2,
        name: 'ジップ付き袋',
        scrollToId: 'futureshop-zip-clear-bag',
        imgUrl: 'img/external/futureshop/navi/zip-clear-bag.png',
      },
      {
        id: 3,
        name: '前透明アルミ袋',
        scrollToId: 'futureshop-zip-aluminum-clear-bag',
        imgUrl: 'img/external/futureshop/navi/zip-aluminum-clear-bag.png',
      },
      {
        id: 4,
        name: '不透明袋',
        scrollToId: 'futureshop-tape-bag',
        imgUrl: 'img/external/futureshop/navi/tape-bag.png',
      },
      {
        id: 5,
        name: '不透明アルミ袋',
        scrollToId: 'futureshop-zip-aluminum-bag',
        imgUrl: 'img/external/futureshop/navi/zip-aluminum-bag.png',
      },
      {
        id: 6,
        name: 'アルミスタンド袋',
        scrollToId: 'futureshop-zip-aluminum-stand',
        imgUrl: 'img/external/futureshop/navi/zip-aluminum-stand.png',
      }
    ]
  })
}
</script>

<style>

</style>
