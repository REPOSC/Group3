<template>
  <div>
    <div class="title">
      <img src="/static/img/rainbow.png">
      <p>阅读拓展</p>
    </div>
    <div>
      <p class="item">课后拓展要求</p>
      <div class="describe">{{ requirement }}</div>
    </div>
    <div>
      <p class="item">打卡内容</p>
      <textarea class="content" v-model="content"></textarea>
    </div>
    <div class="function">
      <button @click="upload">上传作业</button>
      <div>({{has_upload}})</div>
      <button @click="share">打卡分享</button>
    </div>
  </div>
</template>

<script>
import * as Tools from '../../components/Tools'
import qs from 'qs'
export default {
  data() {
    return {
      username: null,
      level: '',
      booknumber: null,
      allfilepaths: [],
      is_punched: false,
      has_upload: 0,
      requirement: '',
      content: ''
    }
  },
  onLoad: function(option) {
    this.username = option.username
    this.booknumber = option.book
  },
  onShow: function() {
    this.init()
  },
  methods: {
    init: function() {
      let save = this
      let fly = Tools.get_fly()
      fly
        .post(
          Tools.get_url() + 'get_punch_info',
          qs.stringify({
            username: save.username,
            booknumber: save.booknumber
          })
        )
        .then(function(response) {
          save.is_punched = response.data.is_punched
          save.requirement = response.data.requirement
        })
    },
    upload: function() {
      if (this.is_punched === true) {
        wx.showToast({
          title: '您已完成打卡，不要再重复上传文件哦~',
          icon: 'none'
        })
      } else if (this.is_punched === 'cannot') {
        wx.showToast({
          title: '本书没有阅读拓展要求，不能上传文件哦~',
          icon: 'none'
        })
      } else {
        let save = this
        wx.showModal({
          title: '请选择上传的文件类型:',
          cancelText: '图片',
          cancelColor: '#3CC51F',
          confirmText: '视频',
          success: function(response) {
            if (response.confirm) {
              save.get_content('video')
            } else {
              save.get_content('picture')
            }
          }
        })
      }
    },
    get_content: function(type) {
      if (type === 'picture') {
        wx.chooseImage({
          success: this.choosesuccess,
          fail: this.choosefail
        })
      } else {
        wx.chooseVideo({
          success: this.choosesuccess,
          fail: this.choosefail
        })
      }
    },
    choosesuccess: function(file) {
      let tempFilePaths = file.tempFilePaths
      let save = this
      for (let i in tempFilePaths) {
        save.allfilepaths.push(tempFilePaths[i])
      }
      wx.showToast({
        title: '上传成功!'
      })
      save.has_upload += tempFilePaths.length
    },
    choosefail: function(response) {
      wx.showToast({
        title: '选择文件失败！',
        icon: 'none'
      })
    },
    share: function() {
      let save = this
      if (save.is_punched) {
        wx.showToast({
          title: '您已完成打卡，不要重复打卡哦~',
          icon: 'none'
        })
      } else if (save.allfilepaths.length === 0) {
        wx.showToast({
          title: '您还未上传文件，请先上传文件再打卡哦~',
          icon: 'none'
        })
      } else {
        wx.uploadFile({
          url: Tools.get_url() + 'upload_homework',
          filePath: save.allfilepaths[0],
          name: 'files',
          formData: {
            username: save.username,
            booknumber: save.booknumber,
            content: save.content
          },
          success: function(response) {
            let answer = response.data
            let jsonanswer = JSON.parse(answer)
            if (jsonanswer.status === 'true') {
              save.is_punched = true
              save.allfilepaths = []
              wx.showModal({
                title: '打卡成功! 是否进入社群页面？',
                success: function(userresponse) {
                  if (userresponse.confirm) {
                    wx.switchTab({
                      url:
                        '../community/main?username=' +
                        save.username +
                        '&level=' +
                        save.level
                    })
                  }
                }
              })
            } else {
              wx.showToast({
                title: '打卡失败，请检查网络！',
                icon: 'none'
              })
            }
          }
        })
      }
    }
  },
  onUnload: function() {
    if (this.allfilepaths.length !== 0) {
      wx.showToast({
        title: '您还未打卡，请注意完成打卡哦~',
        icon: 'none'
      })
    }
  }
}
</script>

<style scoped>
img {
  width: 70px;
  height: 70px;
}
.title {
  height: 70px;
  line-height: 70px;
  text-align: center;
  display: flex;
  justify-content: center;
}
.describe {
  width: 80%;
  height: 100px;
  background-color: #01c758;
  border: 2px solid #27532c;
  border-radius: 10px;
  margin: 10px auto;
}
.content {
  width: 80%;
  height: 150px;
  background-color: #00c6af;
  border: 2px solid #10534b;
  border-radius: 10px;
  margin: 10px auto;
}
p {
  color: yellow;
  font-size: 25px;
  font-weight: bold;
  text-shadow: 2px 2px 3px #000;
}
.item {
  font-size: 20px;
  margin-left: 10%;
}
.function {
  width: 80%;
  display: flex;
  margin: 20px auto;
}
button {
  width: 35%;
  color: #53cce9;
  font-weight: bold;
  text-shadow: 2px 2px 3px #000;
  background-color: #ffb001;
}
</style>
