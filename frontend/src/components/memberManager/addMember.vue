<template>
  <div>
    <div class="card">
      <div class="title space">添加管理员</div>
      <div class="input-title space">管理员姓名</div>
      <el-input v-model="nickname" placeholder="请输入账户名"></el-input>
      <div class="input-title space">登录密码</div>
      <el-input v-model="password" placeholder="请输入密码" type="password">
      </el-input>
      <div class="input-title space">登录密码</div>
      <el-input
        v-model="confirm_pwd"
        placeholder="请再次输入密码"
        type="password"
      ></el-input>
      <el-button class="space" type="primary" @click="submit">
        确认注册
      </el-button>
    </div>
    <div class="card">
      <el-table :data="tableData" height="100">
        <el-table-column
          prop="user_name"
          width="100px"
          align="center"
          label="账号"
        ></el-table-column>
        <el-table-column prop="user_pwd" align="center" label="密码">
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import * as Tools from '../Tools/Tools.js'
import qs from 'qs'
import axios from 'axios'
export default {
  data() {
    return {
      nickname: '',
      password: '',
      confirm_pwd: '',
      tableData: []
    }
  },
  methods: {
    submit: function() {
      if (
        this.nickname === '' ||
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
          Tools.get_url() + 'add_manager',
          qs.stringify({
            username: saved.nickname,
            password: saved.password
          })
        )
        .then(function(response) {
          saved.tableData = []
          saved.tableData.push({
            user_name: response.data.username,
            user_pwd: response.data.password
          })
          saved.$notify({
            title: '添加管理员成功！',
            message: '请注意保存下方的用户名和密码！',
            position: 'bottom-right'
          })
        })
    }
  }
}
</script>
