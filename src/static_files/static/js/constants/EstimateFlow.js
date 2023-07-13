export default {
  TOP: Symbol('top'), // トップ.
  BOTTOM: Symbol('bottom'), // 底(紙器)
  COLOR: Symbol('color'), // 色.
  EMBOSS: Symbol('emboss'), // エンボス/デボス(紙器)
  FLAT_BAG_MATERIAL: Symbol('flatBagMaterial'), // 素材(平袋)
  PRINT_AREA: Symbol('printArea'), // 印刷面(ダンボール/紙器)
  PROCESS: Symbol('process'), // ノッチ(平袋), 角丸(平袋), ジッパー(ダンボール)
  SPECIAL_PRINT: Symbol('specialPrint'), // 紙器 特殊加工.
  SURFACE: Symbol('surface'), // 表面素材(ダンボール/紙器), 表面加工(ダンボール/紙器).

  /**************************************************************************************
   * -------  削除
   **************************************************************************************/
  CARD_BOARD_THICKNESS: Symbol('cardBoardThickness'), // ダンボール 厚さ.
}
