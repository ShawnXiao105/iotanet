<template>
  <div>
    <a-button type="primary" @click="showModal">Raw</a-button>
    <a-modal
      :title="`Raw message: [${title}]`"
      :visible="visible"
      @ok="handleOk"
      @cancel="handleCancel"
    >
      <p>{{rawMessage}}</p>
    </a-modal>
  </div>
</template>

<script>
  export default {
    props: {
      title: String,
      rawMessage: String
    },

    data () {
      return {
        visible: false
      }
    },
    methods: {
      showModal () {
        this.visible = true
      },
      handleOk (e) {
        this.visible = false
      },
      handleCancel (e) {
        this.visible = false
      }
    }
  }
</script>