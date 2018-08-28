<template>
  <div class="card">
    <div class="title space">修改账户等级</div>
    <div class="input-title space">会员账号</div>
    <el-input type="text" v-model="username" auto-complete="off" placeholder="请输入您的账号">{{username}}</el-input>
    <div class="input-title space">等级选择</div>
    <span v-for="option in options">
      <el-checkbox v-model="option.value" class="checkbox">{{"等级"+option.number}}</el-checkbox>
    </span>
    <el-button class="space" type="primary" @click="submit">确认修改</el-button>
  </div>
</template>
<script>
import * as Tools from '../Tools/Tools.js'
import axios from 'axios'
export default {
  data() {
    return {
      max_value: 12,
      options: [],
      username: ''
    }
  },
  created: function() {
    for (let i = 0; i < this.max_value; ++i) {
      this.options.push({ value: false, number: String(i + 1) })
    }
  },
  methods: {
    submit: function() {
      if (this.username === '') {
        this.$notify({
          title: '警告',
          message: '请填写会员账号！',
          type: 'warning'
        })
        return
      }
      let my_values = new URLSearchParams()
      let save = this
      my_values.append('username', this.username)
      let count = 0
      for (let i = 0; i < this.max_value; ++i) {
        if (this.options[i].value) {
          my_values.append('values', i)
          count++
        }
      }
      if (count === 0) {
        this.$notify.error({
          title: '错误',
          message: '请至少选择一个等级！'
        })
        return
      }
      axios
        .post(Tools.get_url() + 'set_level', my_values)
        .then(function(response) {
          if (response.data.success) {
            save.$notify({
              title: '成功',
              message: '设置等级成功！',
              type: 'success',
              position: 'bottom-right'
            })
          } else {
            save.$notify({
              title: '警告',
              message: '设置失败,用户不存在!',
              type: 'warning'
            })
          }
        })
    }
  }
}
</script>
