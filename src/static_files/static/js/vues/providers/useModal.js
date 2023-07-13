import { ref } from 'vue';

const useModal = () => {

  const isOpeningModal = ref(false)

  const openModal = () => {
    isOpeningModal.value = true;
  }

  const closeModal = () => {
    isOpeningModal.value= false;
  }

  const toggleModal = () => {

    if(isOpeningModal.value) {
      closeModal();
      return
    }

    openModal();
  }

  return { isOpeningModal, openModal, closeModal, toggleModal }
}

export {
  useModal
}
