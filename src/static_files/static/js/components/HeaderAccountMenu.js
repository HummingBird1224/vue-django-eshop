export default class HeaderAccountMenu {
  constructor() {
    this.$accountMenu = $('#js-header-account-menu');
    this.$openButton = $('#js-open-header-account-menu');

    this.BUTTON_ACTIVE_CLASS = 'is-active';

    this.isOpen = false;

    if (this.$accountMenu.length) {
      this._addEvent();
    }
  }

  _addEvent() {
    this.$openButton.on('mouseover', evt => {
      evt.preventDefault();
      evt.stopPropagation();

      if (!this.isOpen) {
        this._openMenu();
      }
    });

    $(document).on('mouseover', evt => {
      if (this.isOpen && $(evt.target).closest('#js-header-account-menu').length <= 0) {
        this._closeMenu();
      }
    })
  }

  _openMenu() {
    this.isOpen = true;

    this.$openButton.addClass(this.BUTTON_ACTIVE_CLASS);
    this.$accountMenu.fadeIn(100);
  }

  _closeMenu() {
    this.isOpen = false;

    this.$openButton.removeClass(this.BUTTON_ACTIVE_CLASS);
    this.$accountMenu.fadeOut(100);
  }
}
