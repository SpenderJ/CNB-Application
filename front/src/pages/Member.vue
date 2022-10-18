<template>
    <div class="edit-member">

        <v-img src="../assets/cnb_background.jpeg" alt="banner" class="banner"></v-img>
        <v-container class="create-members">
            <v-layout row justify-center align-center fill-height>
                <v-flex xs12 sm6>
                    <v-hover v-slot:default="{ hover }">
                        <v-card flat id="card" class="pa-5 expand-transition" :elevation="hover ? 12 : 5">
                            <v-card-text class="subtitle-1 pt-2 pb-0">Create a new family membership: </v-card-text>
                            <v-card-text primary-title class="pt-2 pb-0 mb-2">
                                <v-form ref="form" lazy-validation>
                                  <v-text-field outline label="First Name" v-model="first_name" required></v-text-field>
                                  <v-text-field outline label="Last Name" v-model="last_name" required></v-text-field>
                                  <v-text-field outline label="Email" v-model="email" required></v-text-field>
                                  <v-text-field outline label="Phone Number" v-model="phone_number" required></v-text-field>
                                  <v-checkbox outline label="Benefactor Member" v-model="benefactor_member" required></v-checkbox>
                                  <v-checkbox outline label="Parking" v-model="parking" required></v-checkbox>
                                  <v-text-field outline label="Address" v-model="address" required></v-text-field>
                                  <v-text-field outline label="City" v-model="city" required></v-text-field>
                                  <v-text-field outline label="Zip Code" v-model="zip_code" required></v-text-field>
                                  <v-text-field outline label="Country" v-model="country" required></v-text-field>
                                </v-form>
                            </v-card-text>
                            <v-card-text class="mt-5">
                                <v-layout row>
                                    <v-btn class="button mx-3" to="/login" color="error" text>Cancel</v-btn>
                                    <v-spacer></v-spacer>
                                    <v-btn class="button mx-3" @click="validate()" color="primary">Send</v-btn>
                                </v-layout>
                            </v-card-text>
                        </v-card>
                    </v-hover>
                </v-flex>
            </v-layout>
        </v-container>

    </div>
</template>

<script>
    import axios from 'axios';
    import notifications from '@/modules/notifications'

    export default {
        name: "Member",
        data() {
          return {
            first_name: null,
            last_name: null,
            email: null,
            phone_number: null,
            benefactor_member: false,
            parking: false,
            address: null,
            city: null,
            zip_code: null,
            country: null,
          }
        },
        mounted() {
          this.getFamily()
        },
        methods: {
            getFamily() {
              axios.get(process.env.VUE_APP_API_URL + `/family/${this.$route.params.id}`)
                        .then(response => {
                            notifications.addNotification(response.data.msg);
                            return {
                              first_name: response.data.user.first_name,
                              last_name: response.data.user.last_name,
                              email: response.data.user.email,
                              phone_number: response.data.user.phone_number,
                              benefactor_member: response.data.user.benefactor_member,
                              parking: response.data.user.parking,
                              address: response.data.user.address,
                              city: response.data.user.city,
                              zip_code: response.data.user.zip_code,
                              country: response.data.user.country,
                            }
                        })
                        .catch(error => {
                          if (error.response) {
                        notifications.addNotification(error.response.data.error);
                          } else {
                            notifications.addNotification('We\'re sorry, an error occurred')
                          }
                        })
            },
            validate() {
                if (this.$refs.form.validate()) {
                    axios.get(process.env.VUE_APP_API_URL + '/family',{ params: {first_name: this.first_name, last_name: this.last_name}})
                        .then(response => {
                            notifications.addNotification(response.data.msg);
                            this.$router.replace('/')
                        })
                        .catch(error => {
                          console.log(error)
                          notifications.addNotification(error.response.data.error)
                        })
                }
            }
        }
    }
</script>

<style scoped>
    .forgot-password {
        width: 100%;
        height: 100%
    }

    #card {
        margin: 4em;
        border-radius: 8px;
        background-color: rgba(255, 255, 255, 0.70);
    }

    .banner {
        width: 100vw;
        margin: auto;
        position: fixed;
        height: 100vh;
        top: 0
    }

    .button {
        text-transform: None !important;
    }
</style>