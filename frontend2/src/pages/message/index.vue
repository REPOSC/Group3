<template>
  <div>
    <div class="like" :key="like.id" v-for="like in likes">
      <img :src="like.avatar"/>
      <p><span>{{ like.username }}</span>赞了你</p>
    </div>
    <div class="comment" :key="comment.id" v-for="comment in comments">
      <div class="user">
        <img :src="comment.avatar"/>
        <p><span>{{ like.username }}</span>评论了你：</p>
        <a>回复</a>
      </div>
      <br><p class="content">{{ comment.content }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      likes: [
        {
          id: 1,
          avatar: '/static/img/game2/cat1.jpg',
          username: '小吉'
        },
        {
          id: 2,
          avatar: '/static/img/game2/cat2.jpg',
          username: '小蒜'
        },
        {
          id: 3,
          avatar: '/static/img/game2/cat3.jpg',
          username: '小可'
        }
      ],
      comments: [
        {
          id: 1,
          avatar: '/static/img/game2/cat1.jpg',
          username: '小吉',
          content: '我是小吉'
        },
        {
          id: 2,
          avatar: '/static/img/game2/cat2.jpg',
          username: '小蒜',
          content: '我是小蒜'
        },
        {
          id: 3,
          avatar: '/static/img/game2/cat3.jpg',
          username: '小可',
          content: '我是小可'
        }
      ]
    }
  }
}
</script>

<style scoped>
.like {
  display: flex;
  border-bottom: 5px solid #ffb001;
}
like p {
  width: 100%;
  height: 40px;
  line-height: 40px;
  font-size: 20px;
  word-wrap: break-word;
}
.comment {
  border-bottom: 5px solid #53cce9;
}
.user {
  display: flex;
}
.content {
  word-wrap: break-word;
}
a {
  position: absolute;
  right: 5px;
  color: blue;
}
img {
  width: 30px;
  height: 30px;
  margin: 5px;
}
</style>
