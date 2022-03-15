<template>
    <v-list-item link v-on:click="click()">
          <v-icon color="red">mdi-delete</v-icon>
          <v-list-item-title
            class="ml-2 red--text"
            style="font-size: 1em;"
          >
            Delete
          </v-list-item-title>
    </v-list-item>
</template>

<script>
module.exports = {
    name: 'Delete',
    props: {
        torrent: Object
    },
    methods: {
        click() {
            axios.delete("/torrents/" + this.torrent.infoHash);
        }
    }
}
</script>