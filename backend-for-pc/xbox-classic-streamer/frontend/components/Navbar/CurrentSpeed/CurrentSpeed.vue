<template>
    <v-row no-gutters class="mx-2">
        <v-col class="mr-1">
            <DownloadSpeed v-bind:torrents="torrents"></DownloadSpeed>
        </v-col>
        <v-col class="ml-1">
            <UploadSpeed v-bind:torrents="torrents"></UploadSpeed>
        </v-col>
    </v-row>
</template>

<script>
module.exports = {
    name: 'CurrentSpeed',
    props: {
        torrents: Array
    }
}
</script>