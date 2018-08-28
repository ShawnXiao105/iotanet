'use strict'

module.exports = appInfo => {
  const config = exports = {}

  // use for cookie sign key, should change to your own and keep security
  config.keys = appInfo.name + '_1534912796858_8116'

  // add your config here
  config.middleware = []

  config.security = {
    csrf: {
      ignore: ctx => true
    },
    ignore: '/api/',
    domainWhiteList: []
  }

  // socket.io
  config.io = {
    init: { }, // passed to engine.io
    namespace: {
      '/': {
        connectionMiddleware: ['auth'],
        packetMiddleware: ['filter']
      }
    },
    /* redis: {
      host: '127.0.0.1',
      port: 6379
    } */
  }

  return config;
};
