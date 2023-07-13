import axios from 'axios';

class ApiManager {
  constructor() {
    axios.defaults.headers.common = {
      'X-Requested-With': 'XMLHttpRequest',
      'X-CSRFToken': $('#csrf-token').data('token'),
    };

    this.httpClient = axios.create();
  }

  /**
   * 支払時の注文詳細
   * @returns {Promise<AxiosResponse<T>>}
   */
  getBillingOrderInfo() {
    return this.httpClient.get(`/api/billing/order-info/`);
  }

  /**
   * 決済
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postBillingCharge(formValue) {
    return this.httpClient.post(`/api/billing/charge/`, formValue);
  }

  /**
   * お届先住所の送信
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postCreateDeliveryAddress(formValue) {
    return this.httpClient.post(`/api/billing/create-delivery-address/`, formValue);
  }

  /**
   * 請求先住所の送信
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postCreateBillingAddress(formValue) {
    return this.httpClient.post(`/api/billing/create-billing-address/`, formValue);
  }

  /**
   * 注文一覧の取得
   * @param nextUrl
   * @returns {Promise<AxiosResponse<T>>}
   */
  getOrders(nextUrl = null) {
    let url = `/api/orders/`
    if (nextUrl) url = nextUrl;
    return this.httpClient.get(url);
  }

  /**
   * 入稿情報の取得
   * @param refCode
   * @returns {Promise<AxiosResponse<T>>}
   */
  getDraftOrderInfo(refCode) {
    return this.httpClient.get(`/orders/history/${refCode}/state/`);
  }

  /**
   * カンタン入稿画面に必要な情報を取得する
   * @param refCode
   */
  getEasyDraftInfo(refCode) {
    return this.httpClient.get(`/api/orders/draft/${refCode}/`);
  }

  /**
   * アップロードしたデザインを取り下げる
   * @param {*} refCode
   */
  withdrawUploadedDraftData(refCode) {
    return this.httpClient.post(`/api/orders/${refCode}/design/reset/`);
  }

  /**
   * カンタン入稿PDFファイルをアップロード
   * @param refCode
   * @param formValue
   * @param onUploadProgress
   * @returns {Promise<AxiosResponse<T>>}
   */
  postEasyDraftUpload(refCode, formValue, onUploadProgress = () => {}) {
    const config = {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
      onUploadProgress
    };

    return this.httpClient.post(`/api/orders/draft/${refCode}/upload/`, formValue, config);
  }


  /**
   * デザインファイルをアップロード
   * @param refCode
   * @param formValue
   * @param onUploadProgress
   * @returns {Promise<AxiosResponse<T>>}
   */
  postUploadDesign(refCode, formValue, onUploadProgress = () => {}) {
    const config = {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
      onUploadProgress
    };

    return this.httpClient.post(`/orders/history/${refCode}/design/upload/`, formValue, config);
  }

  /**
   * アップロードしたデザインを承認.
   * @param refCode
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postConfirmUpload(refCode, formValue) {
    return this.httpClient.post(`/orders/history/${refCode}/design/upload/confirm/`, formValue);
  }

  /**
   * 入稿したデザインを承認.（注文を完了）
   * @param refCode
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postConfirmDesign(refCode, formValue) {
    return this.httpClient.post(`/orders/history/${refCode}/design/confirm/`, formValue);
  }

  /**
   * 注文をキャンセル.
   * @param refCode
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postCancelOrder(refCode, formValue) {
    return this.httpClient.post(`/api/orders/${refCode}/cancel/`, formValue);
  }

  /**
    * 再注文用の注文情報取得
    * @param refCode
    * @returns {Promise<AxiosResponse<T>>}
    */
  getReorderInfo(refCode) {
    return this.httpClient.get(`/api/orders/reorder/${refCode}/`);
  }

   /**
    * 再注文
    * @param refCode
    * @param formValue
    * @returns {Promise<AxiosResponse<T>>}
    */
   postReorder(refCode, formValue) {
     return this.httpClient.post(`/api/orders/reorder/${refCode}/add/`, formValue)
   }

  /**
   * サインアップ
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postUserSignUp(formValue) {
    return this.httpClient.post(`/accounts/signup/api/`, formValue);
  }

  /**
   * マイデザイン一蘭取得
   * @returns {Promise<AxiosResponse<T>>}
   */
  getMyDesigns() {
    return this.httpClient.get("/api/accounts/mydesign");
  }

  /**
   * マイデザイン名変更
   * @param name
   * @returns
   */
  updateMyDesignName(id, newName) {
    return this.httpClient.post(`/api/accounts/mydesign/${id}/rename/`, { name: newName });
  }

  /**
   * 再注文
   * @returns {Promise<AxiosResponse<T>>}
  */
  getReorderMyDesign(id) {
    return this.httpClient.get(`/api/accounts/mydesign/${id}/reorder`);
  }

  /**
   * マイデザインからカート追加
   * @param designId
   * @param quantity
   * @param options
   * @param productSlug
   * @returns
   */
  addCartFromMyDesign(designId, quantity, options, productSlug) {
    const postFormValue = {
      "options": {
        ...options,
        ...{
          "quantity": quantity,
          "mydesign_id": designId,
          "from_mydesign": true,
        }
      },
      "product": productSlug,
    }

    return this.httpClient.post(`/api/cart/add/`, postFormValue)
  }

  /**
   *  今すぐ買うボタンで集計処理をかける
   * @param designId
   * @param quantity
   * @param options
   * @param productSlug
   */
  getInstantBuyRequirementsInfo(designId, quantity, options, productSlug) {
    const postFormValue = {
      "options": {
        ...options,
        ...{
          "quantity": quantity,
          "mydesign_id": designId,
          "from_mydesign": true,
        }
      },
      "product": productSlug,
    }

    return this.httpClient.post(`/api/billing/instantbuy/`, postFormValue)
  }

  /**
   * 価格見積もり問い合わせAPI
   * @param lots
   * @param options
   * @param productSlug
   */

  getEstimatedList(productSlug, options, lots) {
    const postFormValue = {
      "options": options,
      "lots": lots
    }
    return this.httpClient.post(`/api/products/${productSlug}/estimate/list/`, postFormValue)
  }

  /**
   * 今すぐ買う画面に出てくるクレジットカード一覧を取得する
   * @returns
   */
  getCreditCardListForInstantBuy() {
    return this.httpClient.get(`/api/accounts/credit`)
  }

  /**
   * 今すぐ買う画面に出てくるクレジットカードデフォルト指定を変更
   * @returns
   */
  updateInstantBuyDefaultCreditCart(paymentCardId) {
    return this.httpClient.post(`/api/accounts/credit/change/`, { id: paymentCardId })
  }

  /**
   * 今すぐ買う画面に出てくる発送先一覧を取得する
   * @returns
   */
  getShippingAddressListForInstantBuy() {
    return this.httpClient.get(`/api/accounts/address/`)
  }

  /**
   * 今すぐ買う画面に出てくる発送先デフォルト指定を変更
   * @returns
   */
  updateInstantBuyDefaultShippigAddress(addressId) {
    return this.httpClient.post(`/api/accounts/address/change/`, { id: addressId })
  }

  /**
   * 今すぐ購入APIを叩く
   * @param {*} productSlug
   * @returns
   */
  orderInstantBuy(productSlug, options, quantity, designId, cardId, addressId, paymentMethod) {
    const postFormValue = {
      "options": {
        ...options,
        ...{
          "quantity": quantity,
          "mydesign_id": designId,
          "from_mydesign": true,
        }
      },
      "product": productSlug,
      "card_id": cardId,
      "address_id": addressId,
      "payment_method": paymentMethod,
    }
    return this.httpClient.post(`/api/billing/instantbuy/charge/`, postFormValue)
  }

  /**
   * 商品情報の取得
   * @param productSlug
   * @returns {Promise<AxiosResponse<T>>}
   */
  getProductInfo(productSlug) {
    return this.httpClient.get(`/api/products/${productSlug}/`);
  }

  /**
   * 商品の価格計算（見積もりページ）
   * @param productSlug
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postCalcEstimate(productSlug, formValue) {
    return this.httpClient.post(`/api/products/${productSlug}/estimate/`, formValue);
  }

  /**
   * 商品の価格計算（商品詳細ページ）
   * @param productSlug
   * @param formValue
   * @param cancelToken
   * @returns {Promise<AxiosResponse<T>>}
   */
  postCalcEstimateList(productSlug, formValue, cancelToken) {
    return this.httpClient.post(`/api/products/${productSlug}/estimate/list/`, formValue, { cancelToken });
  }

  /**
   * 商品をカートに追加
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postAddCart(formValue) {
    return this.httpClient.post('/api/cart/add/', formValue);
  }

  /**
   * カート情報取得
   * @returns {Promise<AxiosResponse<T>>}
   */
  getCart() {
    return this.httpClient.get('/api/cart/');
  }

  /**
   * カートアイテム削除
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postCartItemDelete(formValue) {
    return this.httpClient.post('/api/cart/delete/', formValue);
  }
  
  /**
   * Thank You 画面情報取得
   * @param refCode
   * @returns {Promise<AxiosResponse<T>>}
   */
  getBillingThankyou(refCode) {
    return this.httpClient.get(`/api/billing/thankyou/${refCode}/`);
  }

  /**
   * BASEの商品リストを取得
   * @returns {Promise<AxiosResponse<T>>}
   */
  getBaseProducts() {
    return this.httpClient.get('/api/external/base/products/');
  }

  /**
   * BASEの商品に対する選択肢ごとの合計金額を取得
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postCalcBasePriceList(formValue) {
    return this.httpClient.post('/api/external/base/products/pricelist/', formValue);
  }

  /**
   * BASEの商品を見積もり
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postEstimateBaseProduct(formValue) {
    return this.httpClient.post('/api/external/base/products/estimate/', formValue);
  }

  /**
   * ColoMeの商品リストを取得
   * @returns {Promise<AxiosResponse<T>>}
   */
  getColormeProducts() {
    return this.httpClient.get('/api/external/colorme/products/');
  }

   /**
   * ColoMeの商品に対する選択肢ごとの合計金額を取得
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postCalcColorMePriceList(formValue) {
    return this.httpClient.post('/api/external/colorme/products/pricelist/', formValue);
  }

  /**
   * ColoMeの商品を見積もり
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postEstimateColorMeProduct(formValue) {
    return this.httpClient.post('/api/external/colorme/products/estimate/', formValue);
  }

  /**
   * FujiLogiの商品リストを取得
   * @returns {Promise<AxiosResponse<T>>}
   */
  getFujiLogiProducts() {
    return this.httpClient.get('/api/external/fujilogi/products/');
  }

   /**
   * FujiLogiの商品に対する選択肢ごとの合計金額を取得
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postCalcFujiLogiPriceList(formValue) {
    return this.httpClient.post('/api/external/fujilogi/products/pricelist/', formValue);
  }

  /**
   * FujiLogiの商品を見積もり
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postEstimateFujiLogiProduct(formValue) {
    return this.httpClient.post('/api/external/fujilogi/products/estimate/', formValue);
  }

  /**
   * FutureShopの商品リストを取得
   * @returns {Promise<AxiosResponse<T>>}
   */
  getFutureShopProducts() {
    return this.httpClient.get('/api/external/futureshop/products/');
  }

   /**
   * FutureShopの商品に対する選択肢ごとの合計金額を取得
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postCalcFutureShopPriceList(formValue) {
    return this.httpClient.post('/api/external/futureshop/products/pricelist/', formValue);
  }

  /**
   * FutureShopの商品を見積もり
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postEstimateFutureShopProduct(formValue) {
    return this.httpClient.post('/api/external/futureshop/products/estimate/', formValue);
  }

  /**
   * カテゴリリストの取得
   * @returns {Promise<AxiosResponse<T>>}
   */
  getProductCategory() {
    return this.httpClient.get(`/api/products/category/`);
  }

  /**
   * 商品一覧の商品リストの取得
   * @returns {Promise<AxiosResponse<T>>}
   */
  getProductList(categorySlug) {
    return this.httpClient.get(`/api/products/list/${categorySlug}/`);
  }

  /**
   * カスタム商品作成のためのユーザー取得
   * @returns {Promise<AxiosResponse<T>>}
   */
  getCustomProductUsers() {
    return this.httpClient.get('/api/internal/custom-product/');
  }

  /**
   * カスタム商品追加
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  addCustomProduct(formValue) {
    return this.httpClient.post('/api/internal/custom-product/add/', formValue);
  }
  
  /**
   * クレカ取得
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  getAccountsCredit(formValue) {
    return this.httpClient.get(`/api/accounts/credit/`, formValue);
  }

  /**
   * クレカ作成
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postAccountsCreditCreate(formValue) {
    return this.httpClient.post(`/api/accounts/credit/create/`, formValue);
  }

  /**
   * クレカ削除
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postAccountsCreditDelete(formValue) {
    return this.httpClient.post(`/api/accounts/credit/delete/`, formValue);
  }

  /**
   * クレカデフォルト化
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postAccountsCreditChange(formValue) {
    return this.httpClient.post(`/api/accounts/credit/change/`, formValue);
  }

  /**
   * クレカ取得
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  getAccountsAddress(formValue) {
    return this.httpClient.get(`/api/accounts/address/`, formValue);
  }

  /**
   * クレカ作成
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postAccountsAddressCreate(formValue) {
    return this.httpClient.post(`/api/accounts/address/create/`, formValue);
  }

  /**
   * クレカ削除
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postAccountsAddressDelete(formValue) {
    return this.httpClient.post(`/api/accounts/address/delete/`, formValue);
  }

  /**
   * クレカデフォルト化
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postAccountsAddressChange(formValue) {
    return this.httpClient.post(`/api/accounts/address/change/`, formValue);
  }

  /**
   * お知らせリストの取得
   * @returns {Promise<AxiosResponse<T>>}
   */
  getNoticeList(url='/api/notices/') {
    return this.httpClient.get(url);
  }

  /**
   * 既読にする
   * @params notice_id
   * @returns {Promise<AxiosResponse<T>>}
   */
  readNotice(notice_id) {
    return this.httpClient.post(`/api/notices/read/`, { "notice_id": notice_id });
  }

  /**
   * お知らせ投稿の取得
   * @params id
   * @returns {Promise<AxiosResponse<T>>}
   */
  getNotice(id) {
    return this.httpClient.get(`/api/notices/${id}/`);
  }

  /****  管理画面   ****/
  /**
   * 商品追加用カテゴリータグリスト
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  getInternalProductCreateCatNTagList() {
    return this.httpClient.get(`/api/internal/products/create/cat-n-tag-list/`);
  }

  /**
   * 商品追加
   * @param formValue
   * @returns {Promise<AxiosResponse<T>>}
   */
  postInternalProductCreate(formValue, onUploadProgress = () => {}) {
    const config = {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
      onUploadProgress
    };
    return this.httpClient.post(`/api/internal/products/create/`, formValue);
  }

  /**
   * お知らせ投稿リスト
   * @returns {Promise<AxiosResponse<T>>}
   */
  getInternalNoticePostList(url,keyword='') {
    if(!url) { url = `/api/internal/notices/?keyword=${keyword}`}
    return this.httpClient.get(url);
  }

  /**
   * カテゴリリストの取得
   * @returns {Promise<AxiosResponse<T>>}
   */
  getCaseStudyCategory() {
    return this.httpClient.get(`/api/case_studies/category/`);
  }

  /**
   * 商品一覧の商品リストの取得
   * @returns {Promise<AxiosResponse<T>>}
   */
  getCaseStudyList(category, tag) {
    // console.log(category, tag)
    return this.httpClient.get(`/api/case_studies/${category}/${tag}`);
    // return this.httpClient.get(`/api/case_studies/list`);
  }
  
  getCaseStudy(slug){
    return this.httpClient.get(`/api/case_studies/${slug}`);
  }

  getCaseStudySameTagList(category, tag, slug){
    return this.httpClient.get(`/api/case_studies/${category}/${tag}/${slug}`)
  }

  getCaseStudyCategoryObject(tag){
    return this.httpClient.get(`/api/case_studies/${tag}`)
  }
}

export default new ApiManager();

