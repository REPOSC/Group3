import Vue from 'vue'
import Dashboard from '@/components/Dashboard'

describe('Dashboard.vue', () => {
  it('test data() is function', () => {
    expect(typeof Dashboard.data).toBe('function')
  })

  it('test default of oldpassword', () => {
    const defaultData = Dashboard.data()
    expect(defaultData.form.oldPwd).toBe('')
  })

  it('test default of password', () => {
    const defaultData = Dashboard.data()
    expect(defaultData.form.newPwd).toBe('')
  })

  it('test default of confirmPwd', () => {
    const defaultData = Dashboard.data()
    expect(defaultData.form.confirmPwd).toBe('')
  })

  it('test input of oldpassword', () => {
    const Constructor = Vue.extend(Dashboard)
    const vm = new Constructor().$mount()
    vm.form.oldPwd = '1234'
    expect(vm.form.oldPwd).toBe('1234')
  })
})
