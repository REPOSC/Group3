import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)
export default new Vuex.Store({
  state: {
    user: false
  },
  mutations: {
    // 登录
    login () {
      this.state.user = true
    },
    // 退出
    logout (user) {
      this.state.user = false
    }
  }
})
