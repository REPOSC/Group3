<template>
  <div>
    <div class="title">
      <img src="/static/img/rainbow.png">
      <p>阅读拓展</p>
    </div>
    <div>
      <p class="item">文字作业描述</p>
      <div class="describe">{{ content }}</div>
    </div>
    <div>
      <p class="item">打卡内容</p>
      <div class="content"></div>
    </div>
    <div class="function">
      <button>上传作业</button>
      <button>打卡分享</button>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      content: '今天的作业是在画一幅画'
    }
  }
}
</script>

<style scoped>
img {
  width: 70px;
  height: 70px;
}
.title {
  height: 70px;
  line-height: 70px;
  text-align: center;
  display: flex;
  justify-content: center;
}
.describe {
  width: 80%;
  height: 100px;
  background-color: #01c758;
  border: 2px solid #27532c;
  border-radius: 10px;
  margin: 10px auto;
}
.content {
  width: 80%;
  height: 150px;
  background-color: #00c6af;
  border: 2px solid #10534b;
  border-radius: 10px;
  margin: 10px auto;
}
p {
  color: yellow;
  font-size: 25px;
  font-weight: bold;
  text-shadow: 2px 2px 3px #000;
}
.item {
  font-size: 20px;
  margin-left: 10%;
}
.function {
  width: 80%;
  display: flex;
  margin: 20px auto;
}
button {
  width: 35%;
  color: #53cce9;
  font-weight: bold;
  text-shadow: 2px 2px 3px #000;
  background-color: #ffb001;
}
</style>
