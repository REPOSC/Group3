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
      <button @click="tobookshelf">登录</button>
    </form>
  </div>
</template>

<script>

export default {
  data() {
    return {
      username: '10000017',
      password: 'bwCHikKhC5BjPit'
    }
  },
  methods: {
    test: function() {
      console.log(this.username)
      console.log(this.password)
    },
    handlelogin: function() {
      let Fly = require('../../../node_modules/flyio/dist/npm/wx.js')
      let fly = new Fly()
      let save = this
      fly.post('http://192.168.55.33:8082/auth_student', qs.stringify({
        id: save.username,
        password: save.password
      })).then(function(response) {
        if (response.data.status === 'error') {
          wx.showModal({
            content: '账号或密码错误，请重新登录'
          })
        } else {
          wx.redirectTo({
            url: '../level/main'
          })
        }
      })
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
