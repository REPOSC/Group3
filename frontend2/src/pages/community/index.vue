<template>
  <div class="container">
    <div class="record" v-for="(record, id) in records">
      <div class="user">
        <img :src="record.avatar" />
        <p class="username">
          <span v-if="id === -1">id</span>{{ record.username }}
        </p>
      </div>
      <p class="content">{{ record.content }}</p>
      <div class="action">
        <button id="like" @click="like(record)">赞
          <span v-if="record.liked === false"></span>
          <span v-if="record.likes !== 0">{{ record.likes }}</span>
        </button>
        <button id="comment" @click="comment(record)">{{ record.comment_info }}</button>
      </div>
      <div class="comment">
        <p v-for="comment in record.comments">
          <span class="username">{{ comment.username }}</span>
          : {{ comment.content }}
        </p>
        <div class="new-comment" v-if="record.commented">
          <textarea v-model="record.newcomment" />
          <button id="submit" @click="submit(record)">发送</button>
        </div>
      </div>
    </div>
    <div class="function">
      <div @click="toMessage">
        <img src="/static/img/tabbar_icon/yellow-mes.png" />
        <span>消息</span>
      </div>
      <div @click="toRankinglist">
        <img src="/static/img/tabbar_icon/yellow-rank.png" />
        <span>排行榜</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      comment_user: '小可',
      now_comment_record: '',
      username: null,
      level: null,
      records: [
        {
          id: 0,
          avatar: '/static/img/game2/cat1.jpg',
          username: '小吉',
          content:
            '今天我学了10个单词,啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿绿',
          comments: [],
          likes: 0,
          liked: false,
          newcomment: '',
          commented: false,
          comment_info: '评论'
        },
        {
          id: 1,
          avatar: '/static/img/game2/cat2.jpg',
          username: '小蒜',
          content: '今天我学了8个单词',
          comments: [],
          likes: 0,
          liked: false,
          newcomment: '',
          commented: false,
          comment_info: '评论'
        },
        {
          id: 2,
          avatar: '/static/img/game2/cat3.jpg',
          username: '小可',
          content: '今天我学了6个单词',
          comments: [],
          likes: 0,
          liked: false,
          newcomment: '',
          commented: false,
          comment_info: '评论'
        }
      ]
    }
  },
  onLoad: function(status) {
    this.username = status.username
    this.level = status.level
  },
  methods: {
    like(record) {
      if (record.liked === false) {
        record.likes += 1
      } else {
        record.likes -= 1
      }
      record.liked = !record.liked
    },
    comment(record) {
      if (record.commented === true) {
        record.comment_info = '评论'
        record.commented = false
        this.now_comment_record = ''
      } else {
        if (this.now_comment_record !== '') {
          this.records[this.now_comment_record].comment_info = '评论'
          this.records[this.now_comment_record].commented = false
        }
        record.comment_info = '取消'
        record.commented = true
        this.now_comment_record = record.id
      }
    },
    is_empty(record) {
      if (record.newcomment !== '') {
        return false
      }
      return true
    },
    submit(record) {
      if (this.is_empty(record)) {
        wx.showToast({
          title: '请输入评论内容',
          icon: 'none',
          duration: 1000,
          mask: true
        })
      } else {
        record.comments.push({
          username: this.comment_user,
          content: record.newcomment
        })
        record.commented = false
        record.comment_info = '评论'
        record.newcomment = ''
        this.now_comment_record = ''
      }
    },
    toMessage() {
      wx.navigateTo({
        url: '/pages/message/main?username=' + this.username
      })
    },
    toRankinglist() {
      wx.navigateTo({
        url:
          '/pages/Rankinglist/main?username=' +
          this.username +
          '&level=' +
          this.level
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
.content {
  margin: 0 5px;
  text-align: justify;
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
  margin: 5% 0 5% 40%;
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
  width: 25%;
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
  width: 70%;
  border: 2px solid #ffb001;
}
</style>
