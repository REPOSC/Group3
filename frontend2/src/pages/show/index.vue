<template>
  <div>
    <div class="title">
      <img src="/static/img/rainbow.png">
      <p>Book1</p>
    </div>
    <div class="items">
      <button id="btn1" @click="toGuide">亲子阅读指导</button>
      <button id="btn2" @click="toEbook">E-Book</button>
      <button id="btn4" @click="toPractice">课后练习</button>
      <button id="btn5" @click="toExpanding">阅读拓展</button>
    </div>
    <div class="function">
      <div @click="toCommunity">
        <img class="icon" src="/static/img/tabbar_icon/yellow-com.png"/>
        <span>社群</span>
      </div>
      <div @click="toMe">
        <img class="icon" src="/static/img/tabbar_icon/yellow-me.png"/>
        <span>我的</span>
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
      bookprocess: null,
      persual: null
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
          Tools.get_url() + 'get_book_persual',
          qs.stringify({
            booknumber: save.booknumber
          })
        )
        .then(function(response) {
          save.persual =
            response.data.bookpersual === 'true' ? 'persual' : 'not_persual'
        })
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
    toPractice: function() {
      let save = this
      if (this.persual === 'not_persual') {
        wx.showToast({
          title: '此书为泛读书，暂无课后练习哦~',
          icon: 'none'
        })
      } else {
        wx.navigateTo({
          url:
            '../practice/main?username=' +
            save.username +
            '&book=' +
            save.booknumber
        })
      }
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
        url: '../me/main?username=' + save.username
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

.items {
  margin: 60px auto;
}

.function {
  height: 50px;
  width: 100%;
  display: flex;
  justify-content: space-around;
  position: fixed;
  bottom: 0;
  background-color: #53cce9;
}

.function div {
  display: flex;
  flex-wrap: wrap;
  height: 50px;
  width: 50px;
}

.function span {
  height: 20px;
  width: 50px;
  color: #666;
  font-size: 12px;
  text-align: center;
}

.function img {
  width: 30px;
  height: 30px;
  margin: 0 auto;
}

.items button {
  color: #fff;
  width: 75%;
  height: 50px;
  line-height: 50px;
  font-size: 20px;
  font-weight: bold;
  margin: 30px auto;
}

.title {
  height: 70px;
  line-height: 70px;
  margin: 30px;
  text-align: center;
  display: flex;
  justify-content: center;
}

p {
  color: yellow;
  font-size: 30px;
  font-weight: bold;
  text-shadow: 2px 2px 3px #000;
}

.title img {
  width: 70px;
  height: 70px;
}

.icon img {
  margin-top: 50px;
  width: 70px;
  height: 70px;
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
