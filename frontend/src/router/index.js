import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import createAccount from '@/components/stuManage/createAccount'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
      meta: {
        title: '主页'
      }
    },
    {
      path: '/stuManage/createAccount',
      name: 'createAccount',
      component: createAccount,
      meta: {
        title: '创建用户'
      }
    }
  ]
})
