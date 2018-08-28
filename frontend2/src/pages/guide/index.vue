<template>
  <div class="guide">
    <title v-bind="video_function" @play_video="play_video"></title>
    <div class="firstpart">
      <img src="https://daisy-donald.cn/image/yellow-tap.png">
      <h1>本书导读</h1>
      <p :key="index" v-for="(one,index) in ones">{{ index-0+1 }}、{{ one }}</p>
    </div>
    <div class="secpart">
      <img src="https://daisy-donald.cn/image/green-tap.png">
      <h1>本课重点知识</h1>
      <p :key="index" v-for="(two,index) in twos">{{ index-0+1 }}、{{ two }}</p>
    </div>
    <div class="thirdpart">
      <div class="subtitle">
        <img src="https://daisy-donald.cn/image/red-tap.png">
        <h1>词汇表与配音讲解</h1>
      </div>
      <div :key="index" v-for="(three,index) in threes">
        <div class="word">{{ index-0+1 }}、{{ three }}</div>
        <i-icon type="customerservice_fill"
          size="28"
          class="word"
          @click="hear(index)" />
      </div>
    </div>
  </div>
</template>

<script>
import * as Tools from '../../components/Tools.js'
import qs from 'qs'
import title from '../../components/title'

export default {
  data() {
    return {
      video_function: {
        play_info: '功能讲解',
        is_play_video: false,
        src: 'http://wxsnsdy.tc.qq.com/105/20210/snsdyvideodownload?filekey=30280201010421301f0201690402534804102ca905ce620b1241b726bc41dcff44e00204012882540400&bizid=1023&hy=SH&fileparam=302c020101042530230204136ffd93020457e3c4ff02024ef202031e8d7f02030f42400204045a320a0201000400',
        booktitle: 'BOOK1'
      },
      booknumber: 0,
      ones: [],
      twos: [],
      threes: [],
      current_audio: null,
      innerAudioContext: null
    }
  },
  components: {
    title
  },
  onLoad: function(status) {
    this.booknumber = status.booknumber
    this.video_function.booktitle = status.bookname
  },
  onShow: function() {
    this.init()
  },
  methods: {
    init: function() {
      let fly = Tools.get_fly()
      let save = this
      fly
        .post(
          Tools.get_url() + 'get_first_function',
          qs.stringify({
            book_id: save.booknumber
          })
        )
        .then(function(response) {
          let knowledges = response.data.knowledge
          let guides = response.data.guide
          let word_contents = response.data.words
          save.ones = guides
          save.twos = knowledges
          save.threes = word_contents
        })
      this.innerAudioContext = wx.createInnerAudioContext()
    },
    hear: function(index) {
      let save = this
      wx.downloadFile({
        url:
          Tools.get_url() +
          'get_word_audio?book_id=' +
          this.booknumber +
          '&audio_index=' +
          index,
        success: function(res) {
          if (res.statusCode === 200) {
            save.innerAudioContext.src = res.tempFilePath
            save.innerAudioContext.play()
          }
        }
      })
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
  }
}
</script>

<style>
page {
  background-size: 100% 100%;
  background-image: url('https://daisy-donald.cn/image/sky.jpg');
}
.guide {
  margin: 10px 10px;
}
title {
  height: 70px;
}
/* .title {
  height: 70px;
  line-height: 70px;
  text-align: center;
  display: flex;
  justify-content: center;
}
.title p {
  color: yellow;
  font-size: 25px;
  font-weight: bold;
  text-shadow: 2px 2px 3px #000;
}
.title img {
  width: 70px;
  height: 70px;
}
.title button {
  position: absolute;
  color: white;
  font-size: 10px;
  font-weight: bolder;
  line-height: 20px;
  height: 20px;
  right: 10px;
  background-color: #ffb100;
}
.video {
  text-align: center;
} */
.firstpart {
  color: #019dd6;
  align-content: center;
  margin: 30px;
  margin-top: 0px;
}
.secpart {
  color: #02c45d;
  align-content: center;
  margin: 30px;
}
.thirdpart {
  color: #de6648;
  align-content: center;
  margin: 30px;
}
.subtitle {
  display: block;
}
h1 {
  display: inline;
  font-size: 22px;
  font-weight: bolder;
  font-family: fantasy;
}
p {
  display: block;
  margin-right: 15px;
  font-size: 16px;
  font-weight: bold;
}
img {
  width: 30px;
  height: 30px;
}
.thirdpart p {
  display: inline-block;
  font-size: 20px;
  font-weight: bold;
  margin-right: 50px;
  margin-bottom: 10px;
}
.word {
  display: inline;
}
</style>
