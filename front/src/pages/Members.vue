<template>
    <div class="members">

        <v-img src="../assets/cnb_background.jpeg" alt="banner" class="banner"></v-img>
        <v-container class="members">
            <v-layout row justify-center align-center fill-height>
                <v-flex xs12 sm6>
                    <v-hover v-slot:default="{ hover }">
                        <v-card flat id="card" class="pa-5 expand-transition" :elevation="hover ? 12 : 5">
                            <v-card-text class="subtitle-1 pt-2 pb-0">Family you are looking for:</v-card-text>
                            <v-card-text primary-title class="pt-2 pb-0 mb-2">
                                <v-form ref="form" lazy-validation>
                                  <v-text-field outline label="First Name" v-model="first_name" required></v-text-field>
                                  <v-text-field outline label="Last Name" v-model="last_name" required></v-text-field>
                                </v-form>
                            </v-card-text>
                            <v-card-text class="mt-5">
                                <v-layout row>
                                    <v-btn class="button mx-3" to="/login" color="error" text>Cancel</v-btn>
                                    <v-spacer></v-spacer>
                                    <v-btn class="button mx-3" @click="validate()" color="primary">Look up</v-btn>
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
        name: "MembersSearch",
        data() {
            return {
                first_name: null,
                last_name: null,
            }
        },
        methods: {
            validate() {
                if (this.$refs.form.validate()) {
                    axios.get(process.env.VUE_APP_API_URL + '/family',{ params: {first_name: this.first_name, last_name: this.last_name}})
                        .then(response => {
                            notifications.addNotification(response.data.msg);
                            this.$router.replace(`/member/${response.data.family.id}`)
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