<template>
  <!--背景图-->

  <div >
    <!--login框，表单+tab标签页的组合-->
    <div class = "loginFrame">
      <form ref = "AccountForm"  rules = "rules" label-position = "left" label-width = "0px" class = "demo-ruleForm login-container">
        <div style="height:30px">会员账号</div>
        <input type = "text"  auto-complete = "off" placeholder = "请输入您的账号">{{username}}</input>
        <br/><br/>
        <div style="height:30px">新密码</div>
        <input type = "password"  auto-complete = "off" placeholder = "请输入密码">{{password}}</input>
        <br/><br/>
        <div style="height:30px">确认密码</div>
        <input type = "password"  auto-complete = "off" placeholder = "请输入密码">{{password}}</input>
        <br/><br/>
        <form-item style = "width:100%;">
          <el-button type = "primary" style = "width:100%;"  @click="submit" >确认修改</el-button>
        </form-item>
      </form>
    </div>
  </div>

</template>

<script>
  export default {
    data:{
      username:'',
      password:'',
    },
    methods:{
    }
  }

</script>

<style >

  .login-container {
    -webkit-border-radius: 5px;
    border-radius: 5px;
    -moz-border-radius: 5px;
    background-clip: padding-box;
    margin: 180px auto;
    width: 400px;
    padding: 35px 35px 15px 35px;
    background: #fff;
    border: 1px solid #eaeaea;
    box-shadow: 0 0 25px #cac6c6;

  }</style>
