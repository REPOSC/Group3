import changepwd from '@/components/user/changepwd'

describe('changepwd.vue', () => {
  it('test data() is function', () => {
    expect(typeof changepwd.data).toBe('function')
  })

  it('test defaultData of old_pwd', () => {
    const defaultData = changepwd.data()
    expect(defaultData.old_pwd).toBe('')
  })

  it('test defaultData of password', () => {
    const defaultData = changepwd.data()
    expect(defaultData.password).toBe('')
  })

  it('test defaultData of confirm_pwd', () => {
    const defaultData = changepwd.data()
    expect(defaultData.confirm_pwd).toBe('')
  })

  // it('test the old_pwd is ""', () => {
  //   const Constructor = Vue.extend(changepwd)
  //   const vm = new Constructor().$mount()
  //   vm.old_pwd = ''
  //   vm.password = '234'
  //   vm.confirm_pwd = '234'
  //   expect(vm.is_equal()).toBe(false)
  // })

  // it('test the password is ""', () => {
  //   const Constructor = Vue.extend(changepwd)
  //   const vm = new Constructor().$mount()
  //   vm.old_pwd = '123'
  //   vm.password = ''
  //   vm.confirm_pwd = '234'
  //   expect(vm.is_equal()).toBe(false)
  // })

  // it('test the confirm_pwd is ""', () => {
  //   const Constructor = Vue.extend(changepwd)
  //   const vm = new Constructor().$mount()
  //   vm.old_pwd = '123'
  //   vm.password = '234'
  //   vm.confirm_pwd = ''
  //   expect(vm.is_equal()).toBe(false)
  // })

  // it('test the confirm_pwd is not equal to password', () => {
  //   const Constructor = Vue.extend(changepwd)
  //   const vm = new Constructor().$mount()
  //   vm.old_pwd = '123'
  //   vm.password = '234'
  //   vm.confirm_pwd = '235'
  //   expect(vm.is_equal()).toBe(false)
  // })

  // it('test the confirm_pwd is equal to password', () => {
  //   const Constructor = Vue.extend(changepwd)
  //   const vm = new Constructor().$mount()
  //   vm.old_pwd = '123'
  //   vm.password = '234'
  //   vm.confirm_pwd = '234'
  //   expect(vm.is_equal()).toBe(true)
  // })
})
