<template>
    <div>
        <v-tooltip bottom>
            <template #activator="{ on }">
                <v-btn
                    large
                    fab
                    text
                    class="mr-0 ml-0"
                    aria-label="Settings"
                    v-on="on"
                    @click.stop="show=true"
                >
                    <v-icon color="grey">mdi-cog</v-icon>
                </v-btn>
            </template>
            <span>Settings</span>
        </v-tooltip>
        <SettingsModal v-model="show"></SettingsModal>
    </div>
</template>

<script>
module.exports = {
    name: 'Settings',
    data() {
        return {
            show: false
        }
    }
}
</script>