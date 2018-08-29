<template>
  <div id="app">
    <a-row type="flex" justify="center">

      <a-col :lg="14" :sm="20" :xs="24">
        <div class="top">
          <a-row type="flex" justify="space-between" align="center">
            <h1>Live</h1>
            <h4>3.5 FPS <a-icon type="question-circle-o" /></h4>
          </a-row>

          <a-radio-group>
            <a-radio :style="radioStyle" :value="1">Option A</a-radio>
            <a-radio :style="radioStyle" :value="2">Option B</a-radio>
            <a-radio :style="radioStyle" :value="3">Option C</a-radio>
          </a-radio-group>
        </div>

        <transaction-list :list-data="transactionList" />

      </a-col>
    </a-row>
    
  </div>
</template>

<script>
import TransactionList from './components/TransactionList.vue'

export default {
  name: 'app',
  components: {
    TransactionList
  },

  data () {
    return {
      radioStyle: {
        display: 'block',
        height: '24px',
        lineHeight: '24px',
      },
      transactionList: [{
        token: 'MEYFZZRFGUMKALBBBLBAYEMHQXAISWZQTYBRR99QYYGHUSMD9DUVNDCTOBJOMUHINKJCNCNUGODC99999',
        address: 'NQYOTNJLFSESXGVW9UFZQWZFNZKTCKPSQONBMAYKGCBUJVPMGFZLG9WULLPZQMLAGQMVTZTJJTZGHHOBWZNNQXXTVX',
        createdAt: new Date()
      }, {
        token: 'MEYFZZRFGUMKALBBBLBAYEMHQXAISWZQTYBRR99QYYGHUSMD9DUVNDCTOBJOMUHINKJCNCNUGODC99999',
        address: 'NQYOTNJLFSESXGVW9UFZQWZFNZKTCKPSQONBMAYKGCBUJVPMGFZLG9WULLPZQMLAGQMVTZTJJTZGHHOBWZNNQXXTVX',
        createdAt: new Date()
      }]
    }
  },
  
  sockets: {
    connect () {
      console.log('connected')
    },
    transaction (trx) {
      console.log('trx', trx)
    }
  }
}
</script>

<style scoped>
.top {
  padding-bottom: 40px;
  border-bottom: 1px solid #e6e6e6;
}
</style>
