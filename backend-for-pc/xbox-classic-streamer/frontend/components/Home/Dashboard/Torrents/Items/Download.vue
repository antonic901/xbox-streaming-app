<template>
    <v-col class="mr-4">
        <div class="caption grey--text">
            Download
        </div>
        <div class="truncate">
            {{(torrent.stats.speed.down/(1024)).toFixed(2)}}
            <span class="caption grey--text">
                KB/s
            </span>
        </div>
    </v-col>
</template>

<script>
module.exports = {
    name: 'Download',
    props: {
        torrent: Object
    }
}
</script>