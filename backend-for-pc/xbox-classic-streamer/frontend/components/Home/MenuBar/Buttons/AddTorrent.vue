<template>
    <div>
        <v-tooltip bottom>
            <template #activator="{ on }">
                <v-btn
                    text
                    large
                    fab
                    color="grey--text"
                    class="mr-0 ml-0"
                    aria-label="Add torrent"
                    v-on="on"
                    v-on:click.stop="show = true"
                >
                    <v-icon color="grey">mdi-plus</v-icon>
                </v-btn>
            </template>
            <span>Add torrent</span>
        </v-tooltip>
        <AddTorrentModal v-model="show"></AddTorrentModal>
    </div>
</template>
    
<script>
module.exports = {
    name: 'AddTorrent',
    data() {
        return {
            show: false
        }
    }
}
</script>