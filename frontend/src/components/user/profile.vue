<template>
  <div class="card">
    <div class="fillcontain">
      <header class="admin_title title">管理员信息</header>
      <div class="admin_set space">
        <ul>
          <li class="space input-title">
            <span>姓名：{{name}}</span>
          </li>
          <li class="space input-title">
            <span>注册时间：{{time}}</span>
          </li>
          <li class="space input-title">
            <span>管理员权限：{{power}}</span>
          </li>
          <li class="space input-title">
            <span>管理员 ID：{{number}}</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import qs from 'qs'
import * as Tools from '../Tools/Tools'
export default {
  data() {
    return {
      name: null,
      time: null,
      power: null,
      number: window.sessionStorage.username
    }
  },
  mounted() {
    this.init()
  },
  methods: {
    init: function() {
      let save = this
      axios
        .post(
          Tools.get_url() + 'get_manager_info',
          qs.stringify({
            username: window.sessionStorage.username
          })
        )
        .then(function(response) {
          save.name = response.data.name
          save.time = response.data.time
          save.power = response.data.power
        })
    }
  }
}
</script>

<style >
.admin_set {
  text-align: left;
}
</style>
