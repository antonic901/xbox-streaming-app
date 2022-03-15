<template>
    <v-col class="mr-4">
        <div class="caption grey--text">
            Size
        </div>
        <div class="truncate">
            {{(torrent.length / (1024*1024*1024)).toFixed(2)}}
            <span class="caption grey--text">
                GB
            </span>
        </div>
    </v-col>
</template>

<script>
module.exports = {
    name: 'Size',
    props: {
        torrent: Object
    }
}
</script>