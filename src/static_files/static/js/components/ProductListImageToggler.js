export default class ProductListImageToggler {
  constructor($el) {
    this.$listItem = $el;
    this.$thumb = this.$listItem.find('.p-ProductThumb img');
    this.$photoList = this.$listItem.find('.p-ProductPhotos');
    this.$photo = this.$listItem.find('.p-ProductPhoto');
    this.currentImgUrl = this.$thumb.attr('src');
    this.hoverImgUrl = this.$thumb.data('hover-image-url');
    this.IS_CURRENT_CLASS = 'is-current';

    this._addEvent();
  }

  _addEvent() {
    this.$photo.on('click', evt => {
      this._toggleImage($(evt.target));
    });

    this.$thumb.on({
      mouseenter: () => this._setHoverImage(),
      mouseleave: () => this._unsetHoverImage()
    })
  }

  _toggleImage($photo) {
    if (!$photo.hasClass(this.IS_CURRENT_CLASS)) {
      this.$photoList.find(`.${this.IS_CURRENT_CLASS}`).removeClass(this.IS_CURRENT_CLASS);
      $photo.addClass(this.IS_CURRENT_CLASS);

      this.currentImgUrl = $photo.data("thumbnail-url");
      this.$thumb.attr('src', this.currentImgUrl);
    }
  }

  _setHoverImage() {
    this.$thumb.attr('src', this.hoverImgUrl);
  }

  _unsetHoverImage() {
    this.$thumb.attr('src', this.currentImgUrl);
  }
}
