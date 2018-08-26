<template>
  <div class="container">
    <div class="record" v-for="(record, id) in records">
      <div class="user">
        <img :src="record.avatar" />
        <p class="username">{{ record.username }}</p>
      </div>
      <p class="content">{{ record.content }}</p>
      <div class="action">
        <button id="like" @click="like(id)">赞
          <span v-if="record.liked === false"></span>
          <span v-if="record.likes !== 0">{{ record.likes }}</span>
        </button>
        <button id="comment" @click="comment(id)">评论</button>
      </div>
      <div class="comment">
        <p v-for="comment in record.comments">
          <span class="username">{{ comment.username }}</span>
          : {{ comment.content }}
        </p>
        <div class="new-comment" v-if="record.commented">
          <textarea v-model="record.newcomment"/>
          <button id="submit" @click="submit(id)">发送</button>
        </div>
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
          avatar: '/static/img/game2/cat1.jpg',
          username: '小吉',
          content: '今天我学了10个单词',
          comments: [],
          newcomment: '',
          likes: 0,
          liked: false,
          commented: false
        },
        {
          avatar: '/static/img/game2/cat2.jpg',
          username: '小蒜',
          content: '今天我学了8个单词',
          comments: [],
          likes: 0,
          liked: false,
          newcomment: '',
          commented: false
        },
        {
          avatar: '/static/img/game2/cat3.jpg',
          username: '小可',
          content: '今天我学了6个单词',
          comments: [],
          likes: 0,
          liked: false,
          newcomment: '',
          commented: false
        }
      ]
    }
  },
  methods: {
    like(id) {
      if (this.records[id].liked === false) {
        this.records[id].likes += 1
      } else {
        this.records[id].likes -= 1
      }
      this.records[id].liked = !this.records[id].liked
    },
    comment(id) {
      this.records[id].commented = true
    },
    submit(id) {
      this.records[id].comments.push(
        { username: '小可', content: this.records[id].newcomment }
      )
      this.records[id].commented = false
      this.records[id].newcomment = ''
    }
  }
}
</script>

<style>
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
  background-color: antiquewhite;
  border: 5px solid #53cce9;
  border-radius: 10px;
}
.user {
  display: flex;
}
.username {
  color: #53cce9;
  height: 40px;
  line-height: 40px;
}
.action {
  margin: 5% 0 5% 50%;
  display: flex;
  justify-content: space-between;
}
.comment {
  margin: 5px;
  border-top: 1px solid #fcf;
}
.new-comment {
  display: flex;
  margin: 5px 0;
}
button {
  height: 30px;
  line-height: 30px;
  color: #fff;
  font-weight: bold;
}
#like {
  width: 40%;
  background-color: #f53076;
}
#comment {
  width: 40%;
  background-color: #ffb001;
}
#submit {
  width: 20%;
  background-color: #53cce9;
}
img {
  width: 30px;
  height: 30px;
  margin: 5px;
}
textarea {
  padding: 0 2px;
  border-radius: 10px;
  height: 25px;
  width: 75%;
  border: 2px solid #ffb001;
}
</style>
