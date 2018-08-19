<template>
  <div class='login'>
    <form class='form-control'>
      <div class='card'>
        <p>账号:</p>
        <input type='text' class='input' v-model='username'/>
      </div>
      <div class='card'>
        <p>密码:</p>
        <input type='password' class='input' v-model='password'/>
      </div>
      <button @click='handlelogin'>登录</button>
    </form>
  </div>
</template>

<script>
import qs from 'qs';
import * as Tools from '../../components/Tools.js'
export default {
  data() {
    return {
      username: '10000328',
      password: 'A54t8M65hwBrykS',
      last_level: ""
    };
  },
  methods: {
    handlelogin: function() {
      let fly = Tools.get_fly()
      let save = this;
      fly
        .post(
          Tools.get_url()+'auth_student',
          qs.stringify({
            id: save.username,
            password: save.password
          })
        )
        .then(function(response) {
          if (response.data.status === 'error') {
            wx.showModal({
              content: '账号或密码错误，请重新登录'
            });
          } else {
            save.last_level = response.data.last_level
            wx.redirectTo({
              url: '../level/main?username=' + save.username + '&last_level=' + save.last_level
            });
          }
        });
    }
  }
};
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
  display: inline;
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
