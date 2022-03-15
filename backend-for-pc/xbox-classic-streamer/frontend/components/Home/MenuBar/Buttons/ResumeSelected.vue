<template>
    <div>
        <v-tooltip bottom>
            <template #activator="{ on }">
                <v-btn
                    text
                    large
                    fab
                    class="mr-0 ml-0"
                    aria-label="Resume selected"
                    v-on="on"
                    v-on:click="resume()"
                >
                    <v-icon color="grey">mdi-play</v-icon>
                </v-btn>
            </template>
            <span>Resume selected</span>
        </v-tooltip>
    </div>
</template>

<script>
module.exports = {
    name: 'ResumeSelected',
    methods: {
        resume() {
            alert('This funcionality is in development.');
        }
    }
}
</script>