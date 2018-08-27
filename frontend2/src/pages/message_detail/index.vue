<template>
  <div class="message-detail">
    <div class="record">
      <div class="user">
        <img :src="record.avatar" />
        <p class="username">{{ record.username }}</p>
      </div>
      <p class="content">{{ record.content }}
      </p>
      <div class="mes-info">
        <span>赞({{ record.likes }})</span>
        <span>评论({{ record.comments.length }})</span>
      </div>
      <div class="comment">
        <div v-for="comment in record.comments">
          <span class="username">{{ comment.username }}:</span>
          <p class="comment-content">{{ comment.content }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      record: {
        avatar: '/static/img/game2/cat1.jpg',
        username: '小吉',
        content: '今天我学了10个单词啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦',
        comments: [
          {
            username: 'cfl',
            content: 'so good'
          },
          {
            username: 'why',
            content: '今天我学了10个单词啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦啦'
          }
        ],
        likes: 0
      }
    }
  }
}
</script>

<style>
page {
  background-size: 100% 100%;
  background-image: url('https://daisy-donald.cn/image/back.jpg');
}
.record {
  width: 90%;
  margin: 4%;
  background-color: antiquewhite;
  border: 5px solid #53cce9;
  border-radius: 10px;
}
.content {
  height: 100px;
  text-overflow: -o-ellipsis-lastline;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  align-content: center;
  margin: auto 6px;
}
.user {
  display: flex;
}
.username {
  color: #53cce9;
  height: 40px;
  line-height: 40px;
}
.mes-info {
  float: right;
  color: #ffb100;
}
.comment {
  margin: 5px;
  border-top: 1px solid #fcf;
}
img {
  width: 30px;
  height: 30px;
  margin: 5px;
}
</style>
