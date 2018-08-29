import Vue from 'vue'
import Antd from 'ant-design-vue'
import VueSocketIO from 'vue-socket.io'
import App from './App.vue'
import 'ant-design-vue/dist/antd.css'

Vue.use(Antd)
Vue.use(VueSocketIO, 'http://localhost:7001')
Vue.config.productionTip = false

new Vue({
  render: h => h(App)
}).$mount('#app')
