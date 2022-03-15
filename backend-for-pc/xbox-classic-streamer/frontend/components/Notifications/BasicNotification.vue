<template>
    <v-snackbar v-model="show" timeout="5000" color="blue-grey darken-2">
      {{text}}
      <template v-slot:action="{ attrs }">
        <v-btn
          color="blue"
          text
          v-bind="attrs"
          v-on:click="close()"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
</template>

<script>
module.exports = {
    name: 'BasicNotification',
    props: {
        showNotification: Boolean,
        text: String
    },
    computed: {
      show: {
        get() {
          return this.showNotification;
        },
        set(showNotification) {
          this.$emit('input', showNotification);
        }
      }
    },
    methods: {
        close() {
            this.$emit('close')
        }
    }
}
</script>