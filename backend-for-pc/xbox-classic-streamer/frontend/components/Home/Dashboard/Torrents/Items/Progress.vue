<template>
    <v-col class="mr-4">
        <div class="caption grey--text">
            Progress
        </div>
        <v-progress-linear
            :value="torrent.progress[0]"
            height="20"
            color="green"
            rounded
        >
            <span
                class="caption white--text"
            >
                {{ torrent.progress[0].toFixed(2) }}%
            </span>
        </v-progress-linear>
    </v-col>
</template>

<script>
module.exports = {
    name: 'Progress',
    props: {
        torrent: Object
    }
}
</script>