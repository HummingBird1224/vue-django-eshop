export default class HeaderMenuSP {
  constructor() {
    this.$openButton = $('#js-open-header-menu-sp');
    this.$headerMenu = $('#js-menu-sp');
    this.isMenuOpen = false;

    this.$productOpenButton = $('#js-open-header-product-menu-sp');
    this.$productMenu = $('#js-header-product-menu-sp');
    this.isProductMenuOpen = false;

    this.$guideOpenButton = $('#js-open-header-guide-menu-sp');
    this.$guideMenu = $('#js-header-guide-menu-sp');
    this.isGuideMenuOpen = false;

    this.$accountOpenButton = $('#js-open-header-account-menu-sp');
    this.$accountMenu = $('#js-header-account-menu-sp');
    this.isAccountMenuOpen = false;

    this.BUTTON_ACTIVE_CLASS = 'is-active';

    this._addEvent();
  }

  _addEvent() {
    this.$openButton.on('click', evt => {
      if (!this.isMenuOpen) {
        this._openMenu();
      }
      else {
        this._closeMenu();
      }
    });

    this.$productOpenButton.on('click', evt => {
      if (!this.isProductMenuOpen) {
        this._openProductMenu();
      }
      else {
        this._closeProductMenu();
      }
    });

    this.$guideOpenButton.on('click', evt => {
      if (!this.isGuideMenuOpen) {
        this._openGuideMenu();
      }
      else {
        this._closeGuideMenu();
      }
    });

    this.$accountOpenButton.on('click', evt => {
      if (!this.isAccountMenuOpen) {
        this._openAccountMenu();
      }
      else {
        this._closeAccountMenu();
      }
    });
  }

  _openMenu() {
    this.isMenuOpen = true;
    this.$openButton.addClass(this.BUTTON_ACTIVE_CLASS);
    this.$headerMenu.slideDown();
  }

  _closeMenu() {
    this.isMenuOpen = false;
    this.$openButton.removeClass(this.BUTTON_ACTIVE_CLASS);
    this.$headerMenu.slideUp();
  }

   _openProductMenu(btn, target, trigger) {
    this.isProductMenuOpen = true;
    this.$productOpenButton.addClass(this.BUTTON_ACTIVE_CLASS);
    this.$productMenu.slideDown();
  }

  _closeProductMenu(btn, target, trigger) {
    this.isProductMenuOpen = false;
    this.$productOpenButton.removeClass(this.BUTTON_ACTIVE_CLASS);
    this.$productMenu.slideUp();
  }

   _openGuideMenu(btn, target, trigger) {
    this.isGuideMenuOpen = true;
    this.$guideOpenButton.addClass(this.BUTTON_ACTIVE_CLASS);
    this.$guideMenu.slideDown();
  }

  _closeGuideMenu(btn, target, trigger) {
    this.isGuideMenuOpen = false;
    this.$guideOpenButton.removeClass(this.BUTTON_ACTIVE_CLASS);
    this.$guideMenu.slideUp();
  }

   _openAccountMenu(btn, target, trigger) {
    this.isAccountMenuOpen = true;
    this.$accountOpenButton.addClass(this.BUTTON_ACTIVE_CLASS);
    this.$accountMenu.slideDown();
  }

  _closeAccountMenu(btn, target, trigger) {
    this.isAccountMenuOpen = false;
    this.$accountOpenButton.removeClass(this.BUTTON_ACTIVE_CLASS);
    this.$accountMenu.slideUp();
  }
}
