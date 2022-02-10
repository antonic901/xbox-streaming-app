<template>
  <div class="text-center">
    <p>This is component.</p>
    <v-dialog v-model="dialog" width="500">
      <template v-slot:activator="{ on, attrs }">
        <v-btn color="red lighten-2" dark v-bind="attrs" v-on="on">Click Me</v-btn>
        <v-btn color="red lighten-2" dark v-on:click="buttonClickDelete">Delete test</v-btn>
        <v-btn color="red lighten-2" dark v-on:click="buttonClickUpdate">Update test</v-btn>
        <v-btn color="red lighten-2" dark v-on:click="buttonClickCreate">Create test</v-btn>
        <v-btn color="red lighten-2" dark v-on:click="buttonClickGetAll">Get all tests</v-btn>
      </template>
      <v-card>
        <v-card-title class="text-h5 grey lighten-2">Privacy Policy</v-card-title>
        <v-card-text>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="dialog = false">I accept</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>

module.exports = {
    name: 'Test',
    computed: {
        counter() {
            return this.$store.getters.getCounter
        }
    },
    data() {
        return {
            dialog: false,
            test: null
        }
    },
    methods: {
        buttonClickGetAll() {
          axios.get("http://localhost:8080/rest/test/get-all")
            .then(r => {
              this.test = r.data[0]
            })
        },
        buttonClickCreate() {
          var test = {
            isDeleted: true,
            name: 'Test 1',
            user: {
              name: 'Nikola',
              surname: 'Antonic'
            }
          }
          axios.post("http://localhost:8080/rest/test/add-test", test)
            .then(r => {
              console.log(r.data)
            })
        },
        buttonClickUpdate() {
          if(this.test == null) {
            alert("Select some test/click get all")
            return
          }
          var test = {
            id: this.test.id,
            isDeleted: false,
            name: 'Izmenjeni test',
            user: {
              id: this.test.user.id,
              name: 'Bojana',
              surname: 'Pjevalica'
            }
          }
          axios.put("http://localhost:8080/rest/test/update-test", test)
            .then(r => {
              console.log(r.data)
            })
        },
        buttonClickDelete() {
          if(this.test == null) {
            alert("Select some test/click get all")
            return
          }
          axios.delete("http://localhost:8080/rest/test/delete-test/" + this.test.id)
            .then(r => {
              console.log(r.data)
            })
        }
    },
    mounted() {
      console.log("Test is mounted.")
    }
}

</script>

<style scoped>
    
</style>
