<template>
  <div class="show">
    <div class="title">
      <img src="https://daisy-donald.cn/image/rainbow.png">
      <p>{{ bookname }}</p>
    </div>
    <div class="items">
      <button id="guide" @click="to_guide">亲子阅读指导</button>
      <button id="ebook" @click="to_ebook">E-Book</button>
      <button id="practice" @click="to_practice">课后练习</button>
      <button id="expanding" @click="to_expanding">阅读拓展</button>
    </div>
    <div class="function">
      <div class="to-community" @click="to_community">
        <img src="https://daisy-donald.cn/image/community.png">
        <p>社群</p>
      </div>
      <div class="to-ranking" @click="to_ranking">
        <img src="https://daisy-donald.cn/image/ranking.png">
        <p>排行榜</p>
      </div>
      <div class="to-mine" @click="to_mine">
        <img src="https://daisy-donald.cn/image/man.png">
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
      bookprocess: null,
      persual: null,
      level: null
    }
  },
  onLoad: function(option) {
    this.username = option.username
    this.booknumber = parseInt(option.booknum)
    this.level = option.level
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
          Tools.get_url() + 'get_book_info',
          qs.stringify({
            booknumber: save.booknumber
          })
        )
        .then(function(response) {
          save.persual =
            response.data.bookpersual === 'true' ? 'persual' : 'not_persual'
          save.bookname = response.data.bookname
          save.level = response.data.booklevel
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
    to_guide: function() {
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
    to_ebook: function() {
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
    to_practice: function() {
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
    to_expanding: function() {
      let save = this
      wx.navigateTo({
        url:
          '../expanding/main?username=' +
          save.username +
          '&book=' +
          save.booknumber +
          '&booktitle=' +
          save.bookname +
          '&level=' +
          save.level
      })
    },
    to_community: function() {
      let save = this
      wx.navigateTo({
        url:
          '../community/main?username=' +
          save.username +
          '&level=' +
          save.level
      })
    },
    to_ranking() {
      let save = this
      wx.navigateTo({
        url:
          '../ranking/main?username=' +
          save.username +
          '&level=' +
          save.level
      })
    },
    to_mine: function() {
      let save = this
      wx.navigateTo({
        url: '../mine/main?username=' + save.username
      })
    }
  }
}
</script>

<style>
page {
  background-size: 100% 100%;
  background-image: url('https://daisy-donald.cn/image/sky.jpg');
}

.show {
  width: 75%;
  margin: 30px auto;
}

.items {
  margin: 60px auto;
}

.function {
  display: flex;
  justify-content: space-between;
}

.function div {
  width: 70px;
  height: 90px;
  text-align: center;
}

.function p {
  color: #ff9000;
  font-weight: bolder;
  font-size: 18px;
  margin: -5px auto;
}

.function img {
  width: 60px;
  height: 60px;
}

.items button {
  color: #fff;
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

.title p {
  color: yellow;
  font-size: 30px;
  font-weight: bold;
  text-shadow: 2px 2px 3px #000;
}

.title img {
  width: 70px;
  height: 70px;
}

#guide {
  background-color: #019dd6;
}

#ebook {
  background-color: #f67c30;
}

#practice {
  background-color: #f53076;
}

#expanding {
  background-color: #00c544;
}
</style>
