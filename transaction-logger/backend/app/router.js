'use strict'

/**
 * @param {Egg.Application} app - egg application
 */
module.exports = app => {
  const { router, controller } = app
  
  router.get('/', controller.home.index)
  router.post('/api/transaction', controller.transaction.create)

  // socket.io
  /* app.io.route('PING', app.io.controller.index.ping)
  app.io.route('connect', app.io.controller.index.connect)
  app.io.route('disconnect', app.io.controller.index.disconnect) */
}
