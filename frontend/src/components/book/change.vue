<template>
  <div class="card">
    <div class="title space">修改书籍内容</div>
    <div class="input-title space ">{{text()}}</div>
    <el-switch style="display: inline ; float:left" class="space" v-model="value4" active-color="#13ce66" inactive-color="#ff4949" active-text="按序列号查询" inactive-text="按名称查询">
    </el-switch>
    <el-input type="text" v-model="username" auto-complete="off" placeholder="请输入查询内容">{{username}}</el-input>
    <el-button class="space" type="primary" @click="submit">确认</el-button>
  </div>
</template>
<script>
import * as Tools from '../Tools/Tools'
import axios from 'axios'
import qs from 'qs'
export default {
  data() {
    return {
      value4: true,
      text1: '',
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
    },
    text: function() {
      if (this.value4) {
        return '请输入书目序列号'
      } else return '请输入书目名称'
    }
  }
}
</script>
