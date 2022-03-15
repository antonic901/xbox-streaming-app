<template>
    <v-list class="pa-0 transparent">
      <v-list-item v-for="torrent in torrents" :key="torrent.infoHash" class="mb-4">
        <v-hover>
          <template v-slot:default="{ hover }">
            <v-card
              class="pointer noselect transition-swing rounded-lg ml-3 pb-3 border-downloading"
              width="100%"
              :class="`elevation-${hover ? 16 : 2}`"
              @contextmenu="show"
              v-on:click.right="selectTorrent(torrent)"
            >
              <v-row no-gutters class="px-4 pt-2">
                <v-col>
                  <div class="caption grey--text">
                    Torrent title
                  </div>
                </v-col>
              </v-row>
              <v-row no-gutters class="px-4">
                <v-col>
                  <div class="truncate mr-4">
                    {{torrent.name}}
                  </div>
                </v-col>
              </v-row>
              <v-row no-gutters class="px-4">
                  <SizeItem v-bind:torrent="torrent"></SizeItem >
                  <ProgressItem v-bind:torrent="torrent"></ProgressItem>
                  <DownloadedItem  v-bind:torrent="torrent"></DownloadedItem >
                 <UploadedItem  v-bind:torrent="torrent"></UploadedItem >
                 <DownloadItem  v-bind:torrent="torrent"></DownloadItem >
                 <UploadItem  v-bind:torrent="torrent"></UploadItem >
                 <ETAItem  v-bind:torrent="torrent"></ETAItem >
                 <PeersItem  v-bind:torrent="torrent"></PeersItem >
                 <StatusItem  v-bind:torrent="torrent"></StatusItem >
              </v-row>
            </v-card>
          </template>
        </v-hover>
      </v-list-item>
      <RightClickMenu v-bind:torrent="torrent" v-bind:show-menu="showMenu" v-bind:x="x" v-bind:y="y"></RightClickMenu>
    </v-list>
</template>

<script>
module.exports = {
    name: 'Torrents',
    computed: {
        torrents() {
            return this.$store.getters.getTorrents;
        }
    },
    data() {
        return {
            torrent: null,
            showMenu: false,
            x: 0,
            y: 0
        }
    },
    methods: {
        show(e) {
            e.preventDefault();
            this.showMenu = false;
            this.x = e.clientX;
            this.y = e.clientY;
            this.$nextTick(() => {
                this.showMenu = true;
            });
         },
        selectTorrent(torrent) {
            this.torrent = torrent;
        },
    }
}
</script>

<style scoped>
  .border-downloading {
    border-left: 5px solid green;
  }
</style>