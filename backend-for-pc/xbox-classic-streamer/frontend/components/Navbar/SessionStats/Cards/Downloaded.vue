<template>
    <v-card
        flat
        class="d-flex flex-row justify-space-between align-center py-4 px-2 mx-2 mb-2 rounded-lg"
        color="blue-grey darken-1"
    >
        <span style="color:#64CEAA;" class="text-center font-weight-bold robot-mono">Downloaded</span>
        <div style="color:#64CEAA;" class="font-weight-bold">{{100.2}}<span style="color:#64CEAA;" class="caption robot-mono text-center mx-1">MB</span></div>
    </v-card>
</template>

<script>
module.exports = {
    name: 'Downloaded'
}
</script>