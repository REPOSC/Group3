<template>
  <div class="game">
    <div class="word">
      <i-row>
        <i-col span="4" offset="6">
          <img src="/static/img/game2/read.png"/>
        </i-col>
        <i-col span="7" offset="1">
          <span>{{ word }}</span>
        </i-col>
      </i-row>
    </div>
    <div class="picGroup">
      <img :key="pic.index" v-for="pic in pics" :src="pic.src" mode="aspectFit"/>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      word: 'dark',
      pics: [
        {
          index: 1,
          src: '/static/img/game2/cat1.jpg'
        },
        {
          index: 2,
          src: '/static/img/game2/cat2.jpg'
        },
        {
          index: 3,
          src: '/static/img/game2/cat3.jpg'
        },
        {
          index: 4,
          src: '/static/img/game2/cat4.jpg'
        }
      ]
    }
  }
}
</script>

<style>
page {
  background-size: 100% 100%;
  background-image: url('https://thumbnail0.baidupcs.com/thumbnail/208d7bfe35c662f32a88a1fe206d44e9?fid=3911358295-250528-398515735348763&time=1534424400&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-mj%2BYVt%2Fbo9W%2BSqMC7ImwhtUDIcs%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=5285426163203658882&dp-callid=0&size=c710_u400&quality=100&vuk=-&ft=video');
}
.game {
  margin-top: 30px;
}
.word {
  padding: 35px;
}
.word span {
  display: inline-block;
  font-size: 35px;
  font-weight: bolder;
  color: #ffb001;
  vertical-align: middle;
}
.word img {
  display: inline-block;
  width: 50px;
  height: 50px;
  vertical-align: middle;
}
.picGroup {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  margin: 20px;
}
.picGroup img{
  width: 40%;
  height: 100px;
  margin: 10px auto;
  overflow: hidden;
  border: 5px solid #ffb001;
  padding: 5px;
  background-color: white;
  border-radius: 10%;
}
</style>
