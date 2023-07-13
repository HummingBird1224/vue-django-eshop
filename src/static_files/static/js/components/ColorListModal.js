import App from '../vues/pages/ColorListModal.vue';
import Store from '../vues/stores/colorListModal';
import { vueMount } from '../helpers/vueMount';

export default class ColorListModal {
  constructor(element) {

    if (element.length) {
      vueMount(App, Store, element)
    }

    this._addEvent();
  }

  _addEvent() {
    $(document).on('click', '.js-open-color-list-modal-btn', e => {
      e.preventDefault();
      e.stopPropagation();

      this.app.store.openModal();
    });
  }
}
