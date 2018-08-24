import Vue from 'vue'
import Login from '@/components/Login'

describe('Login.vue', () => {
  it('test data() is function', () => {
    expect(typeof Login.data).toBe('function')
  })

  it('test default of username', () => {
    const defaultData = Login.data()
    expect(defaultData.account.username).toBe('100001')
  })

  it('test default of password', () => {
    const defaultData = Login.data()
    expect(defaultData.account.pwd).toBe('111111')
  })

  it('test input of username', () => {
    const Constructor = Vue.extend(Login)
    const vm = new Constructor().$mount()
    vm.account.username = '1234'
    expect(vm.account.username).toBe('1234')
  })
})
