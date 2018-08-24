<template>
  <div class="content">
    <div class="words">
      <div :class="word.status" v-for="word in words" :key="word.index" @click="click_word(word)">
        {{ word.text }}
      </div>
    </div>
    <canvas canvas-id="drawline"></canvas>
    <div class="pics">
      <img :key="pic.index" v-for="pic in pics" :class="pic.status" :src="pic.src" mode="aspectFit" @click="click_picture(pic)" />
    </div>
  </div>
</template>

<script>
import * as Tools from '../../components/Tools.js'
import qs from 'qs'
export default {
  data() {
    return {
      booknumber: null,
      now_word: '',
      now_pic: '',
      length: 0,
      words: [],
      pics: []
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
              index: random_indexs[i],
              match_index: i,
              status: 'pic_unmatch'
            })
          }
          save.pics.sort(function(a, b) {
            return a.index > b.index ? 1 : a.index === b.index ? 0 : -1
          })
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
    line_end(pic_index) {
      return pic_index * 120 + 70
    },
    line_start(word_index) {
      return 120 * word_index + 75
    },
    drawline() {
      let context = wx.createCanvasContext('drawline')
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
          image: '/static/game2/green-yes.png',
          duration: 1500,
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
        this.drawline()
        this.now_word = ''
      } else if (this.now_word !== '') {
        wx.showToast({
          title: '做错啦~再试试~',
          image: '/static/game2/red-false.png',
          duration: 1500,
          mask: true
        })
      } else {
        wx.showToast({
          title: '还没选择单词噢~',
          image: '/static/game2/lock.png',
          duration: 1500,
          mask: true
        })
      }
    }
  }
}
</script>

<style scoped>
page {
  background-size: 100% 100%;
  background-image: url('https://thumbnail0.baidupcs.com/thumbnail/208d7bfe35c662f32a88a1fe206d44e9?fid=3911358295-250528-398515735348763&time=1534424400&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-mj%2BYVt%2Fbo9W%2BSqMC7ImwhtUDIcs%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=5285426163203658882&dp-callid=0&size=c710_u400&quality=100&vuk=-&ft=video');
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
.pics {
  margin-top: 10px;
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
.pics img {
  width: 80px;
  height: 80px;
  border-radius: 10px;
  margin: 15px 0 15px auto;
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
