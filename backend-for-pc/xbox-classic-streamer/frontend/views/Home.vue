<template>
  <div>
    <v-row class="pt-3 pl-3" no-gutters>
      <div class="d-flex justify-start">
        <v-img max-width="64" max-height="64" class="mr-10" src="https://logos-world.net/wp-content/uploads/2020/11/Xbox-Emblem.png"></v-img>
        <h1 style="font-size: 1.6em !important;" class="subtitle-1 grey--text mr-0 ml-0 d-flex align-center">
          XBox Media Center
        </h1>
      </div>
      <v-spacer></v-spacer>
      <div class="d-flex justify-end">
        <v-tooltip bottom>
          <template #activator="{ on }">
            <v-btn
              text
              large
              fab
              color="grey--text"
              class="mr-0 ml-0"
              aria-label="Add torrent"
              v-on="on"
              v-on:click.stop="showAddTorrent = true"
            >
              <v-icon color="grey">mdi-plus</v-icon>
            </v-btn>
          </template>
          <span>Add torrent</span>
        </v-tooltip>
        <v-tooltip bottom>
          <template #activator="{ on }">
            <v-btn
              text
              large
              fab
              class="mr-0 ml-0"
              aria-label="Resume selected"
              v-on="on"
              v-on:click="resumeSelected()"
            >
              <v-icon color="grey">mdi-play</v-icon>
            </v-btn>
          </template>
          <span>Resume selected</span>
        </v-tooltip>
        <v-tooltip bottom>
          <template #activator="{ on }">
            <v-btn
              large
              fab
              text
              class="mr-0 ml-0"
              aria-label="Pause selected"
              v-on="on"
              v-on:click="pauseSelected()"
            >
              <v-icon color="grey">mdi-pause</v-icon>
            </v-btn>
          </template>
          <span>Pause selected</span>
        </v-tooltip>
        <v-tooltip bottom>
          <template #activator="{ on }">
            <v-btn
              large
              fab
              text
              class="mr-0 ml-0"
              aria-label="Remove selected"
              v-on="on"
              v-on:click="removeSelected()"
            >
              <v-icon color="grey">mdi-delete</v-icon>
            </v-btn>
          </template>
          <span>Remove selected</span>
        </v-tooltip>
        <v-tooltip bottom>
          <template #activator="{ on }">
            <v-btn
              text
              large
              fab
              color="grey--text"
              class="mr-0 ml-0"
              aria-label="Search torrents"
              v-on="on"
              v-on:click="searchTorrents()"
            >
              <v-icon color="grey">mdi-search-web</v-icon>
            </v-btn>
          </template>
          <span>Search torrents</span>
        </v-tooltip>
        <v-tooltip bottom>
          <template #activator="{ on }">
            <v-btn
              large
              fab
              text
              class="mr-0 ml-0"
              aria-label="Settings"
              v-on="on"
              @click.stop="showSettings=true"
            >
              <v-icon color="grey">mdi-cog</v-icon>
            </v-btn>
          </template>
          <span>Settings</span>
        </v-tooltip>
      </div>
    </v-row>
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
    <v-row class="mt-5 mx-10 mb-5">
        <v-tooltip bottom>
          <template #activator="{ on }">
            <v-btn
              text
              small
              fab
              class="mr-0 ml-0"
              aria-label="Select Mode"
              v-on="on"
              v-on:click="enableSearchFilter()"
            >
              <v-icon v-if="searchFilterEnabled" color="grey">
                mdi-chevron-left-circle
              </v-icon>
              <v-icon v-else color="grey">
                mdi-text-box-search
              </v-icon>
            </v-btn>
          </template>
          <span>Toggle Search Filter</span>
        </v-tooltip>
        <v-tooltip bottom>
          <template #activator="{ on }">
            <v-btn
              text
              small
              fab
              class="mr-0 ml-0"
              aria-label="Select Mode"
              v-on="on"
              v-on:click="enableSelection()"
            >
              <v-icon v-if="selectMode" color="grey">
                mdi-checkbox-marked
              </v-icon>
              <v-icon v-else color="grey">
                mdi-checkbox-blank-outline
              </v-icon>
            </v-btn>
          </template>
          <span>Select Mode</span>
        </v-tooltip>
        <v-tooltip bottom>
          <template #activator="{ on }">
            <v-btn
              text
              small
              fab
              class="mr-0 ml-0"
              aria-label="Sort Torrents"
              v-on="on"
              v-on:click="enableSorting()"
            >
              <v-icon color="grey">mdi-sort</v-icon>
            </v-btn>
          </template>
          <span>Sort Torrents</span>
        </v-tooltip>
      </v-row>
    <v-list class="pa-0 transparent">
      <v-list-item v-for="torrent in getTorrents" :key="torrent.infoHash" class="mb-4">
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
                <v-col class="mr-4">
                  <div class="caption grey--text">
                    Size
                  </div>
                  <div class="truncate">
                    {{(torrent.length / (1024*1024*1024)).toFixed(2)}}
                    <span class="caption grey--text">
                      GB
                    </span>
                  </div>
                </v-col>
                <v-col class="mr-4">
                  <div class="caption grey--text">
                    Progress
                  </div>
                  <v-progress-linear
                    :value="torrent.progress[0]"
                    height="20"
                    color="green"
                    rounded
                  >
                    <span
                      class="caption white--text"
                    >
                      {{ torrent.progress[0].toFixed(2) }}%
                    </span>
                  </v-progress-linear>
                </v-col>
                <v-col class="mr-4">
                  <div class="caption grey--text">
                    Downloded
                  </div>
                  <div class="truncate">
                    {{(torrent.stats.traffic.down/(1024*1024*1024)).toFixed(2)}}
                    <span class="caption grey--text">
                      GB
                    </span>
                  </div>
                </v-col>
                <v-col class="mr-4">
                  <div class="caption grey--text">
                    Uploaded
                  </div>
                  <div class="truncate">
                    {{(torrent.stats.traffic.up/(1024*1024*1024)).toFixed(2)}}
                    <span class="caption grey--text">
                      GB
                    </span>
                  </div>
                </v-col>
                <v-col class="mr-4">
                  <div class="caption grey--text">
                    Download
                  </div>
                  <div class="truncate">
                    {{(torrent.stats.speed.down/(1024)).toFixed(2)}}
                    <span class="caption grey--text">
                      KB/s
                    </span>
                  </div>
                </v-col>
                <v-col class="mr-4">
                  <div class="caption grey--text">
                    Upload
                  </div>
                  <div class="truncate">
                    {{(torrent.stats.speed.up/(1024)).toFixed(2)}}
                    <span class="caption grey--text">
                      KB/s
                    </span>
                  </div>
                </v-col>
                <v-col class="mr-4">
                  <div class="caption grey--text">
                    ETA
                  </div>
                  <div class="truncate">
                    {{torrent.stats.eta ? getTime(torrent.stats.eta) : '∞'}}
                  </div>
                </v-col>
                <v-col class="mr-4">
                  <div class="caption grey--text">
                    Peers
                  </div>
                  <div class="truncate">
                    {{torrent.stats.peers.unchocked}}
                    <span class="caption grey--text">
                      /{{torrent.stats.peers.total}}
                    </span>
                  </div>
                </v-col>
                <v-col>
                  <div class="caption grey--text">
                    Status
                  </div>
                  <v-chip
                    small
                    class="caption white--text px-2"
                    color="green"
                  >
                    {{ getStatus(torrent) }}
                  </v-chip>
                </v-col>
              </v-row>
            </v-card>
          </template>
        </v-hover>
      </v-list-item>
    </v-list>
    <v-menu 
      v-model="showMenu"
      :position-x="x"
      :position-y="y"
      absolute
      offset-y
      v-if="torrent"
    >
      <v-list class="noselect">
        <v-list-item link v-on:click="rightMenuClick(1)">
          <v-icon v-if="torrent.interested">mdi-pause</v-icon>
          <v-icon v-else>mdi-play</v-icon>
          <v-list-item-title
            class="ml-2"
            style="font-size: 1em"
          >
            {{ torrent.interested ? 'Stop' : 'Start' }}
          </v-list-item-title>
        </v-list-item>
        <v-list-item link v-on:click="rightMenuClick(2)">
          <v-icon v-if="torrent.stats.paused">mdi-play-circle</v-icon>
          <v-icon v-else>mdi-pause-circle</v-icon>
          <v-list-item-title
            class="ml-2"
            style="font-size: 1em"
          >
            {{ torrent.stats.paused ? 'Resume' : 'Pause' }}
          </v-list-item-title>
        </v-list-item>
        <v-divider></v-divider>
        <v-list-item link v-on:click="rightMenuClick(3)">
          <v-icon color="red">mdi-delete</v-icon>
          <v-list-item-title
            class="ml-2 red--text"
            style="font-size: 1em;"
          >
            Delete
          </v-list-item-title>
        </v-list-item>
        <v-divider></v-divider>
        <v-list-item link v-on:click="rightMenuClick(5)">
          <v-icon>mdi-play</v-icon>
          <v-list-item-title class="ml-2">
            Play on Xbox
          </v-list-item-title>
        </v-list-item>
        <v-list-item link v-on:click="rightMenuClick(4)">
          <v-icon>mdi-information</v-icon>
          <v-list-item-title class="ml-2">
            Show Info
          </v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
    <v-snackbar v-model="snackbar" timeout="5000" color="blue-grey darken-2">
      {{notificationText}}
      <template v-slot:action="{ attrs }">
        <v-btn
          color="blue"
          text
          v-bind="attrs"
          @click="snackbar = false, notificationText = ''"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
    <SettingsModal v-model="showSettings"></SettingsModal>
    <AddTorrentModal v-model="showAddTorrent"></AddTorrentModal>
  </div>
</template>

<script>

module.exports = {
    name: 'Home',
    computed: {
      API() {
        let conf = this.$store.getters.getConfiguration;
        return "http://" + conf.PC.IP_ADDRESS + ":" + conf.PC.PORT;
      },
      XBOX_ADDRESS() {
        let conf = this.$store.getters.getConfiguration;
        return "http://" + conf.XBOX.IP_ADDRESS + ":" + conf.XBOX.PORT;
      },
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
        torrent: null,
        showMenu: false,
        x: 0,
        y: 0,
        snackbar: false,
        notificationText: '',
        rightMenuItems: [
          {
            icon: 'mdi-play',
            label: 'Resume' 
          },
          {
            icon: 'mdi-pause',
            label: 'Pause' 
          },
          {
            icon: 'mdi-delete',
            label: 'Delete' 
          },
          {
            icon: 'mdi-information',
            label: 'Show Info' 
          }
        ],
        searchFilterEnabled: false,
        selectMode: false,
        showAddTorrent: false,
        showSettings: false
      }
    },
    watch: {

    },
    methods: {
      addTorrent() {
        let magnet = prompt('Enter magnet link:');
        if(!magnet) { return }
        axios.post("/torrents", {"link": magnet})
          .catch(error => {
            console.log(error)
          })
      },
      resumeSelected() {
        alert('This funcionality is in development.');
      },
      pauseSelected() {
        alert('This funcionality is in development.');
      },
      removeSelected() {
        alert('This funcionality is in development.');
      },
      searchTorrents() {
        alert('This funcionality is in development.');
      },
      openSettings() {
        alert('This funcionality is in development.');
      },
      enableSearchFilter() {
        this.searchFilterEnabled = !this.searchFilterEnabled;
        alert('This funcionality is in development.');
      },
      enableSelection() {
        this.selectMode = !this.selectMode;
        alert('This funcionality is in development.');
      },
      enableSorting() {
        alert('This funcionality is in development.');
      },
      selectTorrent(torrent) {
        this.torrent = torrent;
      },
      rightMenuClick(action) {
        if(this.torrent == null) alert("Torrent is not selected!");
        if (action === 1) {
          socket.emit(this.torrent.interested ? 'stop' : 'start', this.torrent.infoHash, -1);
          this.torrent.interested = !this.torrent.interested;
        } else if(action === 2) {
          socket.emit(this.torrent.stats.paused ? 'resume' : 'pause', this.torrent.infoHash);
          this.torrent.stats.paused = !this.torrent.stats.paused;
        } else if (action === 3) {
          axios.delete("/torrents/" + this.torrent.infoHash)
        } else if (action === 4) {
          alert('This funcionality is in development.');
        } else if (action === 5) {

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
      },
      show(e) {
        e.preventDefault();
        this.showMenu = false;
        this.x = e.clientX;
        this.y = e.clientY;
        this.$nextTick(() => {
          this.showMenu = true;
        });
      },
      getTime(seconds) {
        seconds = Number(seconds);

        var d = Math.floor(seconds / (3600*24));
        var h = Math.floor(seconds % (3600*24) / 3600);
        var m = Math.floor(seconds % 3600 / 60);
        var s = Math.floor(seconds % 60);

        var dDisplay = d > 0 ? d + (d == 1 ? "d " : "d ") : "";
        var hDisplay = h > 0 ? h + (h == 1 ? "h " : "h ") : "";
        var mDisplay = m > 0 ? m + (m == 1 ? "m " : "m ") : "";
        var sDisplay = s > 0 ? s + (s == 1 ? "s" : "s") : "";
        return dDisplay + hDisplay + mDisplay + sDisplay;
      },
      getBorderColor(torrent) {
        if(!torrent.stats.paused) return '.border-downloaded'
      },
      getStatus(torrent) {
        if(torrent.interested) {
          if(torrent.stats.paused) {
            return 'Paused';
          }
          else {
            return 'Downloading';
          }
        }
        else {
          return 'Stopped';
        }
      },
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

<style scoped>
  .border-paused {
    border-left: 5px solid blue;
  }
  .border-downloading {
    border-left: 5px solid green;
  }
  .border-stoped{
    border-left: 5px solid red;
  }
</style>

