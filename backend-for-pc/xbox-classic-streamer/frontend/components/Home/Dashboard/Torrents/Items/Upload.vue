<template>
    <v-col class="mr-4">
        <div class="caption grey--text">
            Upload
        </div>
        <div class="truncate">
            {{(torrent.stats.speed.up/(1024)).toFixed(2)}}
            <span class="caption grey--text">
                KB/s
            </span>
        </div>
    </v-col>
</template>

<script>
module.exports = {
    name: 'Upload',
    props: {
        torrent: Object
    }
}
</script>