<template>
  <div class="me">
    <div class="my_info">
      <img src="/static/img/avatar.jpg">
      <p class="username">{{ username }}</p>
    </div>
    <button id="modify_info" @click="turnTo">修改资料</button>
    <button id="notice" @click="turnTo">系统消息</button>
    <button id="introduction" @click="turnTo">功能介绍</button>
    <button id="about_vron" @click="turnTo">关于弗恩英语</button>
    <button id="logout" @click="turnTo">退出登录</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '哈哈哈'
    }
  },
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
.me {
  padding-top: 30px;
  margin: 20px 50px;
}
.my_info {
  display: flex;
  text-align: center;
}
img {
  width: 70px;
  height: 70px;
  margin-left: 20px;
  border: 3px solid #ffb001;
  border-radius: 10px;
}
p {
  margin: 25px 40px;
  font-weight: bold;
}
#modify_info {
  color: #fff;
  background-color: #019dd6;
  margin-top: 40px;
}
#notice {
  color: #fff;
  background-color: #00c544;
  margin-top: 20px;
}
#introduction {
  color: #fff;
  background-color: #f67c30;
  margin-top: 20px;
}
#about_vron {
  color: #fff;
  background-color: #00fe90;
  margin-top: 20px;
}
#logout {
  color: #fff;
  background-color: #f53076;
  margin-top: 40px;
}
</style>
