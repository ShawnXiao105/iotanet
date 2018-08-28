'use strict'
const Controller = require('egg').Controller

class IOIndexController extends Controller {
  async connect () {
    console.log('connect')
  }

  async disconnect () {
    console.log('disconnect')
  }

  async ping () {
    // const message = this.ctx.args[0]
    await this.ctx.socket.emit('PONG', `PONG`)
  }
}

module.exports = IOIndexController
