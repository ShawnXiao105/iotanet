'use strict'

const Controller = require('egg').Controller

class TransactionController extends Controller {
  /**
   * POST /transaction
   * called by device with transaction log details,
   * and deliver the log to transaction logger web page via socket
   */
  async create () {
    this.ctx.body = 'pushed transaction'
  }
}

module.exports = TransactionController
