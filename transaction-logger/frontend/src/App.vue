<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

import io from 'socket.io-client'
const socket = io('http://127.0.0.1:7001')


socket.on('connect', () => {
  /* eslint-disable */
  console.log('connect!', socket.id)
  socket.emit('PING')
})

socket.on('PONG', msg => {
  /* eslint-disable */
  console.log('PONG msg', msg)
})

/* eslint-disable */
socket.on('transaction', msg => console.log('transaction', msg))

window.socket = socket

export default {
  name: 'app',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
