<template>
  <div class="matching">
    <!-- <p class="game_name">连线游戏</p> -->
    <div class="content">
      <div class="words">
        <span v-for="word in words" :key="word.index">{{ word.text }}</span>
      </div>
      <div class="pictures">
        <img :key="picture.index" v-for="picture in pictures" :src="picture.src" mode="aspectFit" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      words: [
        {
          index: 1,
          text: 'apple'
        },
        {
          index: 2,
          text: 'banana'
        },
        {
          index: 3,
          text: 'cherry'
        },
        {
          index: 4,
          text: 'orange'
        }
      ],
      pictures: [
        {
          index: 1,
          src: '/static/img/game1/apple.jpg'
        },
        {
          index: 2,
          src: '/static/img/game1/banana.jpg'
        },
        {
          index: 3,
          src: '/static/img/game1/cherry.jpg'
        },
        {
          index: 4,
          src: '/static/img/game1/orange.jpg'
        }
      ]
    }
  }
}
</script>

<style scoped>
page {
  background-size: 100% 100%;
  background-image: url('https://thumbnail0.baidupcs.com/thumbnail/208d7bfe35c662f32a88a1fe206d44e9?fid=3911358295-250528-398515735348763&time=1534424400&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-mj%2BYVt%2Fbo9W%2BSqMC7ImwhtUDIcs%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=5285426163203658882&dp-callid=0&size=c710_u400&quality=100&vuk=-&ft=video');
}
.content {
  display: flex;
  justify-content: space-between;
  padding: 20px 20px;
  margin: 10px 10px;
}
.words,
.pictures {
  width: 40%;
}
.words span {
  color: #fff;
  font-size: 25px;
  height: 55px;
  width: 120px;
  line-height: 50px;
  display: inline-block;
  text-align: center;
  background-color: #ffb001;
  margin: 30px auto;
  border-radius: 10px;
}
.pictures img {
  margin: 10px 50px;
  width: 80px;
  height: 80px;
  border: 5px solid #ffb001;
  border-radius: 10px;
}
</style>
