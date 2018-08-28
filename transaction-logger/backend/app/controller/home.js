'use strict'
const Controller = require('egg').Controller

class HomeController extends Controller {
  async index() {
    this.ctx.body = 'hi, this is demo of iotanet'
  }
}

module.exports = HomeController
