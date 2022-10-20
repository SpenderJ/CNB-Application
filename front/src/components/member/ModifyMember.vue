<template>

    <v-row justify="center" align="center" style="height: 100%">
        <v-col cols="6" class="py-0">

            <v-avatar :size="140" color="secondary">
                <v-icon large color="white">account_circle</v-icon>
            </v-avatar>

            <v-card color="transparent" elevation="0">
                <v-card-text class="display-1 white--text mb-5">{{ member.profile.first_name + " " + member.profile.last_name }}</v-card-text>

                <v-card-text class="text-start" v-for="field in fields" :key="field.field">
                    <v-row dense>
                        <v-col cols="8">
                            <span class="primary--text font-weight-light">{{ field.text }}</span>
                        </v-col>
                        <v-col cols="4" class="py-0">
                            <v-row dense justify="end" align="center" v-if="!field.modify">
                                <v-btn icon text small @click="field.modify = true">
                                    <v-icon small color="white">
                                        edit
                                    </v-icon>
                                </v-btn>
                            </v-row>
                            <v-row dense justify="end" align="center" v-else>
                                <v-btn icon text small
                                       @click="field.modify = false; field.value = member.profile[field.field]">
                                    <v-icon small color="error">
                                        cancel
                                    </v-icon>
                                </v-btn>
                                <v-btn icon text small @click="updateField(field)" :disabled="!field.value">
                                    <v-icon small color="primary">
                                        save
                                    </v-icon>
                                </v-btn>
                            </v-row>
                        </v-col>
                    </v-row>
                    <v-divider color="white" class="mb-3"></v-divider>
                    <v-text-field
                            v-if="field.modify"
                            v-model="field.value"
                            dark
                            clearable
                            class="my-0 py-0 title"
                    ></v-text-field>
                    <span class="white--text title" v-else>{{ member.profile[field.field] }}</span>
                </v-card-text>

                <v-card-text class="text-start pb-0">
                    <v-row dense>
                        <v-col cols="8">
                            <span class="primary--text font-weight-light">Email</span>
                        </v-col>
                        <v-col cols="4" class="py-0">
                            <v-row dense justify="end" align="center">
                                <v-btn icon text small>
                                    <v-icon small color="white">
                                        edit
                                    </v-icon>
                                </v-btn>
                            </v-row>
                        </v-col>
                    </v-row>
                </v-card-text>
            </v-card>

        </v-col>
    </v-row>

</template>

<script>
    import axios from 'axios';
    import notifications from '@/modules/notifications';

    export default {
        name: "ModifyMember",
        props: {
            member: Object,
            updateMember: Function
        },
        data() {
            return {
                fields: [
                    {
                        text: 'First name',
                        value: null,
                        modify: false,
                        field: 'first_name'
                    },
                    {
                        text: 'Last name',
                        value: null,
                        modify: false,
                        field: 'last_name'
                    }
                ],
            }
        },
        mounted() {
            for (let i = 0; i < this.fields.length; i++) {
                this.fields[i].value = this.member.profile[this.fields[i].field]
            }
        },
        methods: {
            updateField(field) {
                axios.patch(process.env.VUE_APP_API_URL + `/family/${this.member.profile.id}`,
                    {value: field.value},
                    {params: {field: field.field}}
                ).then(response => {
                    if (response.data.msg === 'success') {
                        this.$emit('update', response.data.family);
                        field.modify = false
                    }
                }).catch(error => {
                    if (error.response) {
                        notifications.addNotification(error.response.data.error);
                    } else {
                        notifications.addNotification('We\'re sorry, an error occurred')
                    }
                    field.modify = false
                })
            }
        }
    }
</script>

<style scoped>

</style>