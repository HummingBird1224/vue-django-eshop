export default {
  NOT_SUBMITTED: Symbol('not-submitted'), // 未入稿
  UNDER_CHECK: Symbol('under-check'), // 入稿チェック
  RE_SUBMITTION_REQUEST: Symbol('re-submittion-request'), // 再入稿依頼
  CHECKED: Symbol('checked'), // 最終確認
  UNASSIGNED: Symbol('unassigned'), // 配送未手配
  PRINTING: Symbol('printing'), // 印刷/加工
  SHIPPED: Symbol('shipped'), // 配送中
  DELIVERED: Symbol('delivered') // 配送済み
}
