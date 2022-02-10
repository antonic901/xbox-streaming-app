<template>
    <v-card flat>
        <v-subheader>Here you can change some PC-specific settings</v-subheader>
        <v-list-item>
            <v-text-field
                v-model="XBOX_IP_ADDRESS"
                class="mb-2"
                outlined
                dense
                type="text"
                hide-details
                label="IP Address"
                :rules="rulesXboxIpAddress"
                readonly
            >
            </v-text-field>
        </v-list-item>
        <v-list-item>
            <v-text-field
                v-model="XBOX_PORT"
                class="mb-2"
                outlined
                dense
                type="number"
                hide-details
                label="Port"
                :rules="rulesXboxPort"
                readonly
            >
            </v-text-field>
        </v-list-item>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
                color="success"
                class="accent white--text elevation-0 px-4"
                v-on:click="save"
            >
                Save
            </v-btn>
            <v-spacer></v-spacer>
        </v-card-actions>
    </v-card>
</template>

<script>
module.exports = {
    name: 'BasicSettings',
    computed: {
        XBOX_ADDRESS() {
            return this.$store.getters.getXboxAddress;
        }
    },
    data() {
        return {
            XBOX_IP_ADDRESS: null,
            rulesXboxIpAddress: [
                value => !!value || 'Requried.',
                value => {
                    const pattern = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/
                    return pattern.test(value) || 'IP Address is not valid.'
                }
            ],
            XBOX_PORT: null,
            rulesXboxPort: [
                value => !!value || 'Requried.',
                value => {
                    const pattern = /^([1-9][0-9]{0,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$/
                    return pattern.test(value) || 'Port is not valid.'
                }
            ]

        }
    },
    methods: {
        save() {
            
        }
    },
    mounted() {
        this.XBOX_IP_ADDRESS = window.location.hostname;
        this.XBOX_PORT = window.location.port;
    }
}
</script>

<style scoped>

</style>