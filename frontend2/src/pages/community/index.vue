<template>
  <div class="container">
    <div class="record" :key="record.id" v-for="record in records">
      <div class="user">
        <img :src="record.avatar" />
        <p class="username">{{ record.username }}</p>
      </div>
      <p class="content">{{ record.content }}</p>
      <div class="action">
        <button id="like" @click="like">赞</button>
        <button id="comment" @click="comment">评论</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      records: [
        {
          id: 1,
          avatar: '/static/img/game2/cat1.jpg',
          username: '小吉',
          content: '今天我学了10个单词',
          comments: [
            {
              id: 1,
              username: '小蒜',
              content: '我是小蒜'
            },
            {
              id: 2,
              username: '小可',
              content: '我是小可'
            }
          ]
        },
        {
          id: 2,
          avatar: '/static/img/game2/cat2.jpg',
          username: '小蒜',
          content: '今天我学了8个单词'
        },
        {
          id: 3,
          avatar: '/static/img/game2/cat3.jpg',
          username: '小可',
          content: '今天我学了6个单词'
        }
      ]
    }
  },
  methods: {
    like() {},
    comment() {}
  }
}
</script>

<style scoped>
page {
  background-size: 100% 100%;
  background-image: url('https://daisy-donald.cn/image/back.jpg');
}
.container {
  display: flex;
  height: 100%;
  padding-top: 10px;
}
.record {
  width: 90%;
  margin: 4%;
  border: 5px solid #53cce9;
  border-radius: 10px;
}
.user {
  display: flex;
}
.username {
  font-weight: bold;
  height: 40px;
  line-height: 40px;
}
.action {
  margin-left: 50%;
  display: flex;
  justify-content: space-between;
}
#like {
  width: 40%;
  color: #fff;
  font-weight: bold;
  background-color: #f53076;
}
#comment {
  width: 40%;
  color: #fff;
  font-weight: bold;
  background-color: #ffb001;
}
.about_me {
  position: fixed;
  bottom: 10px;
  width: 100%;
  display: flex;
  justify-content: space-around;
}
.about_me button {
  color: #fff;
  font-size: 22px;
  background-color: #ffb001;
  border-radius: 10px;
}
img {
  width: 30px;
  height: 30px;
  margin: 5px;
}
</style>
