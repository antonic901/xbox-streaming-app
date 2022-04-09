<template>
    <v-col class="mr-4">
        <div class="caption grey--text">
            Downloaded
        </div>
        <div class="truncate">
            {{(torrent.stats.traffic.down/(1024*1024*1024)).toFixed(2)}}
            <span class="caption grey--text">
                GB
            </span>
        </div>
    </v-col>
</template>

<script>
module.exports = {
    name: 'Downloaded',
    props: {
        torrent: Object
    }
}
</script>