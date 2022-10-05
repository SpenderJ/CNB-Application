const fs = require('fs');

module.exports = {
  "transpileDependencies": [
    "vuetify"
  ],
   devServer: {
    https: {
      key: fs.readFileSync('./certs/localhost-key.pem'),
      cert: fs.readFileSync('./certs/localhost.pem'),
    },
    client: {
    webSocketURL: {
        hostname: "0.0.0.0",
        pathname: "/ws",
        port: 8080,
      },
    },
  },
};
