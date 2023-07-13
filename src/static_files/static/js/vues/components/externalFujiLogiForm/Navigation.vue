<template>
  <div class="p-externalFujiLogiProducts-wrappedNavi">
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
        scrollToId: 'fujilogi-tape-opp-bag',
        imgUrl: 'img/external/fujilogi/navi/nav_tape.jpg',
      },
      {
        id: 2,
        name: 'ジップ付袋-圧着なし',
        scrollToId: 'fujilogi-zip-bag',
        imgUrl: 'img/external/fujilogi/navi/nav_zip.jpg',
      },
    ]
  })
}
</script>

<style>

</style>
