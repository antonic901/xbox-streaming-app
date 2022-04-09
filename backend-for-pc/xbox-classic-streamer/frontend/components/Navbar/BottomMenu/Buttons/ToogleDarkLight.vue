<template>
    <v-tooltip top>
        <template #activator="{ on }">
            <v-btn
                text
                tile
                block
                v-on="on"
                v-on:click="toogleDarkLight()"
            >
                <v-icon class="white--text">
                    mdi-brightness-7
                </v-icon>
            </v-btn>
        </template>
        <span>Dark/Ligh Toogle</span>
    </v-tooltip>
</template>

<script>
module.exports = {
    name: 'ToogleDarkLight',
    methods: {
        toogleDarkLight() {
            alert('This funcionality is in development.')
        }
    }
}
</script>