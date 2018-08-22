<template>
  <div>
    <i-row>
      <div class="head">
        <i-col span="5" offset="5">
          <img src="/static/img/blue-star.png">
        </i-col>
        <i-col span="5">
          <div class="title">
            <h1>{{ booktitle }}</h1>
          </div>
        </i-col>
      </div>
    </i-row>
    <div class="firstpart">
      <img src="/static/img/yellow-tap.png">
      <h1>本课重点知识 </h1>
      <p :key="index" v-for="(one,index) in ones">{{ index-0+1 }}、{{ one }}</p>
    </div>
    <div class="secpart">
      <img src="/static/img/green-tap.png">
      <h1>今日导读</h1>
      <p :key="index" v-for="(two,index) in twos">{{ index-0+1 }}、{{ two }}</p>
    </div>
    <div class="thirdpart">
      <div class="subtitle">
        <img src="/static/img/red-tap.png">
        <h1>词汇表与配音讲解</h1>
      </div>
      <div :key="index" v-for="(three,index) in threes">
        <div class="word">{{ index-0+1 }}、{{ three }}</div>
        <i-icon type="customerservice_fill" size="28" class="word" @click="hear(index)" />
      </div>
    </div>
    <div class="bottom">
      <i-row>
        <i-col span="6" offset="9">
          <div class="toMeBtn" @click="toMe">
            <img src="/static/img/man.png">
            <p>我的</p>
          </div>
        </i-col>
      </i-row>
    </div>
  </div>
</template>

<script>
import * as Tools from '../../components/Tools.js'
import qs from 'qs'

export default {
  data() {
    return {
      booktitle: ' BOOK1 ',
      booknumber: 0,
      ones: [],
      twos: [],
      threes: [],
      current_audio: null
    }
  },
  onLoad: function(status) {
    this.init(status)
  },
  methods: {
    init: function(status) {
      let fly = Tools.get_fly()
      this.booknumber = status.book
      let save = this
      fly
        .post(
          Tools.get_url() + 'get_first_function',
          qs.stringify({
            book_id: this.booknumber
          })
        )
        .then(function(response) {
          let knowledges = response.data.knowledge
          let guides = response.data.guide
          let word_contents = response.data.words
          save.ones = knowledges
          save.twos = guides
          save.threes = word_contents
        })
    },
    hear: function(index) {
      // let fly = Tools.get_fly()
      // let save = this
      // fly
      //     .post(
      //       Tools.get_url() + 'get_word_audio',
      //       qs.stringify({
      //         book_id: this.booknumber,
      //         audio_index: index
      //       })
      //     )
      //     .then(function(response) {
      //       save.current_audio = response.data
      //       console.log(save.current_audio)
      //     })
      wx.downloadFile({
        url:
          Tools.get_url() +
          'get_word_audio?book_id=' +
          this.booknumber +
          '&audio_index=' +
          index,
        success: function(res) {
          console.log(res)
          if (res.statusCode === 200) {
            wx.playVoice({
              filePath: res.tempFilePath,
              success: function() {
                console.log('hello')
              }
            })
            wx.playVoice({
              filePath: '/static/10500.wav',
              success: function() {
                console.log('hello')
              }
            })
          }
        }
      })
    }
  }
}
</script>

<style>
page {
  background-size: 100% 100%;
  /*background-image: url('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1534945615291&di=fa4a915965df971671ec98a8fe2d5a52&imgtype=0&src=http%3A%2F%2Fp.moto8.com%2Fforum%2F201201%2F04%2F195150zxaed89qa2e67t29.jpg');
*/
}
.head img {
  width: 60px;
  height: 60px;
}
.head h1 {
  font-size: 25px;
  font-weight: bolder;
  font-family: fantasy;
  color: white;
  background-color: #019dd6;
}
.title {
  margin-top: 15px;
}
.firstpart {
  color: #eff000;
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
.toMeBtn {
  position: fixed;
  width: 70px;
  height: 90px;
  font-weight: bolder;
  color: white;
  font-size: 18px;
  text-align: center;
  bottom: 10px;
}
.toMeBtn img {
  width: 70px;
  height: 70px;
}
.toMeBtn p {
  background-color: #ffb001;
  margin-left: 10px;
}
.word {
  display: inline;
}
</style>
