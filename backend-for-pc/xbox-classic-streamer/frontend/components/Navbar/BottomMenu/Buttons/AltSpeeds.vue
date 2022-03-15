<template>
    <v-tooltip top>
        <template #activator="{ on }">
            <v-btn
                text
                tile
                block
                v-on="on"
                v-on:click="openSpeedMeter()"
            >
                <v-icon color="teal lighten-3" class="white--text">
                    <!-- {{ altSpeed ? mdi-speedometer-slow : mdi-speedometer }} -->
                    mdi-speedometer-slow
                </v-icon>
            </v-btn>
        </template>
        <span>Alt speeds</span>
    </v-tooltip>
</template>

<script>
module.exports = {
    name: 'AltSpeeds',
    methods: {
        openSpeedMeter() {
            alert('This funcionality is in development.')
        }
    }
}
</script>