<template>
    <v-tooltip bottom>
        <template #activator="{ on }">
            <v-btn
                text
                small
                fab
                class="mr-0 ml-0"
                aria-label="Sort Torrents"
                v-on="on"
                v-on:click="enableSorting()"
            >
                <v-icon color="grey">mdi-sort</v-icon>
            </v-btn>
        </template>
        <span>Sort Torrents</span>
    </v-tooltip>
</template>

<script>
module.exports = {
    name: 'Sorting',
    methods: {
        enableSorting() {
            alert('This funcionality is in development.');
         }
    }
}
</script>