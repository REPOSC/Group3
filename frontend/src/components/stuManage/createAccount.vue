<template>
  <div>
    <div class="card">
      <div class="title space">随机生成账户</div>
      <div class="input-title space">产生个数</div>
      <el-input v-model="number" placeholder="请输入个数"></el-input>
      <div class="input-title space">等级选择</div>
      <span v-for="option in options">
        <el-checkbox class="checkbox" v-model="option.value">{{"等级"+option.number}}</el-checkbox>
      </span>
      <div class="space">
        <el-button type="primary" @click="submit">立即生成</el-button>
      </div>
    </div>
    <div class="card space">
      <el-table :data="tableData" height="400">
        <el-table-column prop="user_name" width="100px" align="center" label="账户"></el-table-column>
        <el-table-column prop="user_pwd" align="center" label="密码"></el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
/* eslint-disable camelcase */
import * as Tools from '../Tools/Tools'
import axios from 'axios'
export default {
  data: function() {
    return {
      MAX_VALUE: Tools.MAX_VALUE,
      options: [],
      tableData: [],
      number: 1
    }
  },
  created: function() {
    for (let i = 0; i < this.MAX_VALUE; ++i) {
      this.options.push({ value: false, number: String(i + 1) })
    }
  },
  methods: {
    submit: function() {
      if (this.number === '') {
        this.$notify({
          title: '警告',
          message: '请填写产生个数！',
          type: 'warning'
        })
        return
      }
      this.tableData = []
      if (!Tools.checkcount(this.number, this)) {
        return
      }
      let my_values = new URLSearchParams()
      let counter = 0
      my_values.append('number', this.number)
      for (let i = 0; i < this.MAX_VALUE; ++i) {
        if (this.options[i].value) {
          my_values.append('values', i)
          counter++
        }
      }
      if (counter === 0) {
        this.$notify.error({
          title: '错误',
          message: '请选择学生所在的等级！'
        })
        return
      }
      let saved = this
      this.$notify.info({
        title: '请等待',
        message: '正在创建用户，请耐心等候……'
      })
      axios
        .post(Tools.get_url() + 'create_student', my_values)
        .then(function(response) {
          let user_names = eval(response.data.number)
          let user_passwords = eval(response.data.password)
          for (let i = 0; i < user_names.length; ++i) {
            saved.tableData.push({
              user_name: user_names[i],
              user_pwd: user_passwords[i]
            })
          }
          saved.$notify({
            title: '生成用户成功！',
            message: '请注意保存表格中的数据！',
            type: 'success',
            position: 'bottom-right'
          })
        })
    }
  }
}
</script>
