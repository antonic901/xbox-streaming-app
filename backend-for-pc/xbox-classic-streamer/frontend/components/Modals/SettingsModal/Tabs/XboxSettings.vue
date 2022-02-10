<template>
    <v-card flat>
        <v-subheader>Here you can change some XBOX-specific settings</v-subheader>
        <v-list-item>
            <v-text-field
                v-model="configuration.XBOX.IP_ADDRESS"
                class="mb-2"
                outlined
                dense
                type="text"
                hide-details
                label="IP Address of your XBOX"
                :rules="rulesXboxIpAddress"
            >
            </v-text-field>
        </v-list-item>
        <v-list-item>
            <v-text-field
                v-model="configuration.XBOX.PORT"
                class="mb-2"
                outlined
                dense
                type="number"
                hide-details
                label="Port of your XBOX"
                :rules="rulesXboxPort"
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
    name: 'XboxSettings',
    computed: {

    },
    data() {
        return {
            configuration: null,
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
        ValidateIPaddress(ipaddress) {  
            if (/^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/.test(ipaddress)) {  
                return (true)
            }  
            return (false)
        },
        save() {
            this.$store.dispatch('updateConfiguration', this.configuration);
            axios.post("/configuration", this.configuration)
        }
    },
    created() {
        this.configuration = this.$store.getters.getConfiguration;
    }
}
</script>