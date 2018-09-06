<template>
  <div>
    <a-row type="flex" justify="space-between" class="searchBar">
      <div>
        <a-select placeholder="DEVICE TYPE" class="condition" v-model="conditions.deviceType" @change="handleDeviceTypeChange">
          <a-select-option value="">ALL DEVICE TYPE</a-select-option>
          <a-select-option value="car">Car</a-select-option>
          <a-select-option value="charger">Charger</a-select-option>
        </a-select>
        <a-input placeholder="DEVICE ID" class="condition" v-model="conditions.deviceId" />
      </div>
      <a-button type="primary" icon="search" @click="handleSearch">Search</a-button>
    </a-row>
    <a-table :columns="columns"
      :rowKey="r => r.id"
      :dataSource="data"
      :pagination="pagination"
      :loading="loading"
      @change="handleTableChange"
    >
      <template slot="name" slot-scope="name">
        {{name.first}} {{name.last}}
      </template>
    </a-table>
  </div>
</template>

<script>
import { list } from '../apis/transaction'

export default {
  data () {
    return {
      columns: [{
        title: 'ID',
        dataIndex: 'objectId'
      }, {
        title: 'Device Id',
        dataIndex: 'deviceId'
      }, {
        title: 'Device Type',
        dataIndex: 'deviceType'
      }, {
        title: 'Created At',
        dataIndex: 'createdAt'
      }],
      data: [],
      pagination: { page: 1 },
      loading: false,

      conditions: {
        deviceId: '',
        deviceType: ''
      }
    }
  },

  mounted () {
    this.fetch(this.conditions, this.pagination)
  },

  methods: {
    fetch (conditions, pagination) {
      this.loading = true
      list(conditions, pagination).then(response => {
        const { data, status } = response.data
        const { list, meta } = data
        this.data = list
        this.pagination = {
          size: `${meta.pageSize}`,
          total: meta.total
        }
        this.loading = false
      })
    },

    handleTableChange (pagination) {
      this.fetch(this.conditions, pagination)
    },

    handleDeviceTypeChange (type) {
      this.fetch({
        ...this.condition,
        deviceType: type
      }, { page: 1 })
    },

    handleSearch () {
      this.fetch(this.conditions, this.pagination)
    }
  }
}
</script>

<style scoped>
.searchBar {
  margin-top: 10px;
  margin-bottom: 20px;
}

.condition {
  width: 200px;
  margin-right: 8px;
}
</style>