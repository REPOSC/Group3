<template>
  <div class="full">
    <div class="title">
      <img src="http://139.199.106.168/image/y-book.png" alt="red-book-open">
      <h1>{{ booktitle }}</h1>
    </div>
    <div class="body">
      <div class="book">
        <img :src="imagesrc" alt="Bookcontent" mode="scaleToFill" class="image">
      </div>
      <div class="btngroup">
        <button class="previous" @click="previouspage"></button>
        <button class="listen" @click="playaudio"></button>
        <button class="add" :isrecord="isrecord" @click="record"></button>
        <button class="play" :isplay="isplay" @click="playrecord"></button>
        <button class="next" @click="nextpage"></button>
      </div>
      <div class="english-text">{{english_text}}</div>
      <i-icon v-bind:type="chinese_button_state" @click="change_chinese_state" class="button" />
      <div v-bind:class="chinese_state">{{chinese_text}}</div>
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
      booktitle: ' BOOK1 ',
      booknumber: 0,
      bookprocess: 0.0,
      booknowpage: 0,
      bookpagenumber: 0,
      imagesrc: null,
      isrecord: false,
      isplay: false,
      recorderManager: null,
      recordsrc: '',
      innerRecordContext: null,
      innerAudioContext: null,
      english_text: '',
      chinese_text: '',
      chinese_state: null,
      chinese_button_state: 'add'
    }
  },
  onLoad: function(status) {
    this.username = status.username
    this.booknumber = status.booknumber
    this.booktitle = status.bookname
    this.bookprocess = status.process
  },
  onShow: function() {
    this.init()
  },
  methods: {
    init: function(status) {
      let fly = Tools.get_fly()
      let save = this
      fly
        .post(
          Tools.get_url() + 'get_second_function',
          qs.stringify({
            book_id: save.booknumber
          })
        )
        .then(function(response) {
          save.bookpagenumber = response.data.page_number
          save.booknowpage = Math.round(save.bookpagenumber * save.bookprocess)
          if (parseInt(save.bookprocess) === 1) {
            save.booknowpage--
          }
          save.getbook()
        })
      this.chinese_state = 'hidden'
      this.recorderManager = wx.getRecorderManager()
      this.innerAudioContext = wx.createInnerAudioContext()
      this.innerRecordContext = wx.createInnerAudioContext()
    },
    change_process(number) {
      if (number > this.bookprocess) {
        this.bookprocess = number
        let fly = Tools.get_fly()
        let save = this
        fly.post(
          Tools.get_url() + 'change_process',
          qs.stringify({
            process: save.bookprocess,
            username: save.username,
            booknumber: save.booknumber
          })
        )
      }
    },
    getbook() {
      this.change_process(this.booknowpage / this.bookpagenumber)
      let fly = Tools.get_fly()
      let save = this
      fly
        .post(
          Tools.get_url() + 'get_page_texts',
          qs.stringify({
            book_id: save.booknumber,
            book_page: save.booknowpage
          })
        )
        .then(function(response) {
          save.english_text = response.data.english
          save.chinese_text = response.data.chinese
        })
      wx.downloadFile({
        url:
          Tools.get_url() +
          'get_page_image?book_id=' +
          save.booknumber +
          '&page_index=' +
          save.booknowpage,
        success: function(res) {
          if (res.statusCode === 200) {
            save.imagesrc = res.tempFilePath
          }
        }
      })
    },
    change_chinese_state() {
      if (this.chinese_state === 'hidden') {
        this.chinese_state = 'visible'
        this.chinese_button_state = 'close'
      } else {
        this.chinese_state = 'hidden'
        this.chinese_button_state = 'add'
      }
    },
    playaudio() {
      let save = this
      wx.downloadFile({
        url:
          Tools.get_url() +
          'get_page_audio?book_id=' +
          save.booknumber +
          '&page_index=' +
          save.booknowpage,
        success: function(res) {
          if (res.statusCode === 200) {
            save.innerAudioContext.src = res.tempFilePath
            save.innerAudioContext.play()
          }
        }
      })
    },
    previouspage() {
      if (this.booknowpage <= 0) {
        wx.showToast({
          title: '已经是第一页',
          icon: 'success',
          duration: 1500,
          mask: true
        })
      } else {
        this.booknowpage--
      }
      this.getbook()
    },
    nextpage() {
      if (this.booknowpage >= this.bookpagenumber - 1) {
        this.change_process(1)
        wx.showToast({
          title: '已经是最后一页',
          icon: 'success',
          duration: 1500,
          mask: true
        })
      } else {
        this.booknowpage++
      }
      this.getbook()
    },
    record() {
      let save = this
      if (save.isrecord === true) {
        save.recorderManager.stop()
        save.recorderManager.onStop(res => {
          this.recordsrc = res.tempFilePath
          this.innerRecordContext.src = this.recordsrc
        })
        save.isrecord = false
      } else {
        save.recorderManager.start()
        save.isrecord = true
      }
    },
    playrecord() {
      this.innerRecordContext.play()
    }
  }
}
</script>
<style>
page {
  background-size: 100% 100%;
  background-image: url('http://139.199.106.168/image/back.jpg');
}

.title {
  margin: 30px 20px;
  text-align: center;
}

h1 {
  display: inline-block;
  text-align: center;
  color: white;
  font-size: 35px;
  background-color: #ffb001;
  width: 150px;
  height: 50px;
  margin: auto 10px;
  vertical-align: middle;
  border-radius: 60%;
}

.title img {
  display: inline-block;
  width: 70px;
  height: 70px;
  vertical-align: middle;
}

.body {
  margin: auto 20px;
  border: 4px solid #ffb001;
  background-color: #ffb001;
}

.book {
  text-align: center;
  width: 100%;
  height: 200px;
}

.btngroup {
  margin: 10px auto;
  text-align: center;
  background-color: #ffb001;
}

.btngroup button {
  display: inline-block;
  width: 50px;
  height: 50px;
  background-size: 100% 100%;
  border: 1px solid #ffb001;
  vertical-align: middle;
}

.previous {
  background-image: url('http://139.199.106.168/image/left.png');
}

.listen {
  background-image: url('http://139.199.106.168/image/listen.png');
}

.add {
  background-image: url('http://139.199.106.168/image/add.png');
}

.play {
  background-image: url('http://139.199.106.168/image/play.png');
}

.next {
  background-image: url('http://139.199.106.168/image/right.png');
}

.hidden {
  visibility: hidden;
}

.visible {
  margin: 20px;
  visibility: visible;
  font-size: 20px;
}

.english-text {
  margin: 20px;
  font-family: 'Courier New', Courier, monospace;
  font-size: 30px;
  display: inline-block;
}

.image {
  height: 100%;
  width: 100%;
}

.button {
  float: right;
  margin: 20px;
}
</style>
