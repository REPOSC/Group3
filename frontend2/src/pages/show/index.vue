<template>
  <div class="div">
    <button id="btn1" @click="toGuide">亲子阅读指导</button>
    <button id="btn2" @click="toEbook">E-Book</button>
    <button id="btn4" @click="toPractice">课后练习</button>
    <button id="btn5" @click="toExpanding">阅读拓展</button>
    <div class="bottom">
      <div class="function" @click="toCommunity">
        <img src="/static/img/man.png">
        <p>社群</p>
      </div>
      <div class="function" @click="toMe">
        <img src="/static/img/man.png">
        <p>我的</p>
      </div>
    </div>
  </div>
</template>

<script>
import * as Tools from '../../components/Tools.js'
import qs from 'qs'

export default {
  data: function() {
    return {
      username: null,
      booknumber: null,
      bookname: null,
      bookprocess: null
    }
  },
  onLoad: function(option) {
    this.username = option.username
    this.booknumber = parseInt(option.booknum)
    this.bookname = option.bookname
  },
  onShow: function() {
    this.init()
  },
  methods: {
    init: function(option) {
      let fly = Tools.get_fly()
      let save = this
      fly
        .post(
          Tools.get_url() + 'get_process',
          qs.stringify({
            username: save.username,
            booknumber: save.booknumber
          })
        )
        .then(function(response) {
          save.bookprocess = response.data.bookprocess
        })
    },
    toGuide: function() {
      let save = this
      wx.navigateTo({
        url:
          '../guide/main?username=' +
          save.username +
          '&booknumber=' +
          save.booknumber +
          '&bookname=' +
          save.bookname
      })
    },
    toEbook: function() {
      let save = this
      wx.navigateTo({
        url:
          '../e_book/main?username=' +
          save.username +
          '&booknumber=' +
          save.booknumber +
          '&bookname=' +
          save.bookname +
          '&process=' +
          save.bookprocess
      })
    },
    toTranslation: function() {
      let save = this
      wx.navigateTo({
        url:
          '../translation/main?username=' +
          save.username +
          '&book=' +
          save.booknumber
      })
    },
    toPractice: function() {
      let save = this
      wx.navigateTo({
        url:
          '../practice/main?username=' +
          save.username +
          '&book=' +
          save.booknumber
      })
    },
    toCommunity: function() {
      let save = this
      wx.navigateTo({
        url:
          '../community/main?username=' +
          save.username +
          '&book=' +
          save.booknumber
      })
    },
    toMe: function() {
      let save = this
      wx.navigateTo({
        url: '../me/main?username=' + save.username + '&book=' + save.booknumber
      })
    },
    toExpanding: function() {
      let save = this
      wx.navigateTo({
        url:
          '../expanding/main?username=' +
          save.username +
          '&book=' +
          save.booknumber
      })
    }
  }
}
</script>

<style>
page {
  background-size: 100% 100%;
  background-image: url('https://daisy-donald.cn/image/back.jpg');
}

.div {
  padding: 60px 50px;
}

button {
  width: 80%;
  color: #fff;
  font-weight: bold;
  margin: 30px auto;
}

.bottom {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin: 30px;
}

.function {
  text-align: center;
}

img {
  margin-top: 50px;
  width: 70px;
  height: 70px;
}

p {
  color: #ffb001;
  font-size: 20px;
  font-weight: bold;
}

#btn1 {
  background-color: #019dd6;
}

#btn2 {
  background-color: #f67c30;
}

#btn3 {
  background-color: #00c544;
}

#btn4 {
  background-color: #f53076;
}

#btn5 {
  background-color: #00fe90;
}
</style>
