<template>
  <div class="my-message">
    <div class="message" :key="message.id" v-for="message in messages">
      <div class="like" v-if="message.likes">
        <img :src="message.avatar" />
        <p>
          <span>{{ message.username }}</span>
          赞了你的消息
        </p>
        <span class="detail_btn" @click="to_detail(message)">详情</span>
      </div>
      <div class="comment" v-if="message.comment" >
        <div class="user">
          <img :src="message.avatar" />
          <p>
            <span>{{ message.username }}</span>评论：
          </p>
          <span class="detail_btn" @click="to_detail(message)">详情</span>
        </div>
        <br>
        <p class="content">{{ message.comment_content }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      messages: [
        {
          id: 1,
          avatar: '/static/img/game2/cat1.jpg',
          username: '小吉',
          likes: false,
          comment: true,
          comment_content: '我是小蒜啦安啦啦啊啊啊啊啊啊阿啊啊啊'
        },
        {
          id: 1,
          avatar: '/static/img/game2/cat1.jpg',
          username: '小吉',
          likes: true,
          comments: false,
          comment_content: ''
        }
      ]
    }
  },
  methods: {
    to_detail(message) {
      wx.navigateTo({
        url: '../message_detail/main'
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

.my-message {
  margin: 10px 10px;
}

.like {
  display: flex;
  height: 100px;
  margin: 4px;
  background-color: antiquewhite;
  border: 2px solid #ffb001;
}

like p {
  width: 100%;
  height: 40px;
  line-height: 40px;
  font-size: 20px;
  word-wrap: break-word;
}

.comment {
  height: 100px;
  margin: 4px;
  background-color: antiquewhite;
  border: 2px solid #53cce9;
}

.user {
  display: flex;
}

.detail_btn {
  position: absolute;
  color: #ffb001;
  right: 19px;
}

.content {
  text-overflow: -o-ellipsis-lastline;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  align-content: center;
  margin: auto 6px;
}

img {
  width: 30px;
  height: 30px;
  margin: 5px;
}
</style>
