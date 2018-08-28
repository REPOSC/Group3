<template>
  <div class="card">
    <div class="title space">修改管理员密码</div>
    <div class="input-title space">管理员账号</div>
    <el-input type="text" v-model="username" auto-complete="off" placeholder="请输入管理员账号">{{username}}</el-input>
    <div class="input-title space">新密码</div>
    <el-input type="password" v-model="password" auto-complete="off" placeholder="请输入密码">{{password}}</el-input>
    <div class="input-title space">确认登陆密码</div>
    <el-input type="password" v-model="confirm_pwd" auto-complete="off" placeholder="请输入密码">{{confirm_pwd}}</el-input>
    <el-button class="space" type="primary" @click="submit">确认修改</el-button>
  </div>
</template>
<script>
import * as Tools from '../Tools/Tools'
import axios from 'axios'
import qs from 'qs'
export default {
  data() {
    return {
      username: '',
      password: '',
      confirm_pwd: ''
    }
  },
  methods: {
    submit: function() {
      if (!confirm('你确认更改密码吗？')) {
        return
      }
      if (
        this.username === '' ||
        this.password === '' ||
        this.confirm_pwd === ''
      ) {
        this.$notify.error({
          title: '错误',
          message: '请填写所有的字段！'
        })
        return
      } else if (this.password !== this.confirm_pwd) {
        this.$notify.error({
          title: '错误',
          message: '两次密码不匹配！'
        })
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
            saved.$notify({
              title: '成功',
              message: '修改管理员密码成功！',
              type: 'success',
              position: 'bottom-right'
            })
          } else {
            saved.$notify.error({
              title: '失败',
              message: '请检查管理员账号是否存在！'
            })
          }
        })
    }
  }
}
</script>
