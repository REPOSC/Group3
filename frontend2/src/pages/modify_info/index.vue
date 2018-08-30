<template>
  <div class="info">
    <p class="change">修改头像</p>
    <div class="div">
      <div class="avatar">
        <img v-bind:src="image_file_addr">
        <div class="image">
          <button @click="choose_image">上传头像</button>
          <button @click="change_image">保存头像</button>
        </div>
      </div>
    </div>
    <p class="change">修改昵称</p>
    <div class="div">
      <div class="item">
        <input v-model="nickname" maxlength="8" placeholder="输入不超过8个字符" />
      </div>
      <button @click="change_nickname">保存昵称</button>
    </div>
    <p class="change">修改密码</p>
    <div class="div">
      <div class="item">
        <input type="password"
          placeholder="原密码"
          v-model="old_password"
          maxlength="15" />
        <input type="password"
          placeholder="新密码"
          v-model="new_password"
          maxlength="15" />
        <input type="password"
          placeholder="确认密码"
          v-model="new_password_again"
          maxlength="15" />
      </div>
      <button @click="change_pwd">保存密码</button>
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
      nickname: '',
      image_file_addr: null,
      old_password: '',
      new_password: '',
      new_password_again: ''
    }
  },
  onLoad: function(status) {
    this.username = status.username
  },
  onShow: function() {
    this.init()
  },
  methods: {
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
    init() {
      this.init_nickname()
      this.init_picture()
    },
    choose_image() {
      let save = this
      wx.chooseImage({
        count: 1,
        success: function(response) {
          save.image_file_addr = response.tempFilePaths[0]
        }
      })
    },
    change_image() {
      let save = this
      wx.uploadFile({
        url: Tools.get_url() + 'change_user_image',
        filePath: save.image_file_addr,
        name: 'image',
        header: {
          'Content-Type': 'multipart/form-data'
        },
        formData: {
          username: save.username
        },
        success: function(response) {
          if (response.statusCode === 200) {
            save.init_picture()
            wx.showToast({
              title: '保存成功！',
              icon: 'success',
              duration: 1500,
              mask: true
            })
          }
        }
      })
    },
    change_nickname() {
      let fly = Tools.get_fly()
      let save = this
      fly
        .post(
          Tools.get_url() + 'change_user_nickname',
          qs.stringify({
            username: save.username,
            nickname: save.nickname
          })
        )
        .then(function(response) {
          if (response.data.success === true) {
            save.init_nickname()
            wx.showToast({
              title: '修改昵称成功！',
              icon: 'success',
              duration: 1500,
              mask: true
            })
          }
        })
    },
    change_pwd() {
      if (this.new_password !== this.new_password_again) {
        wx.showModal({
          title: '密码修改失败',
          showCancel: false,
          content: '两次密码不匹配',
          confirmText: '确定',
          confirmColor: '#ffb001'
        })
        return
      }
      let fly = Tools.get_fly()
      let save = this
      fly
        .post(
          Tools.get_url() + 'change_user_password',
          qs.stringify({
            username: save.username,
            old_password: save.old_password,
            new_password: save.new_password
          })
        )
        .then(function(response) {
          if (response.data.success === 'true') {
            wx.showToast({
              title: '修改成功！',
              icon: 'success',
              duration: 1500,
              mask: true
            })
          } else {
            wx.showModal({
              title: '密码修改失败',
              showCancel: false,
              content: '旧密码不正确',
              confirmText: '确定',
              confirmColor: '#ffb001'
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

button {
  color: #fff;
  width: 50%;
  height: 30px;
  line-height: 30px;
  margin: 15px auto;
  border-radius: 10px;
  background-color: #ffb001;
}

.change {
  width: 40%;
  color: #00c544;
  font-weight: bold;
  margin-bottom: 0;
}

input {
  width: 70%;
  color: #ffb001;
  font-weight: bolder;
  height: 30px;
  line-height: 30px;
  padding-left: 5px;
  border: 4px solid #53cce9;
  margin: 5px auto;
  border-radius: 10px;
}

img {
  width: 90px;
  height: 90px;
  margin-left: 25px;
  border: 4px solid #ffb001;
  border-radius: 10px;
}

.info {
  font-size: 20px;
  color: #fff;
  margin: 10px 20px;
}

.image {
  width: 50%;
  display: flex;
  flex-wrap: wrap;
  height: 94px;
  line-height: 94px;
}

.image button {
  height: 30px;
  line-height: 30px;
  width: 75%;
  margin: 10px auto;
}

.div {
  width: 99%;
  margin: 5px auto;
  border: 4px solid #ffb001;
  border-radius: 10px;
}

.item {
  border-radius: 10px;
  display: flex;
  flex-wrap: wrap;
  margin: 10px auto;
}

.title {
  width: 40%;
  height: 30px;
  line-height: 30px;
  text-align: center;
  margin: 5% auto;
  padding-left: 10px;
  background-color: #ffb001;
  border-radius: 8px;
}

.avatar {
  width: 98%;
  height: 100px;
  line-height: 100px;
  margin: 10px auto;
  display: flex;
  padding-left: 20px;
}
</style>
