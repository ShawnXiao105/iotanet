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
      <template slot="createdAt" slot-scope="value">
        <span>{{value | timeFormater}}</span>
      </template>
      <template slot="operation" slot-scope="text, record">
        <raw-message-modal :rawMessage="JSON.stringify(record.raw, null, 2)" :title="record.objectId" />
      </template>
    </a-table>
  </div>
</template>

<script>
import day from 'dayjs'
import { list } from '../apis/transaction'
import RawMessageModal from '../modals/RawMessage'
const PAGE_SIZE = 20

export default {
  components: {
    RawMessageModal
  },

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
        dataIndex: 'createdAt',
        scopedSlots: { customRender: 'createdAt' }
      }, {
        title: 'Operation',
        dataIndex: '',
        scopedSlots: { customRender: 'operation' }
      }],
      data: [],
      pagination: { current: 1, pageSize: PAGE_SIZE, total: 0 },
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
    fetch (conditions, { current, pageSize = PAGE_SIZE }) {
      this.loading = true
      list(conditions, { page: current, pageSize }).then(response => {
        const { data, status } = response.data
        const { list, meta } = data
        this.data = list
        this.pagination = {
          current: meta.page * 1,
          pageSize: meta.pageSize * 1,
          total: meta.total
        }
        this.loading = false
      })
    },

    handleTableChange ({ current }) {
      this.fetch(this.conditions, { current })
    },

    handleDeviceTypeChange (type) {
      this.fetch({
        ...this.condition,
        deviceType: type
      }, { current: 1 })
    },

    handleSearch () {
      this.fetch(this.conditions, this.pagination)
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
.searchBar {
  margin-top: 10px;
  margin-bottom: 20px;
}

.condition {
  width: 200px;
  margin-right: 8px;
}
</style>