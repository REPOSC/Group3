<template>
  <div>
    <div class="title">
      <img src="/static/img/rainbow.png">
      <p>课后练习</p>
    </div>
    <div class="game" @click="turnTo">
      <button id="game1">连线游戏</button>
      <button id="game2">单词识别</button>
      <button id="game3">趣味拼图</button>
      <button id="game4">选词填空</button>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    turnTo(e) {
      wx.navigateTo({
        url: '/pages/' + e.target.id + '/main'
      })
    }
  }
}
</script>

<style scoped>
page {
  background-image: url('https://thumbnail0.baidupcs.com/thumbnail/208d7bfe35c662f32a88a1fe206d44e9?fid=3911358295-250528-398515735348763&time=1534424400&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-mj%2BYVt%2Fbo9W%2BSqMC7ImwhtUDIcs%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=5285426163203658882&dp-callid=0&size=c710_u400&quality=100&vuk=-&ft=video');
}
button {
  width: 60%;
  color: #fff;
  font-weight: bold;
  margin: 30px auto;
}
.title {
  height: 70px;
  line-height: 70px;
  text-align: center;
  display: flex;
  justify-content: center;
}
p {
  color: yellow;
  font-size: 25px;
  font-weight: bold;
  text-shadow: 2px 2px 3px #000;
}
img {
  width: 70px;
  height: 70px;
}
.game {
  margin: 50px auto;
}
#game1 {
  background-color: #019dd6;
}
#game2 {
  background-color: #f67c30;
}
#game3 {
  background-color: #00c544;
}
#game4 {
  background-color: #f53076;
}
</style>
