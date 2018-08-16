<template>
  <!--背景图-->

  <div >
    <!--login框，表单+tab标签页的组合-->
    <div class = "loginFrame">
      <form ref = "AccountForm"  rules = "rules" label-position = "left" label-width = "0px" class = "demo-ruleForm login-container">

        <div style="height:30px ; float: left">会员账号</div>
        <input type = "text"  style="width:100px ;height:25px" auto-complete = "off" placeholder = "请输入您的账号">{{username}}
        <br/><br/>

        <div id = 'app' style="height:30px ; float: left" >等级选择</div>&nbsp;
        <select v-model="value" placeholder="请选择">
          <option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </option>
        </select>

        <br/><br/><br/><br/>
        <form-item style = "width:100%;">
          <button type = "primary" style = "width:100%;"  @click="submit" >确认修改</button>
        </form-item>
      </form>
    </div>
  </div>

</template>

<script>
export default {
  data() {
    return {
      options: [{
        value: '选项1',
        label: '等级1'
      }, {
        value: '选项2',
        label: '等级2'
      }, {
        value: '选项3',
        label: '等级3'
      }, {
        value: '选项4',
        label: '等级4'
      }, {
        value: '选项5',
        label: '等级5'
      }, {
        value: '选项6',
        label: '等级6'
      }, {
        value: '选项7',
        label: '等级7'
      }, {
        value: '选项8',
        label: '等级8'
      }, {
        value: '选项9',
        label: '等级9'
      }, {
        value: '选项10',
        label: '等级10'
      }, {
        value: '选项11',
        label: '等级11'
      }, {
        value: '选项12',
        label: '等级12'
      }
      ],
      value: ''
    }
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
