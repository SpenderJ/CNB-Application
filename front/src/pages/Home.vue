<template>
  <div class="main">
    
    <v-container fluid class="pa-0">
      <v-row no-gutters justify="center" align="center">

        <v-col cols="12">
          <welcome-screen></welcome-screen>
        </v-col>

        <v-col cols="12">
          <v-card class="elevation-0 mt-5" color="transparent">
            <v-card-text class="text-center display-1 font-weight-bold">
              Welcome to the CNB dashboard
            </v-card-text>
            <v-card-text>
              <main-stack v-for="stack in mainStacks" :key="stack.name" :stack="stack"></main-stack>
            </v-card-text>
          </v-card>
        </v-col>

        <v-col cols="12">
          <v-parallax dark src="../assets/beauvallon_sea.jpeg" class="mb-5 slant" height="800">
            <v-container fluid>
              <v-row dense align="center" justify="center">
                <v-col cols="12" align-self="center" class="mb-5 pb-5">
                  <v-row justify="center" class="display-1">Our other services</v-row>
                </v-col>
                <v-col class="text-center mt-5" cols="2" v-for="stack in backendStacks" :key="stack.name">
                  <backend-stack :stack="stack"></backend-stack>
                </v-col>
              </v-row>
            </v-container>
          </v-parallax>
        </v-col>

        <v-col cols="12" style="margin-bottom: 5em">
          <v-card class="elevation-0 mt-5 mb-5" color="transparent">
            <v-card-text class="text-center display-1 font-weight-bold">
              Already secure
            </v-card-text>
            <v-row align="center" justify="center">
              <v-col cols="2" v-for="auth in auths" v-bind:data="auth" v-bind:key="auth.name">
                <auth-type :auth="auth"></auth-type>
              </v-col>
            </v-row>
          </v-card>
        </v-col>

      </v-row>
    </v-container>
    
  </div>
</template>

<script>
  import WelcomeScreen from "../components/home/WelcomeScreen";
  import MainStack from "../components/home/MainStack";
  import BackendStack from "../components/home/BackendStack";
  import AuthType from "../components/home/AuthType";

  export default {
    name: 'Main',
    components: {AuthType, BackendStack, MainStack, WelcomeScreen},
    data() {
      return {
        mainStacks: [
          {
            name: 'Manage booking',
            caption: 'Create or manage a booking',
            description: 'Create, manage, cancel or end any catamaran, windsurf, paddle booking.',
            logo: require('../assets/logos/windsurf_logo.jpeg'),
            link: 'https://vuejs.org/',
            reverse: false
          },
          {
            name: 'Manage family membership',
            caption: 'Create or manage a family membership',
            description: 'Create or manage a family membership.',
            logo: require('../assets/logos/cnb_club.jpeg'),
            link: 'https://vuetifyjs.com/en/',
            reverse: true
          },
          {
            name: 'Manage sailing program',
            caption: 'Display sailing program planning',
            description: 'Display sailing program planning and/or add a new member to the planning',
            logo: require('../assets/logos/catamaran_group.jpeg'),
            link: 'http://flask.palletsprojects.com/en/1.1.x/',
            reverse: false
          }
        ],
        backendStacks: [
          {
            name: 'Beverages',
            description: 'The World\'s best drinks you\'ll ever get on a beach',
            logo: require('../assets/logos/drink_logo.png'),
            link: 'https://www.elastic.co/'
          },
          {
            name: 'Ponton booking',
            description: 'The most exclusive ponton in the whole gulf',
            logo: require('../assets/logos/boat_logo.png'),
            link: 'https://www.postgresql.org/'
          },
          {
            name: 'Create an invoice',
            description: 'Generates an invoice for a specific family',
            logo: require('../assets/logos/invoice_logo.png'),
            link: 'https://redis.io/'
          },
          {
            name: 'Generate the weather',
            description: 'Because even the best sailors need to check the weather',
            logo: require('../assets/logos/weather_logo.png'),
            link: 'https://min.io/'
          }
        ],
        auths: [
          {name: 'Email', logo: require('../assets/logos/email.png')}
        ]
      }
    }
  }
</script>

<style scoped>
  .main{
    width: 100%;
    height: 100%
  }

  .slant {
    position: relative;
    overflow: hidden;
    z-index: 0;
    -webkit-clip-path: polygon(0 0, 100% 15%, 100% 80%, 0 100%);
    clip-path: polygon(0 0, 100% 15%, 100% 80%, 0 100%);
  }
</style>