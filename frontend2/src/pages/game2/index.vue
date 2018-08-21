<template>
  <div class="game">
    <div class="word">
      <img src="/static/img/game2/read.png"/>
      <span>{{ word }}</span>
    </div>
    <div class="picGroup">
      <img :key="pic.index" v-for="pic in pics" :isanswer="pic.isanswer" :src="pic.src" mode="aspectFit" @click="choice(pic)"/>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      word: 'hehei',
      pics: [
        {
          index: 1,
          isanswer: true,
          src: '/static/img/game2/cat1.jpg'
        },
        {
          index: 2,
          isanswer: false,
          src: '/static/img/game2/cat2.jpg'
        },
        {
          index: 3,
          isanswer: false,
          src: '/static/img/game2/cat3.jpg'
        },
        {
          index: 4,
          isanswer: false,
          src: '/static/img/game2/cat4.jpg'
        }
      ]
    }
  },
  methods: {
    choice(pic) {
      console.log(pic.isanswer);
      if (pic.isanswer === true) {
        wx.showModal({
          title: '选对啦!宝宝真棒！',
          content: '已完成该练习，是否退出~',
          cancelText: '再看看',
          confirmText: '退出',
          confirmColor: '#ffb001',
          success: function(res) {
            if (res.confirm) {
              wx.navigateBack({
                url: '../practice/main'
              })
            }
          }
        })
      } else {
        wx.showModal({
          title:'啊噢，就差一点点噢...',
          content: '再试一次吧~',
          cancelText: '不了',
          confirmText: '再试一次',
          confirmColor: '#ffb001',
          success: function(res) {
            if(res.cancel) {
              wx.navigateBack({
                url: '../practice/main'
              })
            }
          }
        })
      }
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
  width: 100%;
  text-align: center;
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
