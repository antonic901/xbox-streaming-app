<template>
    <v-card
        flat
        class="d-flex flex-row justify-space-between align-center py-4 px-2 mx-2 mb-4 rounded-lg"
        color="blue-grey darken-1"
    >
        <span style="color:#00b3fa;" class="text-center font-weight-bold robot-mono">Free space</span>
        <div style="color:#00b3fa;" class="font-weight-bold">{{160.4}}<span style="color:#00b3fa;" class="caption robot-mono text-center mx-1">GB</span></div>
    </v-card>
</template>

<script>
module.exports = {
    name: 'FreeSpace'
}
</script>