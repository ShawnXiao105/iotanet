<template>
  <div id="app">
    <a-row type="flex" justify="center" style="background:#001529;margin-bottom: 20px">
      <a-col :lg="14" :sm="20" :xs="24">
        <a-menu
          theme="dark"
          mode="horizontal"
          :defaultSelectedKeys="['']"
          :selectedKeys="[$route.name]"
          :style="{ lineHeight: '64px' }"
        >
          <a-menu-item key="live"><router-link to="/">LIVE</router-link></a-menu-item>
          <a-menu-item key="search"><router-link to="/search">SEARCH</router-link></a-menu-item>
        </a-menu>
      </a-col>
    </a-row>
    <a-row type="flex" justify="center">
      <a-col :lg="14" :sm="20" :xs="24">
        <router-view />
      </a-col>
    </a-row>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style scoped>
</style>
