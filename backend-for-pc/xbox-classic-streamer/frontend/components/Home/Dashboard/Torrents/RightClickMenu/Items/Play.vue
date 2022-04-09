<template>
    <v-list-item link v-on:click="click()">
        <v-icon>mdi-play</v-icon>
        <v-list-item-title class="ml-2">
            Play on Xbox
        </v-list-item-title>
    </v-list-item>
</template>

<script>
module.exports = {
    name: 'Play',
    props: {
        torrent: Object
    },
    computed: {
      API() {
        let conf = this.$store.getters.getConfiguration;
        return "http://" + conf.PC.IP_ADDRESS + ":" + conf.PC.PORT;
      },
      XBOX_ADDRESS() {
        let conf = this.$store.getters.getConfiguration;
        return "http://" + conf.XBOX.IP_ADDRESS + ":" + conf.XBOX.PORT;
      }
    },
    methods: {
        click() {
            var video_file;

            for (var i = 0; i < this.torrent.files.length; i++) {
                ['.mkv', '.mp4', '.avi'].forEach(extension => {
                    if (this.torrent.files[i].name.includes(extension)) {
                        video_file = this.torrent.files[i]
                        return
                    }
                })
            }

            var stream_link = this.API + video_file.link + '?ffmpeg=remux';

            axios.get(this.XBOX_ADDRESS + '/xbmcCmds/xbmcHttp?command=ExecBuiltIn(PlayMedia(' + encodeURIComponent(stream_link) + '))')
                .then(r => {
                    console.log("Succesfully started streaming on Xbox.");
                })
                .catch(e => {
                    console.log("Error when playing file. Log: " + e);            
                })
        }
    }
}
</script>