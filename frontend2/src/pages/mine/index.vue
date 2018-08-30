<template>
  <div class="me">
    <div class="my-info">
      <img v-bind:src="image_file_addr">
      <p class="nickname">{{ nickname }}</p>
    </div>
    <button id="modify-info" @click="change_info">修改资料</button>
    <button id="system-message" @click="system_message">系统消息</button>
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
      wx.showModal({
        title: '关于弗恩英语',
        content: '弗恩英语成立于2013年，一直专注于3-18岁青少年语言学习的素质教育。' +
          '截至2018年6月，弗恩英语以全国直营连锁的形式在合肥、南京、杭州等省会城市' +
          '开设了近40所分校。',
        showCancel: false,
        confirmText: '确定',
        confirmColor: '#ffb001'
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
          wx.reLaunch({
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
  width: 75%;
  margin: 60px auto;
}

.my-info {
  margin: 50px auto 30px;
  display: flex;
  flex-wrap: wrap;
}

.nickname {
  color: #ffb001;
  width: 100%;
  text-align: center;
  margin: 20px auto;
  font-size: 22px;
  font-weight: bold;
}

.me button {
  color: #fff;
  font-weight: bold;
}

img {
  width: 80px;
  height: 80px;
  margin: 0 auto;
  border: 3px solid #ffb001;
  border-radius: 10px;
}

#modify-info {
  background-color: #019dd6;
  margin: 20px auto;
}

#system-message {
  background-color: #f67c30;
  margin: 20px auto;
}

#about-vron {
  background-color: #00c544;
  margin: 20px auto;
}

#logout {
  background-color: #f53076;
  margin: 40px auto;
}
</style>
