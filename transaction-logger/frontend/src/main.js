import Vue from 'vue'
import VueRouter from 'vue-router'

import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.css'

import VueSocketIO from 'vue-socket.io'

import App from './App.vue'
import Live from './pages/Live'
import Search from './pages/Search'

Vue.use(VueRouter)
Vue.use(Antd)
Vue.use(VueSocketIO, 'http://jackyang.me:7001')
Vue.config.productionTip = false


const router = new VueRouter({
  routes: [{
    name: 'live',
    path: '/', component: Live
  }, {
    name: 'search',
    path: '/search', component: Search
  }]
})

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
