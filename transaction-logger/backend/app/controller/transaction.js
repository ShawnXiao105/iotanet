'use strict'
const Controller = require('egg').Controller
const randomString = require('randomstring')

const generateData = () => {
  return {
    token: randomString.generate(90),
    address: randomString.generate(81),
    createdAt: new Date()
  }
}

class TransactionController extends Controller {
  /**
   * POST /transaction
   * called by device with transaction log details,
   * and deliver the log to transaction logger web page via socket
   */
  async create () {
    console.log(this.ctx.request.body)
    // broadcast the transaction data to all connected socket clients
    await this.app.io.emit('transaction', generateData())

    // TODO emit('transaction-<type>')

    // reply nothing in response
    this.ctx.body = 'ok'
  }
}

module.exports = TransactionController
