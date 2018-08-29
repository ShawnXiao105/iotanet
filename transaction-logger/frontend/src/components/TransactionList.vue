<template>
  <div class="list">
    <div class="item" v-for="item in listData" :key="item.token">
      <a-row class="item__title" type="flex" justify="space-between" align="middle">
        <h4 class="item__time">{{item.createdAt | timeFormater}}</h4>
        <a-tag color="pink">1M</a-tag>
      </a-row>
      <a-row>
        <div class="item__address"><a-icon type="arrow-right" /> {{item.address}}</div>
        <div class="item__token">{{item.token}}</div>
      </a-row>
    </div>
  </div>
</template>

<script>
import day from 'dayjs'

export default {
  props: {
    listData: {
      type: Array,
      required: true,
      default: () => []
    }
  },

  filters: {
    timeFormater (value) {
      return day(value).format('MMM DD, YYYY HH:mm:ss')
    }
  }
}
</script>

<style scoped>
.list {
  margin: 0 10px;
}
.item {
  padding: 20px 0 8px 0;
  border-bottom: 1px solid #e6e6e6;
}
.item__title {
  margin-bottom: 6px;
}
.item__time {
  margin: 0;
}
.item__address {
  font-size: 14px;
  color: rgba(0,0,0,.9);
  overflow-wrap: break-word;
}
.item__token {
  font-size: 16px;
  line-height: 17px;
  color: #00a0ff;
  overflow-wrap: break-word;
}
</style>