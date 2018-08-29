<template>
  <div>
    <img src="https://daisy-donald.cn/image/lion.png" mode="aspectFit" />
    <div class="login">
      <div class="card">
        <input type="text" placeholder="账号" v-model="username" />
      </div>
      <div class="card">
        <input type="password" placeholder="密码" v-model="password" />
      </div>
      <button @click="handle_login">登录</button>
    </div>
  </div>
</template>

<script>
import qs from 'qs'
import * as Tools from '../../components/Tools.js'
export default {
  data() {
    return {
      username: '10000001',
      password: '111111',
      last_level: ''
    }
  },
  methods: {
    handle_login: function() {
      let fly = Tools.get_fly()
      let save = this
      fly
        .post(
          Tools.get_url() + 'auth_student',
          qs.stringify({
            id: save.username,
            password: save.password
          })
        )
        .then(function(response) {
          if (response.data.status === 'error') {
            wx.showModal({
              content: '账号或密码错误，请重新输入',
              showCancel: false
            })
          } else {
            save.last_level = response.data.last_level
            wx.redirectTo({
              url:
                '../level/main?username=' +
                save.username +
                '&last_level=' +
                save.last_level
            })
          }
        })
    }
  }
}
</script>

<style>
page {
  background-size: 100% 100%;
  background-image: url('https://daisy-donald.cn/image/sky.jpg');
}

.login {
  font-size: 25px;
  margin: 30px auto;
}

.card {
  width: 80%;
  height: 30px;
  line-height: 30px;
  margin: 50px auto;
  display: flex;
  justify-content: space-around;
}

input {
  height: 50px;
  line-height: 50px;
  padding: 0 10px;
  border: 4px solid #ffb001;
  border-radius: 10px;
}

button {
  width: 80%;
  height: 50px;
  line-height: 50px;
  color: #fff;
  background-color: #ffb001;
  margin: 100px auto;
}

img {
  width: 100%;
  height: 200px;
  margin: 0 auto;
}
</style>
