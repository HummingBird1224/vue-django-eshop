import { inject, reactive } from 'vue';
const useStore = () => {
  const store = inject('store');
  return { store: store, state: reactive(store.state)  }
}

export {
  useStore
}
