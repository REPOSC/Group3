<template>
  <div class="card">
    <div class="title space">修改账户密码</div>
    <div class="input-title space">会员账号</div>
    <el-input
      type="text"
      v-model="username"
      auto-complete="off"
      placeholder="请输入您的账号"
    >{{username}}</el-input>
    <div class="input-title space">新密码</div>
    <el-input
      type="password"
      v-model="password"
      auto-complete="off"
      placeholder="请输入密码"
    >{{password}}</el-input>
    <div class="input-title space">确认密码</div>
    <el-input
      type="password"
      v-model="confirm_pwd"
      auto-complete="off"
      placeholder="请输入密码"
    >{{password}}</el-input>
    <el-button class="space" type="primary" @click="submit">确认修改</el-button>
  </div>
</template>

<script>
import * as Tools from '../Tools/Tools.js'
import qs from 'qs'
import axios from 'axios'
export default {
  data: function() {
    return {
      username: '',
      password: '',
      confirm_pwd: ''
    }
  },
  methods: {
    submit: function() {
      if (
        this.username === '' ||
        this.password === '' ||
        this.confirm_pwd === ''
      ) {
        this.$notify({
          title: '警告',
          message: '请填写所有的字段！',
          type: 'warning'
        })
        return
      } else if (this.password !== this.confirm_pwd) {
        this.$notify({
          title: '警告',
          message: '两次密码不一致！',
          type: 'warning'
        })
        return
      }
      let saved = this
      axios
        .post(
          Tools.get_url() + 'change_password',
          qs.stringify({
            username: saved.username,
            password: saved.password
          })
        )
        .then(function(response) {
          if (response.data.success) {
            saved.$notify({
              title: '成功',
              message: '密码修改成功！',
              type: 'success',
              position: 'bottom-right'
            })
          } else {
            saved.$notify({
              title: '警告',
              message: '修改失败，用户不存在！',
              type: 'warning'
            })
          }
        })
    }
  }
}
</script>
