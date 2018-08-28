'use strict'
const Controller = require('egg').Controller

class TransactionController extends Controller {
  /**
   * POST /transaction
   * called by device with transaction log details,
   * and deliver the log to transaction logger web page via socket
   */
  async create () {
    const transactionData = { datetime: new Date() } // this.ctx.request.body

    // broadcast the transaction data to all connected socket clients
    await this.app.io.emit('transaction', transactionData)

    // TODO emit('transaction-<type>')

    // reply nothing in response
    this.ctx.body = 'ok'
  }
}

module.exports = TransactionController
