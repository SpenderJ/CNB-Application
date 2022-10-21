<template>

    <v-row justify="center" align="center" style="height: 100%">
        <v-col cols="6" class="py-0">

            <v-avatar :size="140" color="secondary">
                <v-icon large color="white">account_circle</v-icon>
            </v-avatar>

            <v-card color="transparent" elevation="0">
                <v-card-text class="display-1 white--text mb-5">{{ member.profile.first_name }}</v-card-text>

                <v-card-text class="text-start pt-5">
                    <span class="primary--text font-weight-light">First name</span>
                    <v-divider color="white" class="mb-3"></v-divider>
                    <span class="white--text title">{{ member.profile.first_name }}</span>
                </v-card-text>

                <v-card-text class="text-start">
                    <span class="primary--text font-weight-light">Last name</span>
                    <v-divider color="white" class="mb-3"></v-divider>
                    <span class="white--text title">{{ member.profile.last_name }}</span>
                </v-card-text>
            </v-card>

        </v-col>
    </v-row>

</template>

<script>
    export default {
        name: "ViewMember",
        props: {
            member: Object
        },
    }
</script>

<style scoped>

</style>
