import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import stuManagecreateAccount from '@/components/stuManage/createAccount'
import stuManagerecoverPwd from '@/components/stuManage/recoverPwd'
import stuManagesetLevel from '@/components/stuManage/setLevel'
import stuManagelist from '@/components/stuManage/list'
import memberadd from '@/components/memberManager/addMember'
import memberchangePwd from '@/components/memberManager/changePwd'
import memberremove from '@/components/memberManager/removeMember'
import BookList from '@/components/book/list'
import Bookcategory from '@/components/bookcategory/list'
import video from '@/components/video/list'
import UserChangePwd from '@/components/user/changepwd'
import UserProfile from '@/components/user/profile'
import SendMessage from '@/components/group/sendmessage'
import groupdzone from '@/components/group/dzone'
import StudentWatch from '@/components/stuManage/watch'
Vue.use(Router)
const Login = resolve => require(['@/components/Login'], resolve)
let router = new Router({
  routes: [{
    path: '',
    component: Home
  },
  {
    path: '/Login',
    name: '登录',
    component: Login
  },
  {
    path: '',
    name: '主页',
    component: Home,
    redirect: '/',
    leaf: true, // 只有一个节点
    menuShow: true,
    iconCls: 'iconfont icon-home', // 图标样式class
    children: [{
      path: '/',
      name: '首页',
      menuShow: true,
      component: Home
    }]
  },
  {
    path: '/',
    component: Home,
    name: '学生管理',
    menuShow: true,
    iconCls: 'iconfont icon-setting1',
    children: [{
      path: '/stuManage/createAccount',
      component: stuManagecreateAccount,
      name: '创建账号',
      menuShow: true
    },
    {
      path: '/stuManage/profile',
      component: stuManagesetLevel,
      name: '设置等级',
      menuShow: true
    },
    {
      path: '/stuManage/changepwd',
      component: stuManagerecoverPwd,
      name: '找回密码',
      menuShow: true
    },
    {
      path: '/student/watch',
      component: StudentWatch,
      name: '查看学生详情',
      menuShow: false
    }
    ]
  },
  {
    path: '/',
    component: Home,
    name: '数据统计',
    menuShow: true,
    iconCls: 'iconfont icon-setting1',
    children: [{
      path: '/bookcategory/list',
      component: Bookcategory,
      name: '书本数据统计',
      menuShow: true
    },
    {
      path: '/stuManager/list',
      component: stuManagelist,
      name: '学生数据统计',
      menuShow: true
    }
    ]
  },
  {
    path: '/',
    component: Home,
    name: '教学内容设置',
    menuShow: true,
    iconCls: 'iconfont icon-books',
    children: [{
      path: '/book/list',
      component: BookList,
      name: '添加书籍',
      menuShow: true
    }]
  },
  {
    path: '/',
    name: '功能视频',
    component: Home,
    redirect: '/',
    leaf: true, // 只有一个节点
    menuShow: true,
    iconCls: 'iconfont icon-home', // 图标样式class
    children: [{
      path: '/video/list',
      name: '添加功能介绍视频',
      menuShow: true,
      component: video
    }]
  },
  {
    path: '/',
    component: Home,
    name: '消息公告',
    menuShow: true,
    iconCls: 'iconfont icon-setting1',
    children: [{
      path: '/group/sendmessage',
      component: SendMessage,
      name: '群发消息',
      menuShow: true
    }]
  },
  {
    path: '/',
    name: '社群',
    component: Home,
    menuShow: true,
    iconCls: 'iconfont icon-home', // 图标样式class
    children: [{
      path: '/group/dzone',
      name: '查看社群消息',
      menuShow: true,
      component: groupdzone
    }]
  },
  {
    path: '/',
    component: Home,
    name: '设置',
    menuShow: true,
    iconCls: 'iconfont icon-setting1',
    children: [{
      path: '/user/profile',
      component: UserProfile,
      name: '个人信息',
      menuShow: true
    },
    {
      path: '/user/changePwd',
      component: UserChangePwd,
      name: '修改密码',
      menuShow: true
    }
    ]
  },
  {
    path: '/',
    component: Home,
    name: '管理员账户管理',
    menuShow: judge(),
    iconCls: 'iconfont icon-setting1',
    children: [{
      path: '/memberManager/addMember',
      component: memberadd,
      name: '添加账户',
      menuShow: true
    },
    {
      path: '/memberManager/changePwd',
      component: memberchangePwd,
      name: '修改密码',
      menuShow: true
    },
    {
      path: '/memberManager/removeMember',
      component: memberremove,
      name: '删除账户',
      menuShow: true
    }
    ]
  }
  ]
})

function judge() {
  if (window.sessionStorage.is_superuser === 'true') {
    return true
  } else {
    return false
  }
}

export default router
