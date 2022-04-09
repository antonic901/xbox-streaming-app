<template>
    <div>
        <v-tooltip bottom>
            <template #activator="{ on }">
                <v-btn
                    large
                    fab
                    text
                    class="mr-0 ml-0"
                    aria-label="Remove selected"
                    v-on="on"
                    v-on:click="remove()"
                >
                    <v-icon color="grey">mdi-delete</v-icon>
                </v-btn>
            </template>
            <span>Remove selected</span>
        </v-tooltip>
    </div>
</template>

<script>
module.exports = {
    name: 'RemoveSelected',
    methods: {
        remove() {
            alert('This funcionality is in development.');
        }
    }
}
</script>