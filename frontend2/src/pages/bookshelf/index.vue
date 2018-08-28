<template>
  <div class="bookinterface">
    <div class="title">
      <img src="/static/img/rainbow.png">
      <p>K{{ level + 1 }}</p>
    </div>
    <i-row class="body">
      <i-col span="18" offset="1">
        <div class="bookshelf">
          <book v-for="book in nowbooks"
            :book="book"
            @on_click="get"
            class="book">
          </book>
        </div>
      </i-col>
      <i-col span="3" offset="1">
        <iconbtn
          @persual="change_to_persual"
          @not_persual="change_to_not_persual"
          @toprevious="change_to_previous"
          @tonext="change_to_next">
        </iconbtn>
      </i-col>
    </i-row>
    <div class="bottom">
      <i-row>
        <i-col span="17" offset="1">
          <div>
            <input type="text"
              class="inline"
              v-model="search_text"
              placeholder='搜索' clearable />
            <img src="https://daisy-donald.cn/image/search.png"
              @click="search"
              class="inline search-icon">
          </div>
        </i-col>
        <i-col span="5">
          <div class="to-mine" @click="to_mine">
            <img src="https://daisy-donald.cn/image/man.png">
            <p class="text">我的</p>
          </div>
        </i-col>
      </i-row>
    </div>
  </div>
</template>

<script>
import book from '@/components/book'
import iconbtn from '@/components/iconbtn'
import * as Tools from '../../components/Tools.js'
import qs from 'qs'

export default {
  data() {
    return {
      username: '',
      nowbooks: [],
      candicate_books: [],
      persualbooks: [],
      notpersualbooks: [],
      level: 0,
      search_text: '',
      maxpersualshelf: 0,
      maxnotpersualshelf: 0,
      nowshelf: 0,
      nowbookkind: true
    }
  },
  components: {
    book,
    iconbtn
  },
  onLoad: function(option) {
    this.username = option.username
    this.level = parseInt(option.level)
  },
  onShow: function() {
    this.init()
  },
  methods: {
    init: function() {
      this.persualbooks = []
      this.notpersualbooks = []
      let fly = Tools.get_fly()
      let save = this
      fly
        .post(
          Tools.get_url() + 'get_books',
          qs.stringify({
            level: save.level,
            id: save.username
          })
        )
        .then(function(response) {
          let books = response.data.answer
          for (let book of books) {
            book.process *= 100
            if (book.is_persual === true) {
              save.persualbooks.push(book)
            } else {
              save.notpersualbooks.push(book)
            }
          }
          save.maxpersualshelf = (save.persualbooks.length - 1) / 9 + 1
          save.maxnotpersualshelf = (save.notpersualbooks.length - 1) / 9 + 1
          save.candicate_books = save.nowbookkind
            ? save.persualbooks
            : save.notpersualbooks
          save.split_books()
        })
    },
    get: function(book) {
      let save = this
      wx.navigateTo({
        url:
          '../show/main?username=' +
          save.username +
          '&booknum=' +
          book.number +
          '&level=' +
          save.level
      })
    },
    split_books: function() {
      this.nowbooks = []
      for (
        let i = this.nowshelf * 9;
        i < this.candicate_books.length && i < (this.nowshelf + 1) * 9;
        i++
      ) {
        this.nowbooks.push(this.candicate_books[i])
      }
    },
    change_to_next: function() {
      if ((this.nowshelf + 1) * 9 >= this.candicate_books.length) {
        wx.showToast({
          title: '已经是最后一页',
          icon: 'none',
          duration: 1500,
          mask: true
        })
      } else {
        this.nowshelf++
        this.split_books()
      }
    },
    change_to_previous: function() {
      if (this.nowshelf <= 0) {
        wx.showToast({
          title: '已经是第一页',
          icon: 'none',
          duration: 1500,
          mask: true
        })
      } else {
        this.nowshelf--
        this.split_books()
      }
    },
    change_to_persual: function() {
      if (this.nowbookkind) {
        wx.showToast({
          title: '现在已是精读书',
          icon: 'success',
          duration: 1500,
          mask: true
        })
      }
      this.nowbookkind = true
      this.candicate_books = this.persualbooks
      this.nowshelf = 0
      this.split_books()
    },
    change_to_not_persual: function() {
      if (!this.nowbookkind) {
        wx.showToast({
          title: '现在已是泛读书',
          icon: 'success',
          duration: 1500,
          mask: true
        })
      }
      this.nowbookkind = false
      this.candicate_books = this.notpersualbooks
      this.nowshelf = 0
      this.split_books()
    },
    search: function() {
      let start_books = this.nowbookkind
        ? this.persualbooks
        : this.notpersualbooks
      this.candicate_books = []
      this.nowshelf = 0
      for (let i = 0; i < start_books.length; i++) {
        if (start_books[i].name.indexOf(this.search_text) !== -1) {
          this.candicate_books.push(start_books[i])
        }
      }
      this.split_books()
    },
    to_mine: function() {
      wx.navigateTo({
        url: '../mine/main?username=' + this.username
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

.title {
  height: 70px;
  line-height: 70px;
  text-align: center;
  display: flex;
  justify-content: center;
}

.title p {
  font-size: 30px;
  font-weight: bold;
}

.title img {
  width: 70px;
  height: 70px;
}

.bookshelf {
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;
  background-image: url('https://daisy-donald.cn/image/shelf.png');
  background-size: 100% 100%;
  padding-left: 5px;
  padding-right: 5px;
  padding-top: 4px;
  padding-bottom: 11px;
  height: 360px;
  z-index: 5;
}

.book {
  height: 33%;
}

.body {
  margin: 20px 0px;
}

.to-mine {
  width: 70px;
  height: 90px;
  font-weight: bolder;
  font-size: 18px;
  text-align: center;
  margin: 20px 15px;
}

.to-mine img {
  width: 60px;
  height: 60px;
}

.text {
  color: black;
}

input {
  height: 30px;
  color: white;
  border: white solid 4px;
  padding: 5px;
  font-weight: bolder;
  background-color: #ffb001;
  border-radius: 10px;
  margin-top: 10%;
  width: 75%;
}

.inline {
  display: inline-block;
}

.search-icon {
  width: 40px;
  height: 40px;
}
</style>
