<template>
  <el-form ref="AccountFrom" :model="account" :rules="rules" label-position="left" label-width="0px"
           class="demo-ruleForm login-container">
    <h3 class="title">管理员登录</h3>
    <el-form-item prop="username">
    <el-input type="text" v-model="account.username" auto-complete="off" placeholder="账号"></el-input>
    </el-form-item>
    <el-form-item prop="pwd">
    <el-input type="password" v-model="account.pwd" auto-complete="off" placeholder="密码"></el-input>
    </el-form-item>
    <el-checkbox v-model="checked" checked class="remember">记住密码</el-checkbox>
    <el-button type="primary" @click.native.prevent="handleLogin" :loading="loading">登录</el-button>
  </el-form>
</template>

<script>
import axios from "axios";
import qs from "qs";
export default {
  data() {
    return {
      loading: false,
      account: {
        username: "123",
        pwd: "123456"
      },
      rules: {
        username: [{ required: true, message: "请输入账号", trigger: "blur" }],
        pwd: [{ required: true, message: "请输入密码", trigger: "blur" }]
      },
      checked: true
    };
  },
  methods: {
    handleLogin: function() {
      let saved = this;
      axios
        .post(
          "http://192.168.55.33:8000/auth_manager",
          qs.stringify({
            id: saved.account.username,
            password: saved.account.pwd
          })
        )
        .then(function(response) {
          if (response.data.status === "error") {
            alert("登录失败，用户名或密码错误。");
          } else {
            saved.$router.push({ path: "/" });
          }
        });
    }
  }
};
</script>
<style lang="scss" scoped>
.login-container {
  /*box-shadow: 0 0px 8px 0 rgba(0, 0, 0, 0.06), 0 1px 0px 0 rgba(0, 0, 0, 0.02);*/
  -webkit-border-radius: 5px;
  border-radius: 5px;
  -moz-border-radius: 5px;
  background-clip: padding-box;
  margin: 160px auto;
  width: 350px;
  padding: 35px 35px 15px 35px;
  background: #fff;
  border: 1px solid #eaeaea;
  box-shadow: 0 0 25px #cac6c6;
  background: -ms-linear-gradient(top, #ace, #00c1de); /* IE 10 */
  background: -moz-linear-gradient(top, #ace, #00c1de); /*火狐*/
  background: -webkit-gradient(
    linear,
    0% 0%,
    0% 100%,
    from(#ace),
    to(#00c1de)
  ); /*谷歌*/
  background: -webkit-linear-gradient(
    top,
    #ace,
    #00c1de
  ); /*Safari5.1 Chrome 10+*/
  background: -o-linear-gradient(top, #ace, #00c1de); /*Opera 11.10+*/
  .title {
    margin: 0 auto 40px auto;
    text-align: center;
    color: #505458;
  }
  .remember {
    margin: 0 0 35px 0;
  }
}
</style>
