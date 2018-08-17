<template>
  <div>
    <div class="card">
      <div class="title">添加管理员</div>
      <br><br>
      <div class="input-title">管理员姓名</div>
      <br><br>
      <el-input v-model="username" placeholder="请输入账户名"></el-input>
      <br><br>
      <div class="input-title">登录密码</div>
      <br><br>
      <el-input v-model="password" placeholder="请输入密码" type="password"></el-input>
      <br><br>
      <div class="input-title">登录密码</div>
      <br><br>
      <el-input v-model="confirm_pwd" placeholder="请再次输入密码" type="password"></el-input>
      <br><br>
      <el-button type = "primary" @click="submit" >确认注册</el-button>
      <br><br>
    </div>
    <div class="card">
      <el-table :data="tableData" height="100">
        <el-table-column prop="user_number" width="100px" align="center" label="账号" ></el-table-column>
        <el-table-column prop="user_pwd" align="center" label="密码" ></el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
import * as Tools from "../Tools/Tools.js";
import qs from "qs";
import axios from "axios";
export default {
  data() {
    return {
      username: "",
      password: "",
      confirm_pwd: "",
      tableData: []
    };
  },
  methods: {
    submit: function() {
      if (
        this.username === "" ||
        this.password === "" ||
        this.confirm_pwd === ""
      ) {
        alert("请填写所有的字段！");
        return;
      } else if (this.password !== this.confirm_pwd) {
        alert("两次密码不匹配！");
        return;
      }
      let saved = this;
      axios
        .post(
          Tools.get_url() + "add_manager",
          qs.stringify({
            username: saved.username,
            password: saved.password
          })
        )
        .then(function(response) {
          saved.tableData = [];
          saved.tableData.push({
            user_number: response.data.username,
            user_pwd: response.data.password
          });
          saved.$notify({
            title: "添加管理员成功！",
            message: "请注意保存下方的用户名和密码！",
            position: "bottom-right"
          });
        });
    }
  }
};
</script>
