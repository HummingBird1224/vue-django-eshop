export default class HeaderNoticeMenu {
  constructor() {
    this.$noticeMenu = $('#js-header-notice-menu');
    this.$openButton = $('#js-open-header-notice-menu');

    this.BUTTON_ACTIVE_CLASS = 'is-active';

    this.isOpen = false;

    if (this.$noticeMenu.length) {
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

      const $closestMenuContent = $(evt.target).closest('#js-header-notice-menu-content');
      const $closestOpenButton = $(evt.target).closest('#js-open-header-notice-menu');

      if (!$closestMenuContent.length && !$closestOpenButton.length) {
        this._closeMenu();
      }
    });
  }

  _openMenu() {
    this.isOpen = true;

    this.$openButton.addClass(this.BUTTON_ACTIVE_CLASS);
    this.$noticeMenu.fadeIn(100);
  }

  _closeMenu() {
    this.isOpen = false;

    this.$openButton.removeClass(this.BUTTON_ACTIVE_CLASS);
    this.$noticeMenu.fadeOut(100);
  }
}
