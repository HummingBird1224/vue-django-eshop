<template>
  <ul class="p-MenuList">
    <SizeNavigation/>

    <QuantityNavigation/>

    <MaterialNavigation/>

    <SurfaceNavigation />

    <PrintAreaNavigation />

    <ColorNavigation/>

    <ProcessNavigation/>

    <BottomNavigation/>

    <EmbossNavigation/>

    <SpecialPrintNavigation/>
  </ul>
</template>

<script>
import SizeNavigation from "./SizeNavigation";
import QuantityNavigation from "./QuantityNavigation";
import ColorNavigation from "./ColorNavigation";
import MaterialNavigation from "./MaterialNavigation";
import ProcessNavigation from "./ProcessNavigation";
import BottomNavigation from "./BottomNavigation";
import EmbossNavigation from "./EmbossNavigation";
import SpecialPrintNavigation from "./SpecialPrintNavigation";
import PrintAreaNavigation from "./PrintAreaNavigation";
import SurfaceNavigation from "./SurfaceNavigation";

export default {
  name: "MenuList",
  components: {
    SurfaceNavigation,
    PrintAreaNavigation,
    SpecialPrintNavigation,
    EmbossNavigation,
    BottomNavigation,
    ProcessNavigation, MaterialNavigation, ColorNavigation, QuantityNavigation, SizeNavigation
  }
}
</script>

<style scoped>

</style>
