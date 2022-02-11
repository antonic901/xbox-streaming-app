<template>
    <v-dialog
        v-model="dialog"
        max-width="800px"
    >
        <v-card flat class="rounded-lg">
            <v-subheader>Please enter magnet link:</v-subheader>
            <v-form
                ref="form"
                v-model="valid"
                lazy-validation
            >
                <v-text-field
                    v-model="magnet"
                    class="mb-2 mx-4"
                    outlined
                    dense
                    type="text"
                    hide-details
                    label="Magnet link:"
                    :rules="rules"
                >
                </v-text-field>
            </v-form>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                    :disabled = "!valid"
                    color="success"
                    class="accent white--text elevation-0 px-4"
                    v-on:click="validate()"
                >
                    Add torrent
                </v-btn>
                <v-spacer></v-spacer>
            </v-card-actions>
        </v-card>
    </v-dialog>
</template>

<script>
module.exports = {
    name: 'AddTorrentModal',
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
            magnet: '',
            rules: [
                v => !!v || 'Required.',

            ],
            valid: true
        }
    },
    methods: {
        validate () {
            if(this.$refs.form.validate()) {
                this.add()
            }
        },
        add() {
            axios.post("/torrents", {"link": this.magnet})
                .then (r => {
                    this.magnet = '';
                    this.dialog=false;
                })
                .catch(error => {
                    alert("Magnet link is not valid.")
                    console.log(error)
                })
 
        }
            
    }
}
</script>