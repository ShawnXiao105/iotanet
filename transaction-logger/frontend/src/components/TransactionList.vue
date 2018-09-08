<template>
  <div class="list">
    <transition-group name="list" tag="div">
      <div class="item" v-for="item in listData" :key="item.objectId">
        <a-row class="item__title" type="flex" justify="space-between" align="middle">
          <h4 class="item__time">{{item.createdAt | timeFormater}}</h4>
          <a-tag color="green">{{item.messageType}}</a-tag>
        </a-row>
        <a-row>
          <div class="item__address">[{{item.deviceType}}#{{item.deviceId}}]<a-icon type="arrow-right" /></div>
          <div class="item__token">{{item | raw}}</div>
        </a-row>
      </div>
    </transition-group>
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
    },
    raw ({ deviceId, deviceType, createdAt, updatedAt, messageType, ...rest }) {
      return JSON.stringify(rest)
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

.list-enter-active, .list-leave-active {
  transition: all .3s;
}
.list-enter, .list-leave-to /* .list-leave-active below version 2.1.8 */ {
  opacity: 0;
  transform: translateY(20px);
}
</style>