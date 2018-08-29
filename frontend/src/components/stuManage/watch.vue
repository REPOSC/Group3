<template>
  <div class="card">
    <div class="fillcontain">
      <header class="admin_title title">学生信息</header>
      <div class="admin_set space">
        <ul>
          <li class="space input-title">
            <span>用户名：{{name}}</span>
          </li>
          <li class="space input-title">
            <span>注册时间：{{time}}</span>
          </li>
          <li class="space input-title">
            <span>昵称：{{nickname}}</span>
          </li>
          <li class="space input-title">
            <span>上次登录等级：{{lasttime_level}}</span>
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
      nickname: null,
      lasttime_level: null
    }
  },
  mounted() {
    this.name = this.$route.params.name
    this.init()
  },
  methods: {
    init: function() {
      let save = this
      axios
        .post(
          Tools.get_url() + 'get_student_info',
          qs.stringify({
            username: this.name
          })
        )
        .then(response => {
          save.nickname = response.data.nickname
          save.time = response.data.time
          save.lasttime_level = parseInt(response.data.lasttime_level) + 1
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
