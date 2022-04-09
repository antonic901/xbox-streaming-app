<template>
    <v-col class="mr-4">
        <div class="caption grey--text">
            Peers
        </div>
        <div class="truncate">
            {{torrent.stats.peers.unchocked}}
            <span class="caption grey--text">
                /{{torrent.stats.peers.total}}
            </span>
        </div>
    </v-col>
</template>

<script>
module.exports = {
    name: 'Peers',
    props: {
        torrent: Object
    }
}
</script>