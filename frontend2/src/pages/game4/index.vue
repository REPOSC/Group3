<template>
  <div class="game">
    <div class="center">
      <i-icon type="systemprompt_fill" @click="play_sound" size="40" />
    </div>
    <div class="picGroup">
      <img :key="pic.index" v-for="pic in pics" :isanswer="pic.isanswer" :src="pic.src" mode="aspectFit" @click="choice(pic)" />
    </div>
    <div v-bind:class="word_class">
      {{word}}
    </div>
  </div>
</template>

<script>
import * as Tools from '../../components/Tools.js'
import qs from 'qs'
export default {
  data() {
    return {
      innerAudioContext: null,
      word_class: null,
      booknumber: null,
      word: null,
      pics: []
    }
  },
  onLoad: function(status) {
    this.booknumber = status.booknumber
  },
  onShow: function() {
    this.init()
  },
  methods: {
    init() {
      this.word_class = 'hidden'
      this.innerAudioContext = wx.createInnerAudioContext()
      this.pics = []
      for (let i = 0; i < 4; ++i) {
        this.pics.push({
          isanswer: null,
          src: null,
          index: i
        })
      }
      let fly = Tools.get_fly()
      let save = this
      fly
        .post(
          Tools.get_url() + 'get_fourth_game_text',
          qs.stringify({
            book_id: this.booknumber
          })
        )
        .then(function(response) {
          save.word = response.data.text
        })
      let requests = [
        { status: true, number: -1 },
        { status: false, number: 1 },
        { status: false, number: 2 },
        { status: false, number: 3 }
      ]
      let random_list = Tools.generate_random_list(4)
      for (let i = 0; i < 4; ++i) {
        wx.downloadFile({
          url:
            Tools.get_url() +
            'get_fourth_game_image?book_id=' +
            save.booknumber +
            '&status=' +
            requests[random_list[i]].status +
            '&number=' +
            requests[random_list[i]].number,
          success: function(picture_response) {
            let pic_tmp_obj = save.pics[i]
            pic_tmp_obj.src = picture_response.tempFilePath
            pic_tmp_obj.isanswer = requests[random_list[i]].status
            save.$set(save.pics, i, pic_tmp_obj)
          }
        })
      }
    },
    play_sound() {
      let save = this
      wx.downloadFile({
        url:
          Tools.get_url() + 'get_fourth_game_audio?book_id=' + save.booknumber,
        success: function(audio_response) {
          if (audio_response.statusCode === 200) {
            save.innerAudioContext.src = audio_response.tempFilePath
            save.innerAudioContext.play()
          }
        }
      })
    },
    choice(pic) {
      if (pic.isanswer === true) {
        this.word_class = 'center'
        wx.showModal({
          title: '选对啦!宝宝真棒！',
          content: '已完成该练习，是否退出~',
          cancelText: '再看看',
          confirmText: '退出',
          confirmColor: '#ffb001',
          success: function(response) {
            if (response.confirm) {
              wx.navigateBack({
                url: '../practice/main'
              })
            }
          }
        })
      } else {
        wx.showModal({
          title: '啊噢，就差一点点噢...',
          content: '再试一次吧~',
          cancelText: '不了',
          confirmText: '再试一次',
          confirmColor: '#ffb001',
          success: function(response) {
            if (response.cancel) {
              wx.navigateBack({
                url: '../practice/main'
              })
            }
          }
        })
      }
    }
  }
}
</script>

<style>
page {
  background-size: 100% 100%;
}
.game {
  margin-top: 30px;
}
.picGroup {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  margin: 20px;
}
.picGroup img {
  width: 40%;
  height: 100px;
  margin: 10px auto;
  overflow: hidden;
  border: 5px solid #ffb001;
  padding: 5px;
  background-color: white;
  border-radius: 10%;
}
.center {
  margin: 50px auto;
  text-align: center;
  font-size: 40px;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
    Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
.hidden {
  display: none;
}
</style>
