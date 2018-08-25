import Home from '@/components/Home'

describe('Home.vue', () => {
  it('test data() is function', () => {
    expect(typeof Home.data).toBe('function')
  })

  it('test default of defaultActiveIndex', () => {
    const defaultData = Home.data()
    expect(defaultData.defaultActiveIndex).toBe('0')
  })

  it('test default of nickname', () => {
    const defaultData = Home.data()
    expect(defaultData.nickname).toBe('')
  })

  it('test default of collapsed', () => {
    const defaultData = Home.data()
    expect(defaultData.collapsed).toBe(false)
  })

  // it('test the status change of collapse', () => {
  //   const Constructor = Vue.extend(Home)
  //   const vm = new Constructor().$mount()
  //   vm.collapsed = true
  //   vm.collapse()
  //   expect(vm.collapsed).toBe(false)
  // })
})
