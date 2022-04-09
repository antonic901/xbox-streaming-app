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
                    aria-label="Search torrents"
                    v-on="on"
                    v-on:click="search()"
                >
                    <v-icon color="grey">mdi-search-web</v-icon>
                </v-btn>
            </template>
            <span>Search torrents</span>
        </v-tooltip>
    </div>
</template>

<script>
module.exports = {
    name: 'SearchTorrents',
    methods: {
        search() {
            alert('This funcionality is in development.');
        }
    }
}
</script>