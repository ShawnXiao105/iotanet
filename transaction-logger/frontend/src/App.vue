<template>
  <div id="app">
    <a-row type="flex" justify="center">

      <a-col :lg="14" :sm="20" :xs="24">
        <div class="top">
          <a-row type="flex" justify="space-between" align="middle">
            <h1 class="title">Live<span class="indicator" :key="renderKey" /></h1>
            <h4 class="fps">3.5 FPS <a-icon type="question-circle-o" /></h4>
          </a-row>

          <a-radio-group class="radioGroup">
            <a-radio :style="radioStyle" :value="1">All transactions</a-radio>
            <a-radio :style="radioStyle" :value="2">Only none-zero value</a-radio>
            <a-radio :style="radioStyle" :value="3">Only positive</a-radio>
          </a-radio-group>
        </div>

        <transaction-list :list-data="transactionList" />

      </a-col>
    </a-row>
    
  </div>
</template>

<script>
import randomString from 'randomstring'
import TransactionList from './components/TransactionList.vue'

const MAX_LENGTH = 100

export default {
  name: 'app',
  components: {
    TransactionList
  },

  data () {
    return {
      renderKey: Date.now(),
      radioStyle: {
        display: 'block',
        height: '24px',
        lineHeight: '24px',
      },
      transactionList: []
    }
  },
  
  sockets: {
    connect () {
      console.log('connected')
    },
    transaction (trx) {
      console.log('trx', trx)
      this.push(trx)
      this.renderKey = Date.now()
    }
  },

  methods: {
    push (data) {
      if (this.transactionList.length < MAX_LENGTH) {
        this.transactionList.unshift(data)
      } else {
        this.transactionList.pop()
        this.transactionList.unshift(data)
      }
    }
  }
}
</script>

<style scoped>
.top {
  padding-bottom: 40px;
  border-bottom: 1px solid #e6e6e6;
}
.title {
  position: relative;
  font-size: 42px;
  font-weight: 300;
}
.indicator {
  position: absolute;
  display: inline-block;
  top: 50%;
  left: 80px;
  transform: translateY(-50%);
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: red;
  animation: pulse 1s;
}
.fps {
  margin-top: 8px;
  font-size: 26px;
  font-weight: 200;
}
.radioGroup {
  margin-left: 24px;
}
@keyframes pulse {
  0% {
    box-shadow: 0 0 0 0 rgba(255,0,0,.4)
  }
  70% {
    box-shadow: 0 0 0 10px rgba(255,0,0,0)
  }
  100% {
    box-shadow: 0 0 0 0 rgba(255,0,0,0)
  }
}
</style>
