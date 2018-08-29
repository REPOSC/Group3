<template>
  <div>
    <div>
      <video autoplay loop muted playsinline>
        <source src="./video/movie.mp4" type="video/mp4">
      </video>
    </div>
    <div>
      <el-form
        ref="AccountFrom"
        :model="account"
        :rules="rules"
        label-position="left"
        label-width="0px"
        class="demo-ruleForm login-container"
      >
        <h3 class="title">弗恩英语管理员登录</h3>
        <el-form-item prop="username">
          <el-input
            type="text"
            v-model="account.username"
            auto-complete="off"
            placeholder="账号"
          ></el-input>
        </el-form-item>
        <el-form-item prop="pwd">
          <el-input
            type="password"
            v-model="account.pwd"
            auto-complete="off"
            placeholder="密码"
          ></el-input>
        </el-form-item>
        <el-checkbox v-model="checked" checked class="remember">
          记住密码</el-checkbox>
        <el-button
          type="primary"
          @click.native.prevent="handleLogin"
          :loading="loading"
        >登录</el-button>
      </el-form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import qs from 'qs'
import * as Tools from './Tools/Tools'

export default {
  data() {
    return {
      name: 'login',
      vedioCanPlay: false,
      fixStyle: '',
      loading: false,
      account: {
        username: '100001',
        pwd: '222222'
      },
      rules: {
        username: [{ required: true, message: '请输入账号', trigger: 'blur' }],
        pwd: [{ required: true, message: '请输入密码', trigger: 'blur' }]
      },
      checked: true
    }
  },
  methods: {
    handleLogin: function() {
      let saved = this
      axios
        .post(
          Tools.get_url() + 'auth_manager',
          qs.stringify({
            id: saved.account.username,
            password: saved.account.pwd
          })
        )
        .then(function(response) {
          if (response.data.status === 'error') {
            saved.$notify({
              title: '登录失败',
              message: '用户名或密码错误！',
              type: 'warning'
            })
          } else {
            window.sessionStorage.is_load = 'true'
            window.sessionStorage.username = saved.account.username
            window.sessionStorage.is_superuser = response.data.is_superuser
            saved.$router.push({ path: '/' })
          }
        })
    }
  },
  mounted: function() {}
}
</script>
<style lang="scss" scoped>
.login-container {
  -webkit-border-radius: 5px;
  border-radius: 40px;
  -moz-border-radius: 5px;
  background-clip: padding-box;
  margin: 260px auto;
  width: 500px;
  height: 309px;
  padding: 50px 100px 50px 100px;
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
  );
  background: -webkit-linear-gradient(
    top,
    #ace,
    #00c1de
  );
  background: -o-linear-gradient(top, #ace, #00c1de);

  .title {
    margin: 10px 35px 55px 35px;
    text-align: center;
    color: #505458;
  }

  .remember {
    margin: 40px 35px 35px 0;
  }
}

video {
  position: fixed;
  right: 0;
  bottom: 0;
  min-width: 100%;
  min-height: 100%;
  height: auto;
  width: auto;
  -webkit-filter: grayscale(100%);
  filter: grayscale(100%);
  z-index: -11;
}

source {
  min-width: 100%;
  max-height: 100%;
  height: auto;
  width: 100%;
  display: block;
}
</style>
