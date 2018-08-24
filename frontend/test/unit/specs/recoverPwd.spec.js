import Vue from 'vue'
import recoverPwd from '@/components/stuManage/recoverPwd'

describe('recoverPwd.vue', () => {
  it('test data() is function', () => {
    expect(typeof recoverPwd.data).toBe('function')
  })

  it('test default of username', () => {
    const defaultData = recoverPwd.data()
    expect(defaultData.username).toBe('')
  })

  it('test default of password', () => {
    const defaultData = recoverPwd.data()
    expect(defaultData.password).toBe('')
  })

  it('test default of confirm_pwd', () => {
    const defaultData = recoverPwd.data()
    expect(defaultData.confirm_pwd).toBe('')
  })

  it('test input of username', () => {
    const Constructor = Vue.extend(recoverPwd)
    const vm = new Constructor().$mount()
    vm.username = '1234'
    expect(vm.username).toBe('1234')
  })
})
