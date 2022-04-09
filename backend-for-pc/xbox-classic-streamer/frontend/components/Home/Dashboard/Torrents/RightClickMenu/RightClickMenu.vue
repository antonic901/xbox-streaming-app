<template>
    <v-menu 
      v-model="show"
      :position-x="x"
      :position-y="y"
      absolute
      offset-y
      v-if="torrent"
    >
      <v-list class="noselect">
        <StartStop v-bind:torrent="torrent"></StartStop>
        <ResumePause v-bind:torrent="torrent"></ResumePause>
        <v-divider></v-divider>
        <Delete v-bind:torrent="torrent"></Delete>
        <v-divider></v-divider>
        <Play v-bind:torrent="torrent"></Play>
        <ShowInfo v-bind:torrent="torrent"></ShowInfo>
      </v-list>
    </v-menu>
</template>

<script>
module.exports = {
    name: 'RightClickMenu',
    props: {
      torrent: Object,
      showMenu: Boolean,
      x: Number,
      y: Number
    },
    computed: {
      show: {
        get() {
          return this.showMenu;
        },
        set(showMenu) {
          this.$emit('input', showMenu);
        }
      }
    }
}
</script>