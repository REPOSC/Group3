<template>
  <div class="card">
    <div class="title space">删除管理员</div>
    <div class="input-title space">管理员账号</div>
    <el-input type="text" v-model="username" auto-complete="off" placeholder="请输入账号">{{username}}</el-input>
    <el-button class="space" type="primary" @click="submit">确认删除</el-button>
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
            saved.$notify({
              title: '成功',
              message: '删除管理员成功！',
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
