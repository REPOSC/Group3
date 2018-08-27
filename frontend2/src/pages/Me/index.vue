<template>
  <div class="me">
    <div class="my_info">
      <img v-bind:src="image_file_addr">
      <p class="username">{{ nickname }}</p>
    </div>
    <div class="function">
      <button id="modify_info" @click="change_info">修改资料</button>
      <button id="select_level" @click="select_level">选择等级</button>
      <button id="notice" @click="turnTo">系统消息</button>
      <button id="introduction" @click="turnTo">功能介绍</button>
      <button id="about_vron" @click="about">关于弗恩英语</button>
      <button id="logout" @click="logout">退出登录</button>
    </div>
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

<style>
page {
  background-size: 100% 100%;
  background-image: url('https://daisy-donald.cn/image/back.jpg');
}
.me {
  font-weight: bold;
}
.my_info {
  width: 60%;
  height: 120px;
  margin: 20px auto;
  display: flex;
  flex-wrap: wrap;
  text-align: center;
}
img {
  margin: 2px auto;
  width: 70px;
  height: 70px;
  border: 3px solid #ffb001;
  border-radius: 10px;
}
p {
  height: 40px;
  line-height: 40px;
  width: 100%;
}
button {
  color: #fff;
  width: 75%;
  height: 50px;
  line-height: 50px;
  font-size: 20px;
  margin: 20px auto;
}
#modify_info {
  background-color: #019dd6;
}
#select_level {
  background-color: #f67c30;
}
#notice {
  background-color: #00c544;
}
#introduction {
  background-color: #f67c30;
}
#about_vron {
  background-color: #00fe90;
}
#logout {
  background-color: #f53076;
  margin: 50px auto;
}
</style>
