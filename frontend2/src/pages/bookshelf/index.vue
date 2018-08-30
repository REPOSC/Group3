<template>
  <div class="book-interface">
    <div class="title">
      <img src="https://daisy-donald.cn/image/rainbow.png">
      <p>K{{ level + 1 }}</p>
    </div>
    <div class="body">
      <div class="bookshelf">
        <book v-for="book in nowbooks"
          :book="book"
          @on_click="get"
          class="book">
        </book>
      </div>
      <div class="iconbtn">
        <iconbtn
          @persual="change_to_persual"
          @not_persual="change_to_not_persual"
          @toprevious="change_to_previous"
          @tonext="change_to_next">
        </iconbtn>
      </div>
    </div>
    <div class="bottom">
      <div class="search">
        <input type="text"
          v-model="search_text"
          placeholder='搜索' clearable />
        <img src="https://daisy-donald.cn/image/yellow-search.png"
          @click="search"/>
      </div>
      <div class="to-mine" @click="to_mine">
        <img src="https://daisy-donald.cn/image/man.png">
        <p>我的</p>
      </div>
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

.book-interface {
  margin: 10px 10px;
}

.title {
  position: relative;
  height: 95px;
  line-height: 95px;
  margin: 0 20px;
}

.title p {
  font-size: 40px;
  font-weight: bold;
}

.title img {
  position: absolute;
  left: 0;
  bottom: -20px;
  width: 100px;
  height: 100px;
}

.body {
  margin: 20px 0;
  display: flex;
  justify-content: space-between;
}

.bookshelf {
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;
  background-image: url('https://daisy-donald.cn/image/shelf.png');
  background-size: 100% 100%;
  height: 360px;
  width: 300px;
}

.book {
  height: 33%;
}

.bottom {
  height: 90px;
  display: flex;
  margin: 20px 0;
  justify-content: space-between;
}

.to-mine {
  width: 70px;
  height: 90px;
  font-weight: bolder;
  font-size: 18px;
  text-align: center;
  color: #ff9000;
}

.to-mine img {
  width: 50px;
  height: 50px;
}

.search {
  display: flex;
  width: 80%;
  height: 40px;
  line-height: 40px;
  margin: 20px 10px 20px 0;
  border: #ffb001 solid 5px;
  border-radius: 10px;
  background-color: white;
}

.search input {
  height: 40px;
  color: #ffb001;
  font-weight: bold;
  width: 85%;
  margin: auto 5px;
}

.search img {
  width: 30px;
  height: 30px;
  margin: auto 10px;
}
</style>
