// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import '@/assets/iconfont.css'
import '@/assets/styles/main.css'
import * as tools from './components/Tools/Tools'
Vue.config.productionTip = false

router.beforeEach((to, from, next) => {
  if (from.path === '/login') {
    window.location.reload()
  }
  if (to.path === '/login') {
    tools.initpage()
    next()
  } else {
    if (window.sessionStorage.is_load === 'true') {
      if (
        to.path === '/memberManager/addMember' ||
        to.path === '/memberManager/changePwd' ||
        to.path === '/memberManager/removeMember'
      ) {
        if (window.sessionStorage.is_superuser === 'true') {
          next()
        } else {
          next(from.path)
        }
      } else {
        next()
      }
    } else {
      tools.initpage()
      next({ path: '/login' })
    }
  }
})

Vue.use(ElementUI)
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
