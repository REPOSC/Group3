<template>
  <div class="input">
    <p>欢迎登录</p>
    <p>用户名</p>
    <input type='text' v-model="username" placeholder="请输入您的用户名"/>
    <p>{{ username }}</p>
    <p>密码</p>
    <input type='password' v-model="password" placeholder="请输入您的密码"/>
    <p>{{ password }}</p>
    <a href="/pages/index/main" class="login">登录</a>
  </div>
</template>

<script>

export default {
  data:{
    username:'',
    password:''
  },
  computed: {

  },
  methods: {
    login() {
      console.log(this.username)
      console.log(this.password)
    }
  }
}
</script>

<style>
.input {
  text-align: center;
  margin-top: 100px;
}
.login {
  display: inline-block;
  margin: 100px auto;
  padding: 5px 10px;
  color: blue;
  border: 1px solid blue;
}
</style>
