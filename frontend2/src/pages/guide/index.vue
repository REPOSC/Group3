<template>
  <div class="guide">
    <loading :hidden="hidden">
      加载中...
    </loading>
    <title v-bind="video_function" @play_video="play_video"></title>
    <div class="firstpart">
      <div class="explain">
        <img src="https://daisy-donald.cn/image/yellow-tap.png">
        <p class="subtitle">本书导读</p>
      </div>
      <p class="content" :key="index" v-for="(one,index) in ones">
        {{ index-0+1 }}、{{ one }}
      </p>
    </div>
    <div class="secpart">
      <div class="explain">
        <img src="https://daisy-donald.cn/image/green-tap.png">
        <p class="subtitle">本课重点知识</p>
      </div>
      <p class="content" :key="index" v-for="(two,index) in twos">
        {{ index-0+1 }}、{{ two }}
      </p>
    </div>
    <div class="thirdpart">
      <div class="explain">
        <img src="https://daisy-donald.cn/image/red-tap.png">
        <p class="subtitle">词汇表与配音讲解</p>
      </div>
      <div id="word" :class="is_play_audio[index]" :key="index" v-for="(three,
      index) in threes">
        <div>{{ index-0+1 }}、{{ three }}</div>
        <i-icon type="customerservice_fill" size="30" @click="hear
        (index)" />
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
        src: null,
        booktitle: 'BOOK1'
      },
      hidden: true,
      booknumber: 0,
      ones: [],
      twos: [],
      threes: [],
      current_audio: null,
      innerAudioContext: null,
      is_play_audio: [],
      now_audio_index: '',
      length: 0
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
          save.length = response.data.wordslen
          save.ones = guides
          save.twos = knowledges
          save.threes = word_contents
          for (let i = 0; i < save.length; i++) {
            save.is_play_audio[i] = 'notplay'
          }
        })
      this.innerAudioContext = wx.createInnerAudioContext()
    },
    set_play_status(save, index) {
      if (save.now_audio_index !== '') {
        save.is_play_audio[save.now_audio_index] = 'notplay'
      }
      save.now_audio_index = index
      save.is_play_audio[index] = 'isplay'
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
            save.set_play_status(save, index)
            save.innerAudioContext.play()
          }
        }
      })
    },
    play_video() {
      if (!this.video_function.is_play_video) {
        this.video_function.is_play_video = true
        this.video_function.play_info = '关闭'
        this.hidden = false
        let save = this
        wx.downloadFile({
          url: Tools.get_url() + 'get_video?item=guide',
          success: function(video_response) {
            if (video_response.statusCode === 200) {
              save.video_function.src = video_response.tempFilePath
            }
            save.hidden = true
          }
        })
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

.firstpart {
  color: #019dd6;
  align-content: center;
  margin: 30px;
  margin-top: 0;
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

.explain {
  display: block;
  margin: 15px auto;
}

.explain p {
  display: inline;
  font-size: 24px;
  font-weight: bolder;
  font-family: fantasy;
}

p {
  display: inline-block;
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 10px;
}

img {
  width: 30px;
  height: 30px;
}

#word {
  margin: 15px auto;
  display: flex;
  font-size: 20px;
  justify-content: space-between;
  font-weight: bolder;
}

.notplay {
  color: #de6648;
}

.isplay {
  color: #ffb001;
}

.content {
  display: block;
}
</style>
