<template>
  <div>
    <div class="title">
      <img src="http://139.199.106.168/image/y-book.png" alt="red-book-open">
      <h1>{{ BookName }}</h1>
    </div>
    <div class="body">
      <div class="book">
        <img :src="src" alt="Bookcontent" mode="aspectFit">
      </div>
      <div class="btngroup">
        <button class="previous" @click="previouspage"></button>
        <button class="listen" @click="playaudio"></button>
        <button class="add" :isrecord="isrecord" @click="record"></button>
        <button class="play" :isplay="isplay" @click="playrecord"></button>
        <button class="next" @click="nextpage"></button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      BookName: 'BOOK1',
      src: 'http://139.199.106.168/image/bookface.jpg',
      isrecord: false,
      isplay: false,
      recorderManager: wx.getRecorderManager(),
      recordsrc: '',
      innerRecordContext: '',
      innerAudioContext: ''
    }
  },
  methods: {
    playaudio() {
      this.innerAudioContext = wx.createInnerAudioContext()
      this.innerAudioContext.src = this.recordsrc
      this.innerAudioContext.play()
    },
    previouspage() {
      let now = this
      now.src = 'http://139.199.106.168/image/bookface.jpg'
    },
    record() {
      let save = this
      if (save.isrecord === true) {
        save.recorderManager.stop()
        save.recorderManager.onStop(res => {
          // const tempFilePath = res
          this.recordsrc = res.tempFilePath
          this.innerRecordContext = wx.createInnerAudioContext()
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
    },
    nextpage() {
      let now = this
      now.src = 'http://139.199.106.168/image/bookmiddle.jpg'
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
  background-color: aliceblue;
}
.book {
  text-align: center;
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
</style>
