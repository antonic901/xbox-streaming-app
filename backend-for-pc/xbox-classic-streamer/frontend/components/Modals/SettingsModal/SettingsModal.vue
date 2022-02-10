<template>
    <v-dialog
        v-model="dialog"
        max-width="800px"
        scrollable
    >
        <v-card class="rounded-lg">
            <v-toolbar flat dense dark color="blue-grey darken-3">
                <v-spacer></v-spacer>
                <v-toolbar-title style="font-size: 1.9em !important;" class="font-weight-medium white--text">
                    Settings
                </v-toolbar-title>
                <v-spacer></v-spacer>
                <template v-slot:extension>
                    <v-tabs
                        v-model="tabs"
                        fixed-tabs
                        align-with-title 
                        show-arrows
                    >
                        <v-tabs-slider color="white"></v-tabs-slider>
                        <v-tab href="#basicsettings">
                            <h4>Basic Settings</h4>
                        </v-tab>
                        <v-tab href="#xboxsettings">
                            <h4>Xbox Settings</h4>
                        </v-tab>
                        <v-tab href="#connection">
                            <h4>Connection</h4>
                        </v-tab>
                        <v-tab href="#subtitles">
                            <h4>Subtitles</h4>
                        </v-tab>
                        <v-tab href="#webui">
                            <h4>WEB UI</h4>
                        </v-tab>
                    </v-tabs>
                </template>
            </v-toolbar>
            <v-tabs-items v-model="tabs" touchless>
                <v-tab-item value="basicsettings">
                    <BasicSettings :is-active-tab="tabs === 'basicsettings'"></BasicSettings>
                </v-tab-item>
                <v-tab-item value="xboxsettings">
                    <XboxSettings :is-active-tab="tabs === 'xboxsettings'"></XboxSettings>
                </v-tab-item>
                <v-tab-item value="connection">
                    <v-card flat>
                        <v-card-text v-text="text"></v-card-text>
                    </v-card>
                </v-tab-item>
                <v-tab-item value="subtitles">
                    <v-card flat>
                        <v-card-text v-text="text"></v-card-text>
                    </v-card>
                </v-tab-item>
                <v-tab-item value="webui">
                    <v-card flat>
                        <v-card-text v-text="text"></v-card-text>
                    </v-card>
                </v-tab-item>
            </v-tabs-items>
        </v-card>
    </v-dialog>
</template>

<script>
module.exports = {
    name: 'SettingsModal',
    props: {
        value: Boolean
    },
    computed: {
        dialog: {
            get() {
                return this.value;
            },
            set(value) {
                this.$emit('input', value);
            }
        }
    },
    data() {
        return {
            tab: null,
            tabs: null,
            text: 'This tab is in development. Please be patient.'
        }
    }
}
</script>

<style scoped>
.fix-height .v-card__text {
  height: 400px;
}
</style>