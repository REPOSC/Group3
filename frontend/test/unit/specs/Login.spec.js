import Login from '@/components/Login.vue'

describe('Login', () => {
  it('测试data是函数', () => {
    expect(typeof Login.data).toBe('function')
  })
  it('测试data原始数据', () => {
    const defaultData = Login.data()
    expect(defaultData.account.username).toBe('')
    expect(defaultData.account.pwd).toBe('')
  })
})
