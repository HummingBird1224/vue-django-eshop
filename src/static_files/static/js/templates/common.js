import ColorListModal from "../components/ColorListModal";
import HeaderProductMenu from "../components/HeaderProductMenu";
import HeaderGuideMenu from "../components/HeaderGuideMenu";
import HeaderMenuSP from "../components/HeaderMenuSP";
import ProductListImageToggler from "../components/ProductListImageToggler";
import HeaderAccountMenu from "../components/HeaderAccountMenu";
import HeaderNoticeMenu from "../components/HeaderNoticeMenu";
import ExternalLink from "../components/ExternalLink";

/**
 * 初期化.
 */
const initPage = () => {
  new HeaderProductMenu();
  new HeaderGuideMenu();
  new HeaderAccountMenu();
  new HeaderNoticeMenu();
  new HeaderMenuSP();

  const $colorListModal = $('#js-color-list-modal');

  if ($colorListModal.length) {
    new ColorListModal($colorListModal);
  }

  const $productListItems = $(".p-products .p-ProductList .p-Product");

  if ($productListItems.length) {
    $productListItems.each((i, el) => new ProductListImageToggler($(el)));
  }

  new ExternalLink();
};

$(document).ready(initPage);
