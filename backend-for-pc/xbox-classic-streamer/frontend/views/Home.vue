<template>
  <div>
    <MenuBar></MenuBar>
    <v-row
      no-gutters
      class="grey--text pt-10 pl-5"
      align="center"
      justify="center"
    >
      <v-col>
        <h1 style="font-size: 1.6em !important" class="subtitle-1 ml-2">
          Dashboard
        </h1>
      </v-col>
      <v-col class="align-center justify-center">
        <span style="float: right; font-size: 0.8em" class="mr-4 text-uppercase">
          {{ getTorrents.length }} TORRENTS
        </span>
      </v-col>
    </v-row>
    <Dashboard></Dashboard>
    <!-- <BasicNotification v-bind:show-notification="snackbar" v-bind:text="notificationText" v-on:close="snackbar = false, notificationText=''"></BasicNotification> -->
  </div>
</template>

<script>

module.exports = {
    name: 'Home',
    computed: {
      getTorrents() {
            let torrents = this.torrents.filter(torrent => {
                if (torrent.stats) {
                    return torrent;
                }
            })
            this.$store.dispatch('updateTorrents', torrents)
            return torrents;
        }
    },
    data() {
      return {
        torrents: [],
        snackbar: true,
        notificationText: ''
      }
    },
    methods: {
      async load() {
        await axios.get("/torrents")
          .then(r => {
              this.torrents = r.data.reverse()
          })
      },
      async loadTorrent(hash) {
        return await axios.get("/torrents/" + hash)
          .then(r => {
            torrent = r.data;
            var existing = this.torrents.find(t => t.infoHash === hash);
            if(existing === undefined) {
              this.torrents.push(torrent);
            } else {
              var index = this.torrents.indexOf(existing)
              vm.$set(this.torrents, index, torrent)
            }
            return torrent;
          })
      },
      async findTorrent(hash) {
        var existing = this.torrents.find(t => t.infoHash === hash);
        if(existing === undefined) {
          return await this.loadTorrent(hash);
        } else {
          return existing;
        }
      }
    },
    created() {

      let self = this;

      this.load();

      axios.get("/configuration").then(r => {this.$store.dispatch('updateConfiguration', r.data);})

      socket.on('verifying', function (hash) {
        // console.log('Verifying...')
        self.findTorrent(hash).then(torrent => torrent.ready = true);
      });

      socket.on('ready', function (hash) {
        // console.log('Ready...')
        self.loadTorrent(hash)
      });

      socket.on('interested', function (hash) {
        // console.log('Interested...')
        self.findTorrent(hash).then(torrent => torrent.interested = true);
      });

      socket.on('uninterested', function (hash) {
        // console.log('Uninterested...')
        self.findTorrent(hash).then(torrent => torrent.interested = false);
      });

      socket.on('finished', function (hash) {
        // console.log('Finished...')
        self.findTorrent(hash).then(torrent => {
          self.notificationText = torrent.name + ' has finished downloading!';
          self.snackbar = true;
        })
      });

      socket.on('stats', function (hash, stats) {
        // console.log('Stats...')
        self.findTorrent(hash).then(torrent => {
          vm.$set(torrent, 'stats', stats)
        })
      });

      socket.on('download', function (hash, progress) {
        // console.log('Download...')
        self.findTorrent(hash).then(torrent => torrent.progress = progress);
      });

      socket.on('selection', function (hash, selection) {
        // console.log('Selection...')
        // self.findTorrent(hash).then(torrent => {
        //   if (!torrent.files) {
        //     return;
        //   }
        //   for (var i = 0; i < torrent.files.length; i++) {
        //     var file = torrent.files[i];
        //     file.selected = selection[i];
        //   }
        //   torrent.selected = _.every(torrent.files, 'selected');
        // });
      });

      socket.on('destroyed', function (hash) {
        // console.log('Destroyed...')
        self.torrents = self.torrents.filter(function(item) {
          return item.infoHash != hash;
        })
      });

      socket.on('disconnect', function () {
        // console.log('Disconnect...')
        self.torrents = [];
      });
    }
}

</script>