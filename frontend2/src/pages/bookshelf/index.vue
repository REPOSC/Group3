<template>
<div class="bookinterface" @click="get">
  <i-row class="title">
    <i-col span="8" offset="1">
      <img src="/static/img/rainbow.png">
    </i-col>
    <i-col span="4" offset="1">
      <h1>{{ level + 1 }}</h1>
    </i-col>
  </i-row>
  <i-row class="body">
    <i-col span="18" offset="1">
      <div class="bookshelf">
        <book v-for="book in nowbooks" :key="book.number" :book="book" alt="book" @click="get"></book>
      </div>
    </i-col>
    <i-col span="3" offset="1">
      <iconbtn></iconbtn>
    </i-col>
  </i-row>
  <div class="bottom">
    <i-row>
      <i-col span="17" offset="1">
        <div class="search">
          <input type="text" v-model="search" placeholder='搜索' clearable/>
        </div>
      </i-col>
      <i-col span="5">
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
import book from "@/components/book";
import iconbtn from "@/components/iconbtn";
import * as Tools from "../../components/Tools.js";
import qs from "qs";
export default {
  data() {
    return {
      username: "",
      nowbooks: [],
      persualbooks: [],
      notpersualbooks: [],
      level: "",
      search: "",
      maxpersualshelf: 0,
      maxnotpersualshelf: 0,
      nowshelf: 0,
      nowbookkind: true
    };
  },
  components: {
    book,
    iconbtn
  },
  onLoad: function(option) {
    this.username = option.username;
    this.level = option.level;
    let fly = Tools.get_fly();
    let save = this;
    fly
      .post(
        Tools.get_url() + "get_books",
        qs.stringify({
          level: save.level,
          id: save.username
        })
      )
      .then(function(response) {
        let books = response.data.answer;
        for (let book in books) {
          if (books[book].is_persual === true) {
            save.persualbooks.push(books[book]);
          } else {
            save.notpersualbooks.push(books[book]);
          }
        }
        save.maxpersualshelf = (save.persualbooks.length - 1) / 9 + 1;
        save.maxnotpersualshelf = (save.notpersualbooks.length - 1) / 9 + 1;
        console.log(save.persualbooks);
        console.log(save.notpersualbooks);
      });
  },
  onReady: function() {
    this.get()
  },
  methods: {
    get: function() {
      this.nowbooks = []
      this.nowbooks = this.getbooks()
    },
    getbooks: function() {
      let nowbooks = [];
      let save = this;
      if (save.nowbookkind === true) {
        for (
          let i = save.nowshelf * 9;
          (i < save.persualbooks.length) & (i < (save.nowshelf + 1) * 9);
          i++
        ) {
          nowbooks.push(save.persualbooks[i]);
        }
        save.nowbookkind = false
      } else {
        for (
          let i = save.nowshelf * 9;
          (i < save.notpersualbooks.length) & (i < (save.nowshelf + 1) * 9);
          i++
        ) {
          nowbooks.push(save.notpersualbooks[i]);
        }
      }
      console.log(nowbooks)
      return nowbooks;
    },
    storebook: function() {},
    toMe: function() {
      console.log("click tome");
    },
    choosebook: function() {}
  }
};
</script>

<style>
page {
  background-size: 100% 100%;
  background-image: url("https://139.199.106.168/image/back.jpg");
}
.search {
  margin-top: 20px;
}
h1 {
  margin-top: 30px;
  padding: 2px;
  color: #ffb001;
  font-size: 43px;
  font-family: fantasy;
}
.title img {
  margin-top: 10px;
  width: 90px;
  height: 90px;
}
.bookshelf {
  display: flex;
  flex-wrap: wrap;
  justify-content: left;
  background-image: url("https://139.199.106.168/image/shelf.png");
  background-size: 100% 100%;
  padding-left: 5px;
  padding-right: 5px;
  padding-top: 4px;
  padding-bottom: 11px;
  height: 360px;
}
.body {
  margin: 20px 0px;
}
.toMeBtn {
  width: 70px;
  height: 90px;
  font-weight: bolder;
  color: white;
  font-size: 18px;
  text-align: center;
  float: right;
}
.toMeBtn img {
  width: 70px;
  height: 70px;
}
input {
  height: 50px;
  color: white;
  border: white solid 4px;
  font-weight: bolder;
  background-color: #ffb001;
  border-radius: 3%;
}
</style>
