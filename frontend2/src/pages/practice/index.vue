<template>
  <div>
    <div class="title">
      <img src="https://daisy-donald.cn/image/rainbow.png">
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
  data: function() {
    return {
      booknumber: null
    }
  },
  onLoad: function(status) {
    this.booknumber = status.book
  },
  methods: {
    turnTo(e) {
      wx.navigateTo({
        url: '/pages/' + e.target.id + '/main?booknumber=' + this.booknumber
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

.game button {
  color: #fff;
  width: 75%;
  height: 50px;
  line-height: 50px;
  font-size: 20px;
  font-weight: bold;
  margin: 30px auto;
}

.title {
  height: 70px;
  line-height: 70px;
  margin: 30px;
  text-align: center;
  display: flex;
  justify-content: center;
}

p {
  color: yellow;
  font-size: 30px;
  font-weight: bold;
  text-shadow: 2px 2px 3px #000;
}

img {
  width: 70px;
  height: 70px;
}

.game {
  margin: 60px auto;
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
