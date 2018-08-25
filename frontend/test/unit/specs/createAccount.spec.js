import createAccount from '@/components/stuManage/createAccount'

describe('createAccount.vue', () => {
  it('test data() is function', () => {
    expect(typeof createAccount.data).toBe('function')
  })

  it('test default of options', () => {
    const defaultData = createAccount.data()
    expect(defaultData.options.length).toBe(0)
  })

  it('test default of tableData', () => {
    const defaultData = createAccount.data()
    expect(defaultData.tableData.length).toBe(0)
  })

  it('test default of number', () => {
    const defaultData = createAccount.data()
    expect(defaultData.number).toBe(1)
  })
})
