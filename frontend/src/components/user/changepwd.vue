<template>
  <div class="card">
    <div class="title">修改密码</div>
    <div class="space"></div>
    <div class="input-title">旧密码</div>
    <div class="space"></div>
    <el-input type="password" v-model="old_pwd" auto-complete="off" placeholder="请输入旧密码">{{old_pwd}}</el-input>
    <div class="space"></div>
    <div class="input-title">新密码</div>
    <div class="space"></div>
    <el-input type="password" v-model="password" auto-complete="off" placeholder="请输入密码">{{password}}</el-input>
    <div class="space"></div>
    <div class="input-title">确认登陆密码</div>
    <div class="space"></div>
    <el-input type="password" v-model="confirm_pwd" auto-complete="off" placeholder="请输入密码">{{confirm_pwd}}</el-input>
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
        alert('请填写所有的字段！')
        return false
      } else if (this.password !== this.confirm_pwd) {
        alert('两次密码不匹配！')
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
          Tools.get_url() + 'change_manager',
          qs.stringify({
            username: saved.username,
            password: saved.password
          })
        )
        .then(function(response) {
          if (response.data.success) {
            alert('修改管理员密码成功！')
          } else {
            alert('修改密码失败，管理员不存在！')
          }
        })
    }
  }
}
</script>
