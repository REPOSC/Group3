<template>
  <div class="layout">
    <Layout>
      <Sider>
        <Menu>
          <a class="info">弗恩英语管理平台</a>
          <Submenu name="1">
            <template slot="title">
              <Icon type="md-person" />
              学生管理
            </template>
            <MenuItem name="1-1">创建账号</MenuItem>
            <MenuItem name="1-2">设置等级</MenuItem>
            <MenuItem name="1-3">找回密码</MenuItem>
          </Submenu>

          <Submenu name="2">
            <template slot="title">
              <Icon type="md-analytics" />
              数据统计
            </template>
            <MenuItem name="2-1">书本数据统计</MenuItem>
            <MenuItem name="2-2">学生数据统计</MenuItem>
          </Submenu>

          <Submenu name="3">
            <template slot="title">
              <Icon type="md-desktop" />
              后台账户管理
            </template>
            <MenuItem name="3-1">添加账户</MenuItem>
            <MenuItem name="3-2">修改密码</MenuItem>
            <MenuItem name="3-3">删除账户</MenuItem>
          </Submenu>

          <Submenu name="4">
            <template slot="title">
              <Icon type="md-settings" />
              教学内容设置
            </template>
            <MenuItem name="4-1">添加书籍</MenuItem>
            <MenuItem name="4-2">管理书籍</MenuItem>
            <MenuItem name="4-3">添加功能介绍视频</MenuItem>
          </Submenu>

          <Submenu name="5">
            <template slot="title">
              <Icon type="md-notifications" />
              消息公告
            </template>
            <MenuItem name="5-1">群发消息</MenuItem>
            <MenuItem name="5-2">私发消息</MenuItem>
            <MenuItem name="5-3">历史消息</MenuItem>
          </Submenu>

          <Submenu name="6">
            <template slot="title">
              <Icon type="md-contacts" />
              查看社群
            </template>
            <MenuItem name="6-1">级别1</MenuItem>
            <MenuItem name="6-2">级别2</MenuItem>
            <MenuItem name="6-3">级别3</MenuItem>
            <MenuItem name="6-4">级别4</MenuItem>
          </Submenu>

        </Menu>
      </Sider>
    </Layout>
  </div>
</template>

<script>
export default {
  meta: {
    title: '弗恩英语'
  }
}
</script>
<style>
.info {
  font-size: 25px;
  color: black;
}
</style>
