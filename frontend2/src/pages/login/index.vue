<template>
  <div class="login">
    <form class="form-control">
      <div class="card">
      <p>用户名:</p>
      <input type='text' class="input"/>
      <p>{{ username }}</p>
      </div>
      <div class="card">
      <p>密码:</p>
      <input type='password' class="input"/>
      <p>{{ password }}</p>
      </div>
      <a href="/pages/level/main">登录</a>
    </form>
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
a {
  padding: 10px 28px;
  margin-bottom: 30px，40px;
  background-color: #e7e7e7;
  color: black;
  border: none;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
}
.card {
  display:inline;
}
.input {
  display: block;
  padding: 0 12px;
  margin-bottom: 5px;
  border: 1px solid #ccc;
}
.form-control {
  display: block;
  padding: 150px 12px;
  margin-bottom: 5px;
}
.login {
  display: block;
  padding: 0px 20px;
  margin-bottom: 5px;
}
</style>
