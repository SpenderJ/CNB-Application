<template>
    <div class="edit-member">

        <v-img src="../assets/cnb_background.jpeg" alt="background" class="background"></v-img>
        <v-container class="container" v-if="loaded">
            <modify-member
                    :member="member"
                    @update="updateFamily"
            ></modify-member>
        </v-container>

    </div>
</template>

<script>
    import axios from 'axios';
    import notifications from '@/modules/notifications';
    import auth from '@/modules/auth';
    import ModifyMember from "../components/member/ModifyMember";

    export default {
        name: "Member",
        components: {ModifyMember},
        data() {
          return {
            loaded: false,
            member: null,
          }
        },
        mounted() {
          this.getFamily()
        },
        methods: {
            getFamily() {
              axios.get(process.env.VUE_APP_API_URL + `/family/${this.$route.params.id}`)
                        .then(response => {
                            if (response.data.status === 200) {
                              this.member = response.data.family;
                              this.loaded = true;
                            }
                            console.log(this.member)
                        })
                        .catch(error => {
                          if (error.response) {
                        notifications.addNotification(error.response.data.error);
                          } else {
                            notifications.addNotification('We\'re sorry, an error occurred')
                          }
                        })
            },
            updateFamily(member) {
                this.member = member;
                auth.getMemberInfo(this.$route.params.id)
            }
        }
    }
</script>

<style scoped>
    .edit-member {
        width: 100%;
        text-align: center;
        height: 100%;
        padding-top: 60px;
    }
</style>
