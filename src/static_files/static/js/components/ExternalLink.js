export default class ExternalLink {
  constructor() {
    this.addEvent();
  }

  addEvent() {
    $(document).on('click', '.js-external-link', e => {
      e.preventDefault();
      e.stopPropagation();

      const $target = $(e.target);
      const link = $target.data('link');

      if (link) {
        window.open(link);
      }
    });
  }
}
