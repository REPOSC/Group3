<template>
  <div class="card">
    <div class="title">修改账户等级</div>
    <div class="space"></div>
    <div class="input-title">会员账号</div>
    <div class="space"></div>
    <el-input type="text" v-model="username" auto-complete="off" placeholder="请输入您的账号">{{username}}</el-input>
    <div class="space"></div>
    <div class="input-title">等级选择</div>
    <div class="space"></div>
    <span v-for="option in options">
      <el-checkbox v-model="option.value" class="checkbox">{{"等级"+option.number}}</el-checkbox>
    </span>
    <div class="space"></div>
    <el-button type="primary" @click="submit">确认修改</el-button>
    <div class="space"></div>
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
      let my_values = new URLSearchParams()
      my_values.append('username', this.username)
      for (let i = 0; i < this.max_value; ++i) {
        if (this.options[i].value) {
          my_values.append('values', i)
        }
      }
      axios
        .post(Tools.get_url() + 'set_level', my_values)
        .then(function(response) {
          if (response.data.success) {
            alert('等级设置成功！')
          } else {
            alert('设置失败，用户不存在！')
          }
        })
    }
  }
}
</script>
