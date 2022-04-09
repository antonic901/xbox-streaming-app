<template>
    <v-tooltip top>
        <template #activator="{ on }">
            <v-btn
                text
                tile
                block
                v-on="on"
                v-on:click="exit()"
            >
                <v-icon class="white--text">
                    mdi-exit-to-app
                </v-icon>
            </v-btn>
        </template>
        <span>Exit</span>
    </v-tooltip>
</template>

<script>
module.exports = {
    name: 'Exit',
    methods: {
        exit() {
            alert('This funcionality is in development.')
        }
    }
}
</script>