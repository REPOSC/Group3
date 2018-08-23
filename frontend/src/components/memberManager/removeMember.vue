<template>
  <div class="card">
    <div class="title">删除管理员</div>
    <br><br>
    <div class="input-title">管理员账号</div>
    <br><br>
    <el-input type="text" v-model="username" auto-complete="off" placeholder="请输入账号">{{username}}</el-input>
    <br><br>
    <el-button type="primary" @click="submit">确认删除</el-button>
    <br><br>
  </div>
</template>

<script>
import * as Tools from '../Tools/Tools'
import axios from 'axios'
import qs from 'qs'
export default {
  data() {
    return {
      username: ''
    }
  },
  methods: {
    submit: function() {
      if (!confirm('删除管理员后无法恢复，确认要删除吗？')) {
        return
      }
      let saved = this
      axios
        .post(
          Tools.get_url() + 'del_manager',
          qs.stringify({
            username: saved.username
          })
        )
        .then(function(response) {
          if (response.data.success) {
            alert('删除管理员成功！')
          } else {
            alert('删除失败，管理员不存在！')
          }
        })
    }
  }
}
</script>
