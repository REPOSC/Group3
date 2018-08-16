<template>
  <div>
    <div class="card">
      <div class="title">随机生成账户</div>
      <br><br>

      <div class="input-title">产生个数</div>
      <br><br>

      <el-input v-model="number" placeholder="请输入个数"></el-input>
      <br><br>

      <div class="input-title">等级选择</div>
      <br><br>

      <span v-for="option in options">
        <el-checkbox class="checkbox" v-model="option.value">{{"等级"+option.number}}</el-checkbox>
      </span>
      <br><br>

      <el-button type = "primary" @click="submit">立即生成</el-button>
      <br><br>
    </div>

    <div class="card">
      <el-table :data="tableData" height="400">
        <el-table-column prop="user_number" width="100px" align="center" label="账户" ></el-table-column>
        <el-table-column prop="user_pwd" align="center" label="密码" ></el-table-column>
      </el-table>
    </div>
    <br><br>
  </div>
</template>

<script>
/* eslint-disable camelcase */
import * as Tools from '../Tools/Tools'
import axios from 'axios'

export default {
  data: function() {
    return {
      max_value: 12,
      options: [],
      tableData: [],
      number: 1
    }
  },

  created: function () {
    for (let i = 0; i < this.max_value; ++i) {
      this.options.push({value: false, number: String(i + 1)})
    }
  },

  methods: {
    submit: function () {
      this.tableData = []
      if (!Tools.checkcount(this.number)) {
        return
      }

      let my_values = new URLSearchParams()
      my_values.append('number', this.number)
      for (let i = 0; i < this.max_value; ++i) {
        if (this.options[i].value) {
          my_values.append('values', i)
        }
      }

      let saved = this
      axios.post(Tools.get_url() + 'create_student', my_values)
        .then(function(response) {
          let user_numbers = eval(response.data.number)
          let user_passwords = eval(response.data.password)
          for (let i = 0; i < user_numbers.length; ++i) {
            saved.tableData.push({user_number: user_numbers[i], user_pwd: user_passwords[i]})
          }
          alert('生成成功！请注意保存表格中的数据！')
        })
    }
  }
}
</script>
