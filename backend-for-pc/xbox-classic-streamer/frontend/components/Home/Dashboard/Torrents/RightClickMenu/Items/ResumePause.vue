<template>
    <v-list-item link v-on:click="click()">
        <v-icon v-if="torrent.stats.paused">mdi-play-circle</v-icon>
        <v-icon v-else>mdi-pause-circle</v-icon>
        <v-list-item-title
            class="ml-2"
            style="font-size: 1em"
        >
            {{ torrent.stats.paused ? 'Resume' : 'Pause' }}
        </v-list-item-title>
    </v-list-item>
</template>

<script>
module.exports = {
    name: 'ResumePause',
    props: {
        torrent: Object
    },
    methods: {
        click() {
            socket.emit(this.torrent.stats.paused ? 'resume' : 'pause', this.torrent.infoHash);
        }
    }
}
</script>