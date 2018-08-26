<template>
  <div class="me">
    <div class="my_info">
      <img v-bind:src="image_file_addr">
      <p class="username">{{ nickname }}</p>
    </div>
    <button id="modify_info" @click="change_info">修改资料</button>
    <button id="notice" @click="turnTo">系统消息</button>
    <button id="introduction" @click="turnTo">功能介绍</button>
    <button id="about_vron" @click="about">关于弗恩英语</button>
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
        },
        fail: function(err) {
          console.log(err)
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
    system_msg() {},
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

<style scoped>
page {
  background-image: url();
}
.me {
  padding-top: 30px;
  margin: 20px 50px;
}
.my_info {
  display: flex;
  text-align: center;
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
#modify_info {
  color: #fff;
  background-color: #019dd6;
  margin-top: 40px;
}
#notice {
  color: #fff;
  background-color: #00c544;
  margin-top: 20px;
}
#introduction {
  color: #fff;
  background-color: #f67c30;
  margin-top: 20px;
}
#about_vron {
  color: #fff;
  background-color: #00fe90;
  margin-top: 20px;
}
#logout {
  color: #fff;
  background-color: #f53076;
  margin-top: 40px;
}
</style>
