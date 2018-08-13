<template>
  <div>
    <h3>弗恩英语教学管理系统</h3>
    <el-col :span="12">
      <el-menu
      class="el-menu-vertical-demo"
      @open="handleOpen"
      @close="handleClose">

      <el-submenu index="1">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>学生管理</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="1-1">创建账号</el-menu-item>
          <el-menu-item index="1-2">设置等级</el-menu-item>
          <el-menu-item index="1-3">找回密码</el-menu-item>
        </el-menu-item-group>
      </el-submenu>

      <el-submenu index="2">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>数据统计</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="2-1">学生数据</el-menu-item>
          <el-menu-item index="2-2">书籍数据</el-menu-item>
        </el-menu-item-group>
      </el-submenu>

      <el-submenu index="3">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>账户管理</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="3-1">添加账户</el-menu-item>
          <el-menu-item index="3-2">修改密码</el-menu-item>
          <el-menu-item index="3-3">删除账户</el-menu-item>
        </el-menu-item-group>
      </el-submenu>

      <el-menu-item index="4">
        <i class="el-icon-location"></i>
        <span>设置功能介绍视频</span>
      </el-menu-item>

      <el-submenu index="5">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>消息公告</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="5-1">群发消息</el-menu-item>
          <el-menu-item index="5-2">私发消息</el-menu-item>
          <el-menu-item index="5-3">历史消息</el-menu-item>
        </el-menu-item-group>
      </el-submenu>

      <el-menu-item index="6">
        <i class="el-icon-location"></i>
        <span>查看社群</span>
      </el-menu-item>

      <el-submenu index="7">
        <template slot="title">
          <i class="el-icon-location"></i>
          <span>个人设置</span>
        </template>
        <el-menu-item-group>
          <el-menu-item index="7-1">个人信息</el-menu-item>
          <el-menu-item index="7-2">修改密码</el-menu-item>
        </el-menu-item-group>
      </el-submenu>

    </el-menu>
  </el-col>
</div>
</template>

<script>
export default {

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
div {
  width: 40%;
}
h3 {
  margin: 3px 3px 3px 3px;
}
</style>
