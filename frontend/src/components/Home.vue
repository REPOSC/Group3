<template>
  <el-row class="container">
    <el-col :span="24" class="topbar-wrap">
      <div class="topbar-logo topbar-btn">
        <a href="/"><img src="../assets/logo.png"></a>
      </div>
      <div class="topbar-logos" v-show="!collapsed">
        <a href="/"><img src="../assets/logotxt.png"></a>
      </div>
      <div class="topbar-title">
        <span>后台管理系统</span>
      </div>
      <div class="topbar-account topbar-btn">
        <el-dropdown trigger="click">
          <span class="el-dropdown-link userinfo-inner">
            <i class="iconfont icon-user"></i> {{nickname}}
            <i class="iconfont icon-down"></i>
          </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item>
              <div @click="jumpTo('/user/profile')">
                <span>个人信息</span>
              </div>
            </el-dropdown-item>
            <el-dropdown-item>
              <div @click="jumpTo('/user/changepwd')">
                <span>修改密码</span>
              </div>
            </el-dropdown-item>
            <el-dropdown-item divided @click.native="logout">
              退出登录</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </div>
    </el-col>
    <el-col :span="24" class="main">
      <aside :class="{showSidebar:!collapsed}">
        <div class="menu-toggle" @click.prevent="collapse">
          <i class="iconfont icon-menufold" v-show="!collapsed"></i>
          <i class="iconfont icon-menuunfold" v-show="collapsed"></i>
        </div>
        <el-menu
          :default-active="defaultActiveIndex"
          router :collapse="collapsed"
          @select="handleSelect"
        >
          <template
            v-for="(item,index) in $router.options.routes"
            v-if="item.menuShow"
          >
            <el-submenu v-if="!item.leaf" :index="index+''">
              <template slot="title">
                <i :class="item.iconCls"></i>
                <span slot="title">{{item.name}}</span>
              </template>
              <el-menu-item
                v-for="term in item.children"
                :key="term.path"
                :index="term.path"
                v-if="term.menuShow"
                :class="$route.path===term.path?'is-active':''">
                <i :class="term.iconCls"></i>
                <span slot="title">{{term.name}}</span>
              </el-menu-item>
            </el-submenu>
            <el-menu-item
              v-else-if="item.leaf&&item.children&&item.children.length"
              :index="item.children[0].path"
              :class="$route.path===item.children[0].path?'is-active':''">
              <i :class="item.iconCls"></i>
              <span slot="title">{{item.children[0].name}}</span>
            </el-menu-item>
          </template>
        </el-menu>
      </aside>
      <!--右侧内容区-->
      <section class="content-container">
        <div class="grid-content bg-purple-light">
          <el-col :span="24" class="content-wrapper">
            <transition name="fade" mode="out-in">
              <router-view></router-view>
            </transition>
          </el-col>
        </div>
      </section>
    </el-col>
  </el-row>
</template>

<script>
export default {
  name: 'home',
  data() {
    return {
      defaultActiveIndex: '0',
      nickname: '',
      collapsed: false
    }
  },
  methods: {
    handleSelect(index) {
      this.defaultActiveIndex = index
    },
    collapse: function() {
      this.collapsed = !this.collapsed
    },
    jumpTo(url) {
      this.defaultActiveIndex = url
      this.$router.push(url)
    },
    logout() {
      let that = this
      this.$confirm('确认退出吗?', '提示', {
        confirmButtonClass: 'el-button--warning'
      })
        .then(() => {
          that.$router.push('/login')
        })
        .catch(() => {})
    }
  }
}
</script>
<style scoped lang="scss">

.container {
  position: absolute;
  top: 0;
  bottom: 0;
  width: 100%;

  .topbar-wrap {
    height: 50px;
    line-height: 50px;
    background: #373d41;
    padding: 0;

    .topbar-btn {
      color: #ffffff;
    }

    .topbar-btn:hover {
      color: #f5ff7f;
    }

    .topbar-logo {
      float: left;
      width: 59px;
      line-height: 26px;
    }

    .topbar-logos {
      float: left;
      width: 120px;
      line-height: 26px;
    }

    .topbar-logo img,

    .topbar-logos img {
      height: 40px;
      margin-top: 5px;
      margin-left: 2px;
    }

    .topbar-title {
      float: left;
      text-align: left;
      width: 200px;
      padding-left: 10px;
      border-left: 1px solid #060606;
    }

    .topbar-account {
      float: right;
      padding-right: 12px;
    }

    .userinfo-inner {
      cursor: pointer;
      color: #fff;
      padding-left: 10px;
    }
  }

  .main {
    display: -webkit-box;
    display: -webkit-flex;
    display: -ms-flexbox;
    display: flex;
    position: absolute;
    top: 50px;
    bottom: 0;
    overflow: hidden;
  }

  aside {
    min-width: 50px;
    background: #333744;

    &::-webkit-scrollbar {
      display: none;
    }

    &.showSidebar {
      overflow-x: hidden;
      overflow-y: auto;
    }

    .el-menu {
      height: 100%;
      height: -moz-calc(100% - 80px);
      height: -webkit-calc(100% - 80px);
      height: calc(100% - 80px);
      border-radius: 0;
      background-color: #333744;
      border-right: 0;
    }

    .el-submenu .el-menu-item {
      min-width: 60px;
    }

    .el-menu {
      width: 180px;
      text-align: left;
    }

    .el-menu--collapse {
      width: 60px;
    }

    .el-menu .el-menu-item,

    .el-submenu .el-submenu__title {
      height: 46px;
      line-height: 46px;
      color: white;
      text-align: left;
    }

    .el-menu-item:hover,

    .el-submenu .el-menu-item:hover,

    .el-submenu__title:hover {
      background-color: #7ed2df;
    }
  }

  .menu-toggle {
    background: #4a5064;
    text-align: center;
    color: white;
    height: 26px;
    line-height: 30px;
  }

  .content-container {
    background: #fff;
    flex: 1;
    overflow-y: auto;
    padding: 10px 10px 1px;
    .content-wrapper {
      background-color: #fff;
      box-sizing: border-box;
    }
  }
}
</style>
