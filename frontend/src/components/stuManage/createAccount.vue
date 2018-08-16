<template>
  <div>
    <div label-width = "150px" class = "login-container" >

      <div style="height:30px; font-size: 24px" class="label">随机生成账户</div>

      <br><br>
      <div style="height:30px ; float: left ; color:brown" >产生个数</div>
      <br><br>
      <el-input v-model="number" placeholder="请输入内容"></el-input>

      <br><br>

      <div style="height:30px ; float: left ; color:brown" >等级选择</div>

      <br><br>

      <span v-for="option in options">
        <el-checkbox v-model="option.value" style="width: 33%; border:2px; text-align: left; color:grey">{{"等级"+option.number}}</el-checkbox>
      </span>
      <br><br>

      <el-button style="color:deeppink" @click="submit">立即生成</el-button>

      <br>

    </div>

    <div class = "login-container" >
      <el-table :data="tableData" height="400">
        <el-table-column prop="user_number" width="100px" align="center" label="账户" ></el-table-column>
        <el-table-column prop="user_pwd" align="center" label="密码" ></el-table-column>
      </el-table>
    </div>
  </div>

</template>

<script>
/* eslint-disable camelcase */

import qs from 'qs'
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
    checknum: function (number) {
      for (let i = 0; i < number.length; ++i) {
        if (number[i] > '9' || number[i] < '0') {
          alert('输入的个数非法，请检查')
          return false
        }
      }
      if (parseInt(number) > 10000) {
        alert('输入的个数过大，请检查')
        return false
      } else if (parseInt(number) === 0) {
        alert('个数不能为0！')
        return false
      }
      return true
    },
    submit: function () {
      this.tableData = []
      if (!this.checknum(this.number)) {
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
      axios.post('http://192.168.55.33:8000/create_student', my_values)
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

<style >

  .login-container {
    -webkit-border-radius: 5px;
    border-radius: 5px;
    -moz-border-radius: 5px;
    background-clip: padding-box;
    margin: 50px auto;
    width: 400px;
    padding: 35px 35px 15px 35px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;
  }</style>
