<template>
  <div class="game">
    <loading :hidden="hidden">
      加载中...
    </loading>
    <div class="introduce">
      <button @click="play_video()">{{ video_function.play_info }}</button>
    </div>
    <div v-if="video_function.is_play_video" class="video">
      <video :src="video_function.src" />
    </div>
    <div class="content">
      <div class="words">
        <div :class="word.status" v-for="word in words" :key="word.index"
         @click="click_word(word)">{{ word.text }}
        </div>
      </div>
      <canvas canvas-id="draw_line"></canvas>
      <div class="pics">
        <div class="pic" :key="pic.index" v-for="pic in pics">
          <img :class="pic.status" :src="pic.src" mode="aspectFit"
          @click="click_picture(pic)" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import * as Tools from '../../components/Tools.js'
import qs from 'qs'
export default {
  data() {
    return {
      video_function: {
        play_info: '功能讲解',
        is_play_video: false,
        src: null
      },
      booknumber: null,
      now_word: '',
      now_pic: '',
      length: 0,
      words: [],
      pics: [],
      hidden: true
    }
  },
  onLoad(status) {
    this.booknumber = status.booknumber
  },
  onShow() {
    this.init()
  },
  methods: {
    init() {
      this.now_word = ''
      this.now_pic = ''
      this.length = 0
      this.words = []
      this.pics = []
      let fly = Tools.get_fly()
      let save = this
      fly
        .post(
          Tools.get_url() + 'get_first_game_texts',
          qs.stringify({
            book_id: save.booknumber
          })
        )
        .then(function(response) {
          let texts = response.data.texts
          let random_indexs = Tools.generate_random_list(texts.length)
          for (let i = 0; i < texts.length; ++i) {
            save.words.push({
              index: i,
              text: texts[i],
              status: 'word_unmatch'
            })
            save.pics.push({
              index: i,
              match_index: random_indexs[i],
              status: 'pic_unmatch'
            })
          }
          for (let i = 0; i < texts.length; ++i) {
            wx.downloadFile({
              url:
                Tools.get_url() +
                'get_first_game_image?book_id=' +
                save.booknumber +
                '&word_text=' +
                save.words[save.pics[i].match_index].text,
              success: function(picture_response) {
                if (picture_response.statusCode === 200) {
                  let pic_tmp_obj = save.pics[i]
                  pic_tmp_obj.src = picture_response.tempFilePath
                  save.$set(save.pics, i, pic_tmp_obj)
                }
              }
            })
          }
          save.length = save.words.length
        })
    },
    line_start(word_index) {
      return word_index * 120 + 75
    },
    line_end(pic_index) {
      return pic_index * 120 + 75
    },
    draw_line() {
      let context = wx.createCanvasContext('draw_line')
      context.setStrokeStyle('#53cce9')
      context.setLineWidth(5)
      for (let i = 0; i < this.words.length; i++) {
        if (this.pics[i].status === 'pic_matched') {
          context.moveTo(0, this.line_start(this.pics[i].match_index))
          context.lineTo(
            wx.getSystemInfoSync().windowWidth * 0.4,
            this.line_end(i)
          )
        }
      }
      context.stroke()
      context.draw()
    },
    click_word(word) {
      if (word.status === 'word_matching') {
        this.now_word = ''
        word.status = 'word_unmatch'
      } else {
        if (
          this.now_word !== '' &&
          this.words[this.now_word].status !== 'word_matched'
        ) {
          this.words[this.now_word].status = 'word_unmatch'
        }
        if (word.status === 'word_unmatch') {
          this.now_word = word.index
          word.status = 'word_matching'
        } else {
          this.now_word = ''
        }
      }
    },
    show_right_message() {
      this.length = this.length - 1
      if (this.length !== 0) {
        wx.showToast({
          title: '做对啦！真棒！',
          image: 'https://daisy-donald.cn/image/green-yes.png',
          duration: 800,
          mask: true
        })
      } else {
        wx.showModal({
          title: '宝宝真棒！',
          content: '已完成该练习，是否退出~',
          cancelText: '再看看',
          confirmText: '退出',
          confirmColor: '#ffb001',
          success: function(res) {
            if (res.confirm) {
              wx.navigateBack({
                url: '../practice/main'
              })
            }
          }
        })
      }
    },
    click_picture(pic) {
      if (pic.match_index === this.now_word) {
        this.show_right_message()
        pic.status = 'pic_matched'
        this.words[this.now_word].status = 'word_matched'
        this.draw_line()
        this.now_word = ''
      } else if (this.now_word !== '') {
        wx.showToast({
          title: '做错啦~再试试~',
          image: 'https://daisy-donald.cn/image/red-false.png',
          duration: 800,
          mask: true
        })
      } else {
        wx.showToast({
          title: '还没选择单词噢~',
          image: 'https://daisy-donald.cn/image/lock.png',
          duration: 800,
          mask: true
        })
      }
    },
    play_video() {
      if (!this.video_function.is_play_video) {
        this.video_function.is_play_video = true
        this.video_function.play_info = '关闭'
        this.hidden = false
        let save = this
        wx.downloadFile({
          url: Tools.get_url() + 'get_video?item=first_game',
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

.game {
  position: relative;
  margin-top: 20px;
}

.introduce {
  margin: 0 10% 0 70%;
}

button {
  color: white;
  font-size: 10px;
  font-weight: bolder;
  line-height: 20px;
  background-color: #ffb100;
}

.video {
  margin: 10px auto;
  text-align: center;
}

canvas {
  width: 40%;
  height: auto;
}

.content {
  display: flex;
  justify-content: space-between;
  margin: 10px 10px;
}

.words,
.pics {
  width: 30%;
}

.words div {
  color: #fff;
  font-size: 25px;
  height: 90px;
  width: 100%;
  line-height: 80px;
  text-align: center;
  margin: 30px auto;
  border-radius: 10px;
}

.pic {
  height: 90px;
  width: 100%;
  line-height: 80px;
  text-align: left;
  margin: 30px auto;
  border-radius: 10px;
}

.pics img {
  width: 80px;
  height: 80px;
  border-radius: 10px;
}

.word_unmatch {
  background-color: #ffb001;
}

.word_matching {
  background-color: #53cce9;
}

.word_matched {
  background-color: #cccccc;
}

.pic_unmatch {
  display: inline-block;
  border: 5px solid #ffb001;
}

.pic_matching {
  display: inline-block;
  border: 5px solid #53cce9;
}

.pic_matched {
  border: 5px solid #cccccc;
}
</style>
