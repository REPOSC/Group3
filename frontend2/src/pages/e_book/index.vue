<template>
  <div class="e-book">
    <loading :hidden="hidden">
      加载中...
    </loading>
    <title v-bind="video_function" @play_video="play_video"></title>
    <div class="body">
      <div class="book">
        <img :src="imagesrc" mode="scaleToFill" class="image">
      </div>
      <div class="function">
        <button class="previous" @click="to_previouspage"></button>
        <button class="listen" @click="play_audio"></button>
        <button class="add" :isrecord="isrecord" @click="record"></button>
        <button class="play" :isplay="isplay" @click="play_record"></button>
        <button class="next" @click="to_nextpage"></button>
      </div>
      <div class="english-text">{{ english_text }}</div>
      <i-icon
        v-bind:type="chinese_button_state"
        @click="change_chinese_state"
        class="button"/>
      <div v-bind:class="chinese_state">{{ chinese_text }}</div>
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
      username: null,
      booknumber: 0,
      bookprocess: 0.0,
      booknowpage: 0,
      bookpagenumber: 0,
      imagesrc: null,
      isrecord: false,
      isplayrecord: false,
      isplay: false,
      recorderManager: null,
      recordsrc: '',
      innerRecordContext: null,
      innerAudioContext: null,
      english_text: '',
      chinese_text: '',
      chinese_state: null,
      chinese_button_state: 'add',
      hidden: true
    }
  },
  components: {
    title
  },
  onLoad: function(status) {
    this.username = status.username
    this.booknumber = status.booknumber
    this.video_function.booktitle = status.bookname
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
          save.get_book()
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
    get_book() {
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
        success: function(response) {
          if (response.statusCode === 200) {
            save.imagesrc = response.tempFilePath
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
    play_audio() {
      let save = this
      wx.downloadFile({
        url:
          Tools.get_url() +
          'get_page_audio?book_id=' +
          save.booknumber +
          '&page_index=' +
          save.booknowpage,
        success: function(response) {
          if (response.statusCode === 200) {
            save.innerAudioContext.src = response.tempFilePath
            save.innerAudioContext.play()
          }
        }
      })
    },
    to_previouspage() {
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
      this.get_book()
    },
    to_nextpage() {
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
      this.get_book()
    },
    record() {
      let save = this
      if (save.isplayrecord) {
        wx.showToast({
          title: '正在播放录音中，无法录音',
          icon: 'none'
        })
      } else {
        if (save.isrecord) {
          save.recorderManager.stop()
          save.recorderManager.onStop(response => {
            this.recordsrc = response.tempFilePath
            this.innerRecordContext.src = this.recordsrc
          })
        } else {
          save.recorderManager.start()
        }
        save.isrecord = !save.isrecord
      }
    },
    play_record() {
      let save = this
      if (save.isrecord) {
        wx.showToast({
          title: '正在录音中，无法播放',
          icon: 'none'
        })
      } else {
        if (save.isplayrecord === true) {
          save.innerRecordContext.stop()
        } else {
          save.innerRecordContext.play()
        }
        save.isplayrecord = !save.isplayrecord
      }
    },
    play_video() {
      if (!this.video_function.is_play_video) {
        this.video_function.is_play_video = true
        this.video_function.play_info = '关闭'
        this.hidden = false
        let save = this
        wx.downloadFile({
          url: Tools.get_url() + 'get_video?item=ebook',
          success: function(video_response) {
            if (video_response.statusCode === 200) {
              save.video_function.src = video_response.tempFilePath
              console.log(save.video_function.src)
            }
            save.hidden = true
          }
        })
      } else {
        this.video_function.is_play_video = false
        this.video_function.play_info = '功能讲解'
      }
    }
  },
  onUnload: function() {
    this.recorderManager.stop()
    this.innerRecordContext.stop()
  }
}
</script>

<style>
page {
  background-size: 100% 100%;
  background-image: url('https://daisy-donald.cn/image/sky.jpg');
}

.e-book {
  margin: 10px 10px;
}

title {
  height: 70px;
}

.body {
  margin: auto 20px;
  border: 4px solid #ffb001;
  background-color: white;
}

.book {
  text-align: center;
  width: 100%;
  height: 200px;
}

.function {
  margin: 20px auto;
  text-align: center;
}

.function button {
  display: inline-block;
  width: 50px;
  height: 50px;
  background-size: 100% 100%;
  border: 1px solid #ffb001;
  vertical-align: middle;
}

.previous {
  background-image: url('http://daisy-donald.cn/image/left.png');
}

.listen {
  background-image: url('http://daisy-donald.cn/image/listen.png');
}

.add {
  background-image: url('http://daisy-donald.cn/image/add.png');
}

.play {
  background-image: url('http://daisy-donald.cn/image/play.png');
}

.next {
  background-image: url('http://daisy-donald.cn/image/right.png');
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
