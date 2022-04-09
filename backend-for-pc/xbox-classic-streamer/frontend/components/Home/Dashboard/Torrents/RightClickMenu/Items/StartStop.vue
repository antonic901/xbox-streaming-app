<template>
    <v-list-item link v-on:click="click()">
        <v-icon v-if="torrent.interested">mdi-pause</v-icon>
        <v-icon v-else>mdi-play</v-icon>
        <v-list-item-title
            class="ml-2"
            style="font-size: 1em"
        >
         {{ torrent.interested ? 'Stop' : 'Start' }}
        </v-list-item-title>
    </v-list-item>
</template>

<script>
module.exports = {
    name: 'StartStop',
    props: {
        torrent: Object
    },
    methods: {
        click() {
            socket.emit(this.torrent.interested ? 'stop' : 'start', this.torrent.infoHash, -1);
        }
    }
}
</script>