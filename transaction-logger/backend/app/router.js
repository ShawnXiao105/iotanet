'use strict'

const APP_ID = '3Fhv8rFwcN2IX6JHDxmomozU-gzGzoHsz'
const APP_KEY = 'EUNG1BzfzHjL6UAb6YY2oyGD'
const AV = require('leancloud-storage')

AV.init({
  appId: APP_ID,
  appKey: APP_KEY
})

/**
 * @param {Egg.Application} app - egg application
 */
module.exports = app => {
  const { router, controller } = app
  
  router.get('/', controller.home.index)
  router.resources('transaction', '/api/transaction', controller.transaction)

  // socket.io
  /* app.io.route('PING', app.io.controller.index.ping)
  app.io.route('connect', app.io.controller.index.connect)
  app.io.route('disconnect', app.io.controller.index.disconnect) */
}
