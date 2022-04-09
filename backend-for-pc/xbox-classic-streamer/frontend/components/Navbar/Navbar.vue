<template>
    <v-navigation-drawer 
        app 
        color="blue-grey darken-3"
        style="position: fixed;"
        width="256"
        height="100%"
        permanent
    >
        <v-card
            class="pt-3 fill-height"
            flat
            color="blue-grey darken-3"
        >
            <div class="text-uppercase white--text caption ml-3 font-weight-medium">CURRENT SPEED</div>
            <CurrentSpeed v-bind:torrents="torrents"></CurrentSpeed>
            <v-row no-gutters align="center" class="mx-3 mt-3">
                <div class="text-uppercase white--text caption font-weight-medium">
                    SESSION STATS
                </div>
                <v-icon class="grey--text" small>mdi-information-outline</v-icon>
            </v-row>
            <SessionStats></SessionStats>
        </v-card>
        <template v-slot:append>
            <v-row no-gutters align="end" class="my-7">
                <v-col align="center">
                    <div style="color:#64CEAA;" class="text-center font-weight-bold robot-mono">{{torrents.length}} TORRENTS</div>
                </v-col>
            </v-row>
            <BottomMenu></BottomMenu>
        </template>
    </v-navigation-drawer>
</template>

<script>
module.exports = {
    name: 'Navbar',
    computed: {
        torrents() {
            return this.$store.getters.getTorrents
        }
    }
}
</script>