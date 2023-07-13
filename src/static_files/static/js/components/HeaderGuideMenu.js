export default class HeaderGuideMenu {
  constructor() {
    this.$productMenu = $('#js-header-guide-menu');
    this.$openButton = $('#js-open-header-guide-menu');

    this.BUTTON_ACTIVE_CLASS = 'is-active';

    this.isOpen = false;

    if (this.$productMenu.length) {
      this._addEvent();
    }
  }

  _addEvent() {
    this.$openButton.on('mouseover', evt => {
      this._openMenu();
    });

    $(document).on('mouseover', evt => {
      if (!this.isOpen) {
        return;
      }

      const $closestMenuContent = $(evt.target).closest('#js-header-guide-menu-content');
      const $closestOpenButton = $(evt.target).closest('#js-open-header-guide-menu');

      if (!$closestMenuContent.length && !$closestOpenButton.length) {
        this._closeMenu();
      }
    });
  }

  _openMenu() {
    this.isOpen = true;

    this.$openButton.addClass(this.BUTTON_ACTIVE_CLASS);
    this.$productMenu.fadeIn(100);
  }

  _closeMenu() {
    this.isOpen = false;

    this.$openButton.removeClass(this.BUTTON_ACTIVE_CLASS);
    this.$productMenu.fadeOut(100);
  }
}
