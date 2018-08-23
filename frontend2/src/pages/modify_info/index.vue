<template>
  <div class="info">
    <p class="title">修改头像</p>
    <div class="div">
      <div class="avatar">
        <img src="/static/img/avatar.jpg">
        <button class="upload">上传新头像</button>
      </div>
    </div>
    <p class="title">修改用户名</p>
    <div class="div">
      <div class="username">
        <p class="item">用户名</p>
        <input :value="username"/>
      </div>
    </div>
    <p class="title">修改密码</p>
    <div class="div">
      <div class="password">
        <p class="item">原密码</p>
        <input type="password" maxlength="15"/>
      </div>
      <div class="password">
        <p class="item">新密码</p>
        <input type="password" maxlength="15"/>
      </div>
      <div class="password">
        <p class="item">确认密码</p>
        <input type="password" maxlength="15"/>
      </div>
    </div>
    <button class="save" type="submit">保存修改</button>
  </div>
</template>

<script>
export default {
  data () {
    return {
      username: '小吉',
      password: '111111'
    }
  }
}
</script>

<style scoped>
button {
  color: #fff;
  height: 40px;
  line-height: 40px;
  font-size: 20px;
  margin: 30px 50px;
  border-radius: 10px;
}
p {
  width: 40%;
}
input {
  height: 30px;
  width: 60%;
  color: #000;
  line-height: 30px;
  border: 2px solid #53cce9;
  margin: 5px 50px;
}
img {
  width: 90px;
  height: 90px;
  border: 2px solid #ffb001;
  border-radius: 10px;
}
.info {
  font-size: 20px;
  color: #fff;
  margin: 10px 20px;
}
.div {
  width: 99%;
  margin: 5px auto;
  border: 2px solid #53cce9;
  border-radius: 10px;
}
.title {
  width: 98%;
  height: 40px;
  line-height: 40px;
  text-align: center;
  margin-top: 20px;
  padding-left: 10px;
  background-color: #ffb001;
  border-radius: 8px;
}
.avatar {
  width: 98%;
  height: 100px;
  line-height: 100px;
  margin: 10px auto;
  display: flex;
  padding-left: 20px;
}
.username {
  width: 98%;
  height: 50px;
  line-height: 50px;
  margin: 10px auto;
  display: flex;
  padding-left: 20px;
}
.password {
  width: 98%;
  height: 60px;
  line-height: 60px;
  display: flex;
  padding-left: 20px;
}
.item {
  height: 40px;
  line-height: 40px;
  text-align: center;
  background-color: #53cce9;
  border-radius: 10px;
  margin-top: 5px;
}
.upload {
  background-color: #53cce9;
}
.save {
  background-color: #ffb001;
}
</style>
