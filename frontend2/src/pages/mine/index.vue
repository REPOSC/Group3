<template>
  <div class="me">
    <div class="my-info">
      <img v-bind:src="image_file_addr">
      <p class="username">{{ nickname }}</p>
    </div>
    <button id="modify-info" @click="change_info">修改资料</button>
    <button id="system-message" @click="system_message">系统消息</button>
    <button id="introduction" @click="introduce">功能介绍</button>
    <button id="about-vron" @click="about">关于弗恩英语</button>
    <button id="logout" @click="logout">退出登录</button>
  </div>
</template>

<script>
import * as Tools from '../../components/Tools.js'
import qs from 'qs'
export default {
  data() {
    return {
      username: null,
      nickname: null,
      image_file_addr: null
    }
  },
  onLoad(status) {
    this.username = status.username
  },
  onShow() {
    this.init()
  },
  methods: {
    init_nickname() {
      let fly = Tools.get_fly()
      let save = this
      fly
        .post(
          Tools.get_url() + 'get_user_nickname',
          qs.stringify({
            username: save.username
          })
        )
        .then(function(response) {
          save.nickname = response.data.nickname
        })
    },
    init_picture() {
      let save = this
      wx.downloadFile({
        url: Tools.get_url() + 'get_user_image?username=' + save.username,
        success: function(picture_response) {
          if (picture_response.statusCode === 200) {
            save.image_file_addr = picture_response.tempFilePath
          }
        }
      })
    },
    init() {
      this.init_nickname()
      this.init_picture()
    },
    change_info() {
      wx.navigateTo({
        url: '../modify_info/main?username=' + this.username
      })
    },
    system_message() {
      wx.navigateTo({
        url: '../system_message/main?username=' + this.username
      })
    },
    about() {
      wx.showToast({
        title: 'By Windows Vista',
        icon: 'none',
        duration: 1500,
        mask: true
      })
    },
    logout() {
      let fly = Tools.get_fly()
      let save = this
      fly
        .post(
          Tools.get_url() + 'log_out',
          qs.stringify({
            username: save.username
          })
        )
        .then(function(response) {
          wx.redirectTo({
            url: '../login/main'
          })
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

.me {
  padding-top: 30px;
  margin: 20px 50px;
}

.my-info {
  display: flex;
  text-align: center;
}

.username {
  color: #ffb001;
  font-size: 25px;
}

img {
  width: 70px;
  height: 70px;
  margin-left: 20px;
  border: 3px solid #ffb001;
  border-radius: 10px;
}

p {
  margin: 25px 40px;
  font-weight: bold;
}

#modify-info {
  color: #fff;
  font-weight: bold;
  background-color: #019dd6;
  margin-top: 40px;
}

#system-message {
  color: #fff;
  font-weight: bold;
  background-color: #00c544;
  margin-top: 20px;
}

#introduction {
  color: #fff;
  font-weight: bold;
  background-color: #f67c30;
  margin-top: 20px;
}

#about-vron {
  color: #fff;
  font-weight: bold;
  background-color: #00fe90;
  margin-top: 20px;
}

#logout {
  color: #fff;
  font-weight: bold;
  background-color: #f53076;
  margin-top: 40px;
}
</style>
