<template>
  <transition name="container">
    <div class="c-modal" v-show="isShow" @click.self="$emit('close')">
      <slot />
    </div>
  </transition>
</template>

<script>
export default {
  name: "ModalWindow",
  emits: ['close'],
  data: () => ({
    fixedScrollTop: 0,
    isAlreadyFixed: false,
  }),
  props: {
    isShow: {
      type: Boolean
    }
  },
  watch: {
    isShow: function (newVal) {
      this.toggleFix(newVal);
    }
  },
  methods: {
    toggleFix(isFix) {
      const $body = $('body');

      if (isFix) {
        this.isAlreadyFixed = $body.css('position') === 'fixed';

        if (this.isAlreadyFixed) {
          return;
        }

        this.fixedScrollTop = $(window).scrollTop();

        $body
          .css({
            position: 'fixed',
            top: -1 * this.fixedScrollTop,
            width: '100%'
          });
      } else {
        if (this.isAlreadyFixed) {
          return;
        }

        $body.removeAttr('style');
        $(window).scrollTop(this.fixedScrollTop);
      }
    }
  },
  beforeUnmount() {
    this.toggleFix(false);
  },
  mounted() {
    this.isAlreadyFixed = $('body').css('position') === 'fixed';
  }
}
</script>

<style scoped>
  .container-enter-active,
  .container-leave-active {
    transition: opacity 0.3s;
  }

  .container-enter,
  .container-leave-to {
    opacity: 0;
  }
</style>
