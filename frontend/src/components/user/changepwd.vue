<template>
  <div class="card">
    <div class="title">修改密码</div>
    <div class="space"></div>
    <div class="input-title">旧密码</div>
    <div class="space"></div>
    <el-input
      type="password"
      v-model="old_pwd"
      auto-complete="off"
      placeholder="请输入旧密码"
    >{{old_pwd}}</el-input>
    <div class="space"></div>
    <div class="input-title">新密码</div>
    <div class="space"></div>
    <el-input
      type="password"
      v-model="password"
      auto-complete="off"
      placeholder="请输入密码"
    >{{password}}</el-input>
    <div class="space"></div>
    <div class="input-title">确认登陆密码</div>
    <div class="space"></div>
    <el-input
      type="password"
      v-model="confirm_pwd"
      auto-complete="off"
      placeholder="请输入密码"
    >{{confirm_pwd}}</el-input>
    <div class="space"></div>
    <el-button type="primary" @click="submit">确认修改</el-button>
    <div class="space"></div>
  </div>
</template>
<script>
import * as Tools from '../Tools/Tools'
import axios from 'axios'
import qs from 'qs'
export default {
  data() {
    return {
      old_pwd: '',
      password: '',
      confirm_pwd: ''
    }
  },
  methods: {
    is_equal: function() {
      if (
        this.old_pwd === '' ||
        this.password === '' ||
        this.confirm_pwd === ''
      ) {
        this.$notify({
          title: '警告',
          message: '请填写所有的字段！',
          type: 'warning'
        })
        return false
      } else if (this.password !== this.confirm_pwd) {
        this.$notify({
          title: '警告',
          message: '两次密码不匹配！',
          type: 'warning'
        })
        return false
      } else {
        return true
      }
    },
    submit: function() {
      if (!this.is_equal()) {
        return
      }
      let saved = this
      axios
        .post(
          Tools.get_url() + 'change_selfpassword',
          qs.stringify({
            username: window.sessionStorage.username,
            password: saved.password,
            oldpassword: saved.old_pwd
          })
        )
        .then(function(response) {
          if (response.data.success) {
            saved.$notify({
              title: '成功',
              message: '修改管理员密码成功！',
              type: 'success',
              position: 'bottom-right'
            })
          } else {
            saved.$notify({
              title: '密码错误',
              message: '修改密码失败！',
              type: 'warning'
            })
          }
        })
    }
  }
}
</script>
