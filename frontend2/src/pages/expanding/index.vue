<template>
  <div class="expanding">
    <title v-bind="video_function" @play_video="play_video"></title>
    <div>
      <p class="item">课后拓展要求</p>
      <div class="describe">{{ requirement }}</div>
    </div>
    <div>
      <p class="item">打卡感想</p>
      <textarea class="content" v-model="content"></textarea>
    </div>
    <div class="function">
      <button @click="uploadhomework">上传作业</button>
      <button @click="share">打卡分享</button>
      <button @click="reset">清除打卡</button>
    </div>
  </div>
</template>

<script>
import * as Tools from '../../components/Tools'
import qs from 'qs'
import title from '../../components/title'

export default {
  data() {
    return {
      video_function: {
        play_info: '功能讲解',
        is_play_video: false,
        src: 'http://wxsnsdy.tc.qq.com/105/20210/snsdyvideodownload?' +
          'filekey=30280201010421301f0201690402534804102ca905ce620b1' +
          '241b726bc41dcff44e00204012882540400&bizid=1023&hy=SH&file' +
          'param=302c020101042530230204136ffd93020457e3c4ff02024ef20' +
          '2031e8d7f02030f42400204045a320a0201000400',
        booktitle: 'BOOK1'
      },
      username: '',
      level: 0,
      booknumber: '',
      allfilepaths: [],
      is_punched: false,
      has_upload: 0,
      requirement: '',
      content: ''
    }
  },
  components: {
    title
  },
  onLoad: function(option) {
    this.username = option.username
    this.booknumber = option.book
    this.level = option.level
    this.video_function.booktitle = option.booktitle
  },
  onShow: function() {
    this.init()
  },
  methods: {
    init: function() {
      let save = this
      let fly = Tools.get_fly()
      wx.downloadFile({
        url: Tools.get_url() + 'get_video?item=expanding',
        success: function(video_response) {
          if (video_response.statusCode === 200) {
            save.video_function.src = video_response.tempFilePath
          }
        }
      })
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
          save.content = response.data.content
        })
    },
    uploadhomework: function() {
      if (this.is_punched === true) {
        this.failtoast('您已完成打卡，不要再重复上传文件哦~')
      } else if (this.is_punched === 'cannot') {
        this.failtoast('本书暂时没有阅读拓展要求，不能上传文件哦~')
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
      save.successtoast('上传成功！')
      save.has_upload += tempFilePaths.length
    },
    choosefail: function(response) {
      this.failtoast('选择文件失败！')
    },
    share: function() {
      let save = this
      let allfilenumber = save.allfilepaths.length
      if (save.is_punched) {
        save.failtoast('您已完成打卡，不要重复打卡哦~')
      } else if (save.has_upload === 0) {
        save.failtoast('您还未上传文件，请先上传文件再打卡哦~')
      } else {
        let status = save.shareupload(save, allfilenumber, 0)
        if (status) {
          save.is_punched = true
          save.has_upload = 0
          save.gotocommunity(save)
        } else {
          save.failtoast('打卡失败，请检查网络链接~')
          let fly = Tools.get_fly()
          fly
            .post(
              Tools.get_url() + 'punch_reset',
              qs.stringify({
                username: save.username,
                booknumber: save.booknumber
              })
            )
            .then(function(response) {
              save.is_punched = false
              save.has_upload = 0
              save.allfilepaths = []
              save.content = ''
            })
        }
      }
    },
    shareupload(save, total, index) {
      if (index < total) {
        let status = true
        wx.uploadFile({
          url: Tools.get_url() + 'upload_homework',
          filePath: save.allfilepaths[index],
          name: 'file',
          formData: {
            username: save.username,
            booknumber: save.booknumber,
            content: save.content
          },
          success: function(response) {
            let answer = response.data
            let jsonanswer = JSON.parse(answer)
            if (jsonanswer.status !== 'true') {
              status = false
              return status
            } else {
              return save.shareupload(save, total, index + 1)
            }
          }
        })
      }
      return true
    },
    gotocommunity: function(save) {
      wx.showModal({
        title: '打卡成功! 是否进入社群页面？',
        success: function(userresponse) {
          if (userresponse.confirm) {
            wx.navigateTo({
              url:
                '../community/main?username=' +
                save.username +
                '&level=' +
                save.level
            })
          }
        }
      })
    },
    failtoast: function(innertext) {
      wx.showToast({
        title: innertext,
        icon: 'none'
      })
    },
    successtoast: function(innertext) {
      wx.showToast({
        title: innertext
      })
    },
    reset: function() {
      let save = this
      let fly = Tools.get_fly()
      if (!save.is_punched) {
        save.failtoast('您还未完成打卡~')
      } else {
        wx.showModal({
          title: '是否要重置打卡记录？',
          confirmText: '重置',
          cancelText: '取消',
          success: function(response) {
            if (response.confirm) {
              fly
                .post(
                  Tools.get_url() + 'punch_reset',
                  qs.stringify({
                    username: save.username,
                    booknumber: save.booknumber
                  })
                )
                .then(function(response) {
                  if (response.data.status) {
                    save.is_punched = false
                    save.has_upload = 0
                    save.allfilepaths = []
                    save.content = ''
                    save.successtoast('重置成功！')
                  } else {
                    save.failtoast('重置失败！')
                  }
                })
            }
          }
        })
      }
    },
    play_video() {
      if (!this.video_function.is_play_video) {
        this.video_function.is_play_video = true
        this.video_function.play_info = '关闭'
      } else {
        this.video_function.is_play_video = false
        this.video_function.play_info = '功能讲解'
      }
    }
  },
  onUnload: function() {
    if (this.has_upload !== 0) {
      this.failtoast('您还未打卡，请注意完成打卡哦~')
    }
  }
}
</script>

<style>
page {
  background-size: 100% 100%;
  background-image: url('https://daisy-donald.cn/image/sky.jpg');
}

.expanding {
  margin: 10px 10px;
}

title {
  height: 70px;
}

img {
  width: 70px;
  height: 70px;
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
  margin-top: 15%;
  width: 30%;
  color: #53cce9;
  font-weight: bold;
  font-size: 14px;
  text-shadow: 2px 2px 3px #000;
  background-color: #ffb001;
}
</style>
