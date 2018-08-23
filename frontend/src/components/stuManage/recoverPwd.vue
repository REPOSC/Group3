<template>
  <div class="card">
    <div class="title">修改账户密码</div>
    <div class="space"></div>
    <div class="input-title">会员账号</div>
    <div class="space"></div>
    <el-input type="text" v-model="username" auto-complete="off" placeholder="请输入您的账号">{{username}}</el-input>
    <div class="space"></div>
    <div class="input-title">新密码</div>
    <div class="space"></div>
    <el-input type="password" v-model="password" auto-complete="off" placeholder="请输入密码">{{password}}</el-input>
    <div class="space"></div>
    <div class="input-title">确认密码</div>
    <div class="space"></div>
    <el-input type="password" v-model="confirm_pwd" auto-complete="off" placeholder="请输入密码">{{password}}</el-input>
    <div class="space"></div>
    <el-button type="primary" @click="submit">确认修改</el-button>
    <div class="space"></div>
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
        alert('请填写所有的字段！')
        return
      } else if (this.password !== this.confirm_pwd) {
        alert('两次密码不匹配！')
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
            alert('密码修改成功！')
          } else {
            alert('修改失败，用户不存在！')
          }
        })
    }
  }
}
</script>
