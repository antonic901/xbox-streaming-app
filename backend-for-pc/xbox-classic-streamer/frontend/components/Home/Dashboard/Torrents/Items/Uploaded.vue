<template>
    <v-col class="mr-4">
        <div class="caption grey--text">
            Uploaded
        </div>
        <div class="truncate">
            {{(torrent.stats.traffic.up/(1024*1024*1024)).toFixed(2)}}
            <span class="caption grey--text">
                GB
            </span>
        </div>
    </v-col>
</template>

<script>
module.exports = {
    name: 'Uploaded',
    props: {
        torrent: Object
    }
}
</script>