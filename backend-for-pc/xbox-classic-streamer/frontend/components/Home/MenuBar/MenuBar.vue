<template>
    <v-row class="pt-3 pl-3" no-gutters>
        <div class="d-flex justify-start">
            <v-img max-width="64" max-height="64" class="mr-10" src="img/logo.png"></v-img>
            <h1 style="font-size: 1.6em !important;" class="subtitle-1 grey--text mr-0 ml-0 d-flex align-center">
                XBox Media Center
            </h1>
        </div>
        <v-spacer></v-spacer>
        <div class="d-flex justify-end">
            <AddTorrent></AddTorrent>
            <ResumeSelected></ResumeSelected>
            <PauseSelected></PauseSelected>
            <RemoveSelected></RemoveSelected>
            <SearchTorrents></SearchTorrents>
            <Settings></Settings>
        </div>
    </v-row>
</template>

<script>
module.exports = {
    name: 'MenuBar',
    props: {

    }
}
</script>