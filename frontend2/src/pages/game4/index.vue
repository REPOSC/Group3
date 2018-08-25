<template>
  <div class="game">
    <i-icon type="customerservice" @click="playsound"/>
    <div class="picGroup">
      <img :key="pic.index" v-for="pic in pics" :isanswer="pic.isanswer" :src="pic.src" mode="aspectFit" @click="choice(pic)" />
    </div>
  </div>
</template>

<script>
export default {
  onLoad: function(status) {
    this.booknumber = status.booknumber
    this.username = status.username
  },
  onShow: function() {
    this.init()
  },
  data() {
    return {
      audio: null,
      picture: null,
      username: null,
      booknumber: null
    }
  },
  methods: {
    init() {},
    choice(pic) {
      console.log(pic.isanswer)
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
          title: '啊噢，就差一点点噢...',
          content: '再试一次吧~',
          cancelText: '不了',
          confirmText: '再试一次',
          confirmColor: '#ffb001',
          success: function(res) {
            if (res.cancel) {
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
  background-image: url('https://daisy-donald.cn/image/back.jpg');
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
.picGroup img {
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
