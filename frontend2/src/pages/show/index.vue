<template>
  <div class="div">
    <button id="btn1">亲子阅读指导</button>
    <button id="btn2">E-Book</button>
    <button id="btn3">中英文讲解</button>
    <button id="btn4">课后练习</button>
    <button id="btn5">阅读拓展</button>
    <div class="bottom">
      <div class="function" @click="toCommunity">
        <img src="/static/img/man.png">
        <p>社群</p>
      </div>
      <div class="function" @click="toMe">
        <img src="/static/img/man.png">
        <p>我的</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    toCommunity () {

    },
    toMe () {

    }
  }
}
</script>

<style scoped>
page {
  background-image: url('https://thumbnail0.baidupcs.com/thumbnail/208d7bfe35c662f32a88a1fe206d44e9?fid=3911358295-250528-398515735348763&time=1534424400&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-mj%2BYVt%2Fbo9W%2BSqMC7ImwhtUDIcs%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=5285426163203658882&dp-callid=0&size=c710_u400&quality=100&vuk=-&ft=video');
}
.div {
  padding: 60px 50px;
}
button {
  color: #fef;
  font-weight: bold;
  margin: 20px auto;
}
.bottom {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}
.function {
  text-align: center;
}
img {
  width: 70px;
  height: 70px;
}
p {
  color: #ffb001;
  font-size: 20px;
  font-weight: bold;
}
#btn1 {
  background-color: #019dd6;
}
#btn2 {
  background-color: #f67c30;
}
#btn3 {
  background-color: #00c544;
}
#btn4 {
  background-color: #f53076;
}
#btn5 {
  background-color: #00fe90;
}
</style>
