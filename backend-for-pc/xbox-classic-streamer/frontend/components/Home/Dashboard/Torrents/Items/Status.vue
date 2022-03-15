<template>
    <v-col>
        <div class="caption grey--text">
            Status
        </div>
        <v-chip
            small
            class="caption white--text px-2"
            color="green"
        >
            {{ getStatus(torrent) }}
        </v-chip>
    </v-col>
</template>

<script>
module.exports = {
    name: 'Status',
    props: {
        torrent: Object
    },
    methods: {
        getStatus(torrent) {
            if(torrent.interested) {
                if(torrent.stats.paused) {
                    return 'Paused';
                }
                else {
                    return 'Downloading';
                }
            }
            else {
                return 'Stopped';
            }
        }
    }
}
</script>