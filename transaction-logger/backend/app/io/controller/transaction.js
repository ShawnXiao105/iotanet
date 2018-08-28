'use strict'
const Controller = require('egg').Controller

class IOTransactionController extends Controller {

  async ping () {
    // const message = this.ctx.args[0]
    await this.ctx.socket.emit('PONG', `PONG`)
  }
}

module.exports = IOTransactionController
