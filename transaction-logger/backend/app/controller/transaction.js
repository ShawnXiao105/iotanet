'use strict'
const Controller = require('egg').Controller
const AV = require('leancloud-storage')
const Transaction = AV.Object.extend('Transaction')

/*
const randomString = require('randomstring')
const generateData = () => {
  return {
    token: randomString.generate(90),
    address: randomString.generate(81),
    createdAt: new Date()
  }
}
*/

class TransactionController extends Controller {

  async index () {
    const { deviceId, deviceType, messageType, page = 1, pageSize = 20 } = this.ctx.query
    const query = new AV.Query('Transaction')

    deviceId && query.equalTo('deviceId', deviceId)
    deviceType && query.equalTo('deviceType', deviceType)
    messageType && query.equalTo('messageType', messageType)

    const total = await query.count()
    query.limit(pageSize)
    query.skip(pageSize * (page - 1))

    const list = await query.find()
    
    this.ctx.response.body = {
      status: 0,
      data: {
        list,
        meta: {
          total,
          totalPage: Math.ceil(total / pageSize),
          page,
          pageSize
        }
      }
    }
  }

  async show () {
    const query = new AV.Query('Transaction')
    try {
      const trx = await query.get(this.ctx.params.id)
      this.ctx.response.body = {
        status: 0,
        data: trx
      }
    } catch (e) {
      if (e.code === 101) {
        this.ctx.response.body = {
          status: 0,
          data: null
        }
      } else {
        this.ctx.response.body = {
          status: -1,
          error: { code: e.code, message: e.message }
        }
      }
    }
  }

  /**
   * POST /transaction
   * called by device with transaction log details,
   * and deliver the log to transaction logger web page via socket
   */
  async create () {
    const { body } = this.ctx.request
    const trx = new Transaction()
    let error

    ;['deviceId', 'deviceType', 'messageType'].forEach(field => {
      if (body[field]) {
        trx.set(field, body[field])
      } else {
        error = { code: 1, message: `${field} is empty` }
      }
    })

    if (error) {
      this.ctx.body = {
        status: -1,
        error
      }
      return
    }

    try {
      await trx.save()
      // broadcast the transaction data to all connected socket clients
      await this.app.io.emit('transaction', trx)
      // reply nothing in response
      this.ctx.body = trx
    } catch (e) {
      this.ctx.response.body = {
        status: -1,
        error: { code: e.code, message: e.message }
      }
    }
  }
}

module.exports = TransactionController
