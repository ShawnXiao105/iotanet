'use strict'

/**
 * @param {Egg.Application} app - egg application
 */
module.exports = app => {
  const { router, controller } = app
  
  router.get('/', controller.home.index)

  router.post('/transaction', controller.transaction.create)

  // socket.io
  app.io.route('transaction', app.io.controller.transaction.ping)
}
