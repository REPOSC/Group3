<template>
<div class="bookinterface">
  <i-row class="title">
    <i-col span="8" offset="1">
      <img src="/static/img/rainbow.png">
    </i-col>
    <i-col span="4" offset="1">
      <h1>{{ level }}</h1>
    </i-col>
  </i-row>
  <i-row class="body">
    <i-col span="18" offset="1">
      <div class="bookshelf">
        <book :key="book.id" v-for="book in books" :book="book" alt="book" @click="choosebook"></book>
      </div>
    </i-col>
    <i-col span="3" offset="1">
      <iconbtn ref="childMethod"></iconbtn>
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
export default {
  data() {
    return {
      books: [
        {
          id: 1,
          percent: 10,
          title: "BOOK1",
          image: "/static/img/english1.jpg"
        },
        {
          id: 2,
          percent: 90,
          title: "BOOK1",
          image: "/static/img/english1.jpg"
        },
        {
          id: 3,
          percent: 30,
          title: "BOOK1",
          image: "/static/img/english1.jpg"
        },
        {
          id: 4,
          percent: 10,
          title: "BOOK1",
          image: "/static/img/english1.jpg"
        },
        {
          id: 5,
          percent: 90,
          title: "BOOK1",
          image: "/static/img/english1.jpg"
        },
        {
          id: 6,
          percent: 30,
          title: "BOOK1",
          image: "/static/img/english1.jpg"
        },
        {
          id: 7,
          percent: 10,
          title: "BOOK1",
          image: "/static/img/english1.jpg"
        },
        {
          id: 8,
          percent: 90,
          title: "BOOK1",
          image: "/static/img/english1.jpg"
        },
        {
          id: 9,
          percent: 30,
          title: "BOOK1",
          image: "/static/img/english1.jpg"
        }
      ],
      level: "K1",
      search: ""
    };
  },
  components: {
    book,
    iconbtn
  },
  methods: {
    toMe() {
      console.log("click tome");
    },
    choosebook() {}
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
  justify-content: center;
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
