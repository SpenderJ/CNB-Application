<template>

    <v-footer color="transparent" padless style="width: 100%">
        <v-img src="../../assets/beauvallon_sea.jpeg" alt="banner" class="banner" v-if="background"></v-img>
        <v-card flat tile class="white--text text-center" color="transparent" style="width: 100%">
            <v-card-text class="white--text" v-if="background">
                Coming from love by the CNB
            </v-card-text>
            <v-divider v-if="background" color="grey" style="width: 20%; margin: auto;"></v-divider>
            <v-card-text>
                <a v-for="link in links" :key="link.icon" :href="link.link" target="_blank" class="link">
                    <v-btn class="mx-4 white--text text-center" icon>
                        <v-icon size="24px">{{ link.icon }}</v-icon>
                    </v-btn>
                </a>
            </v-card-text>
        </v-card>
    </v-footer>

</template>

<script>
    export default {
        name: "Footer.vue",
        props: {
            background: Boolean
        },
        data: () => ({
            links: [
                {icon: 'fab fa-github', link: 'https://www.club-nautique-beauvallon.fr/'},
                {icon: 'fab fa-facebook', link: 'https://www.facebook.com/profile.php?id=100009301527414'},
            ]
        })
    }
</script>

<style scoped>
    .link {
        text-decoration: none
    }

    .banner {
        width: 100%;
        margin: auto;
        position: absolute;
        height: 100%;
        top: 0
    }
</style>
