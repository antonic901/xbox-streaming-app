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
                v-on:click="enableSelection()"
            >
                <v-icon v-if="selectMode" color="grey">
                    mdi-checkbox-marked
                </v-icon>
                <v-icon v-else color="grey">
                    mdi-checkbox-blank-outline
                </v-icon>
            </v-btn>
        </template>
        <span>Select Mode</span>
    </v-tooltip>
</template>

<script>
module.exports = {
    name: 'Selection',
    data() {
        return {
            selectMode: false
        }
    },
    methods: {
        enableSelection() {
            this.selectMode = !this.selectMode;
            alert('This funcionality is in development.');
        }
    }
}
</script>