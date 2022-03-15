<template>
    <div>
        <v-tooltip bottom>
            <template #activator="{ on }">
                    <v-btn
                        large
                        fab
                        text
                        class="mr-0 ml-0"
                        aria-label="Pause selected"
                        v-on="on"
                        v-on:click="pause()"
                    >
                        <v-icon color="grey">mdi-pause</v-icon>
                    </v-btn>
                </template>
                <span>Pause selected</span>
            </v-tooltip>
    </div>
</template>

<script>
module.exports = {
    name: 'PauseSelected',
    methods: {
        pause() {
            alert('This funcionality is in development.');
        }
    }
}
</script>