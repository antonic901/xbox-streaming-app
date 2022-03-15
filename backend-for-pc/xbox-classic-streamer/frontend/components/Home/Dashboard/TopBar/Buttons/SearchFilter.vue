<template>
    <v-tooltip bottom>
        <template #activator="{ on }">
            <v-btn
                text
                small
                fab
                class="mr-0 ml-0"
                aria-label="Select Mode"
                v-on="on"
                v-on:click="enableSearchFilter()"
            >
                <v-icon v-if="searchFilterEnabled" color="grey">
                    mdi-chevron-left-circle
                </v-icon>
                <v-icon v-else color="grey">
                    mdi-text-box-search
                </v-icon>
            </v-btn>
        </template>
        <span>Toggle Search Filter</span>
    </v-tooltip>
</template>

<script>
module.exports = {
    name: 'SearchFilter',
    data() {
        return {
            searchFilterEnabled: false
        }
    },
    methods: {
        enableSearchFilter() {
            this.searchFilterEnabled = !this.searchFilterEnabled;
            alert('This funcionality is in development.');
        }
    }
}
</script>