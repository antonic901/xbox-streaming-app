<template>
    <v-card
        flat
        class="d-flex flex-row justify-space-between align-center py-6 rounded-lg"
        color="blue-grey darken-1"
    >
        <v-icon color="#64CEAA" size="20px" class="mx-1">mdi-chevron-down</v-icon>
        <span style="color:#64CEAA;" class="text-center font-weight-bold robot-mono">{{(downloadSpeed/1024).toFixed(2)}}</span>
        <span style="color:#64CEAA;" class="caption robot-mono text-center mx-1">KB/s</span>
    </v-card>
</template>

<script>
module.exports = {
    name: 'DownloadSpeed',
    props: {
        torrents: Array
    },
    computed: {
         downloadSpeed() {
            var speed = 0;
            for (let i = 0; i < this.torrents.length; i++) {
                if(!this.torrents[i].paused) {
                    speed = speed + this.torrents[i].stats.speed.down;
                }
            }
            return speed;
        }
    }
}
</script>