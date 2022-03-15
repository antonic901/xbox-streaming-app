<template>
    <v-list-item link v-on:click="click()">
        <v-icon>mdi-information</v-icon>
        <v-list-item-title class="ml-2">
            Show Info
        </v-list-item-title>
    </v-list-item>
</template>

<script>
module.exports = {
    name: 'ShowInfo',
    props: {
        torrent: Object
    },
    methods: {
        click() {
            alert('This funcionality is in development.');
        }
    }
}
</script>