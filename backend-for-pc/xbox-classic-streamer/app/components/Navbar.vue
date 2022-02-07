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
            <v-row no-gutters class="mx-2">
                <v-col class="mr-1">
                    <v-card
                        flat
                        class="d-flex flex-row justify-space-between align-center py-6 rounded-lg"
                        color="blue-grey darken-1"
                    >
                    <v-icon color="#64CEAA" size="20px" class="mx-1">mdi-chevron-down</v-icon>
                    <span style="color:#64CEAA;" class="text-center font-weight-bold robot-mono">{{(downloadSpeed/1024).toFixed(2)}}</span>
                    <span style="color:#64CEAA;" class="caption robot-mono text-center mx-1">KB/s</span>
                    </v-card>
                </v-col>
                <v-col class="ml-1">
                    <v-card
                        flat
                        class="d-flex flex-row justify-space-between align-center py-6 rounded-lg"
                        color="blue-grey darken-1"
                    >
                        <v-icon color="#00b3fa" size="20px" class="mx-1">mdi-chevron-up</v-icon>
                        <span style="color:#00b3fa;" class="text-center font-weight-bold robot-mono">{{(uploadSpeed/1024).toFixed(2)}}</span>
                        <span style="color:#00b3fa;" class="caption robot-mono text-center mx-1">KB/s</span>
                    </v-card>
                </v-col>
            </v-row>
            <v-row no-gutters align="center" class="mx-3 mt-3">
                <div class="text-uppercase white--text caption font-weight-medium">
                    SESSION STATS
                </div>
                <v-icon class="grey--text" small>mdi-information-outline</v-icon>
            </v-row>
            <v-card
                flat
                class="d-flex flex-row justify-space-between align-center py-4 px-2 mx-2 mb-2 rounded-lg"
                color="blue-grey darken-1"
            >
                <span style="color:#64CEAA;" class="text-center font-weight-bold robot-mono">Downloaded</span>
                <div style="color:#64CEAA;" class="font-weight-bold">{{100.2}}<span style="color:#64CEAA;" class="caption robot-mono text-center mx-1">MB</span></div>
            </v-card>
            <v-card
                flat
                class="d-flex flex-row justify-space-between align-center py-4 px-2 mx-2 mb-4 rounded-lg"
                color="blue-grey darken-1"
            >
                <span style="color:#00b3fa;" class="text-center font-weight-bold robot-mono">Uploaded</span>
                <div style="color:#00b3fa;" class="font-weight-bold">{{1.2}}<span style="color:#00b3fa;" class="caption robot-mono text-center mx-1">MB</span></div>
            </v-card>
            <v-card
                flat
                class="d-flex flex-row justify-space-between align-center py-4 px-2 mx-2 mb-4 rounded-lg"
                color="blue-grey darken-1"
            >
                <span style="color:#00b3fa;" class="text-center font-weight-bold robot-mono">Free space</span>
                <div style="color:#00b3fa;" class="font-weight-bold">{{160.4}}<span style="color:#00b3fa;" class="caption robot-mono text-center mx-1">GB</span></div>
            </v-card>
        </v-card>
        <template v-slot:append>
            <!-- <v-row no-gutters align="center" class="mx-2">
                <div class="white--text text-center font-weight-bold robot-mono">
                    Menu:
                </div>
                <v-icon class="grey--text" small>mdi-information-outline</v-icon>
            </v-row> -->
            <v-row no-gutters class="mx-2 mb-2">
                <v-col>
                    <v-hover>
                        <template v-slot:default="{ hover }">
                            <v-sheet class="rounded-lg transition-swing" :elevation="hover ? 12 : 2" v-on:click="browseTorrents()">
                                <div class="subtitle-1 grey--text font-weight-bold align-center mx-2 text-center">Browse torrents</div>
                            </v-sheet>
                        </template>
                    </v-hover>
                </v-col>
            </v-row>
            <v-row no-gutters class="mx-2 mb-2">
                <v-col>
                    <v-hover>
                        <template v-slot:default="{ hover }">
                            <v-sheet class="rounded-lg transition-swing" :elevation="hover ? 12 : 2" v-on:click="openAbout()">
                                <div class="subtitle-1 grey--text font-weight-bold align-center mx-2 text-center">About</div>
                            </v-sheet>
                        </template>
                    </v-hover>
                </v-col>
            </v-row>
            <v-row no-gutters align="end" class="my-7">
                <v-col align="center">
                    <div style="color:#64CEAA;" class="text-center font-weight-bold robot-mono">{{torrents.length}} TORRENTS</div>
                </v-col>
            </v-row>
            <v-row no-gutters align="end">
                <v-col class="mb-4">
                    <v-tooltip top>
                        <template #activator="{ on }">
                        <v-btn
                            text
                            tile
                            block
                            v-on="on"
                            v-on:click="exit()"
                        >
                            <v-icon class="white--text">
                                mdi-exit-to-app
                            </v-icon>
                        </v-btn>
                        </template>
                        <span>Exit</span>
                    </v-tooltip>
                </v-col>
                <v-col class="mb-4">
                    <v-tooltip top>
                        <template #activator="{ on }">
                            <v-btn
                                text
                                tile
                                block
                                v-on="on"
                                v-on:click="openSpeedMeter()"
                            >
                                <v-icon color="teal lighten-3" class="white--text">
                                    <!-- {{ altSpeed ? mdi-speedometer-slow : mdi-speedometer }} -->
                                    mdi-speedometer-slow
                                </v-icon>
                            </v-btn>
                        </template>
                        <span>Alt speeds</span>
                    </v-tooltip>
                </v-col>
                <v-col class="mb-4">
                    <v-tooltip top>
                        <template #activator="{ on }">
                            <v-btn
                                text
                                tile
                                block
                                v-on="on"
                                v-on:click="toogleDarkLight()"
                            >
                                <v-icon class="white--text">
                                <!-- {{ theme === 'Light' ? mdiBrightness7 : mdiBrightness4 }} -->
                                    mdi-brightness-7
                                </v-icon>
                            </v-btn>
                        </template>
                        <span>Dark/Ligh Toogle</span>
                    </v-tooltip>
                </v-col>
            </v-row>
        </template>
    </v-navigation-drawer>
</template>

<script>
module.exports = {
    name: 'Navbar',
    computed: {
        torrents() {
            return this.$store.getters.getTorrents
        },
        downloadSpeed() {
            var speed = 0;
            for (let i = 0; i < this.torrents.length; i++) {
                if(!this.torrents[i].paused) {
                    speed = speed + this.torrents[i].stats.speed.down;
                }
            }
            return speed;
        },
        uploadSpeed() {
            var speed = 0;
            for (let i = 0; i < this.torrents.length; i++) {
                if(!this.torrents[i].paused) {
                    speed = speed + this.torrents[i].stats.speed.up;
                }
            }
            return speed;
        } 
    },
    methods: {
        browseTorrents() {
            alert('This funcionality is in development.')
        },
        openAbout() {
            alert('This funcionality is in development.')
        },
        exit() {
            alert('This funcionality is in development.')
        },
        openSpeedMeter() {
            alert('This funcionality is in development.')
        },
        toogleDarkLight() {
            alert('This funcionality is in development.')
        }
    }
}
</script>

<style scoped>
.speedCard {
    padding: 20px 20px !important;
    font-size: 1.10em;
}
</style>