import changepwd from '@/components/user/changepwd.vue'

describe('测试密码修改界面', () => {
  it('测试密码不统一', () => {
    expect(changepwd.isequal('123', '234', '245')).toBe(false)
  })

  it('测试旧密码未填写', () => {
    expect(changepwd.isequal('', '234', '245')).toBe(false)
  })

  it('测试新密码未填写', () => {
    expect(changepwd.isequal('123', '', '245')).toBe(false)
  })

  it('测试确认密码未填写', () => {
    expect(changepwd.isequal('123', '245', '')).toBe(false)
  })

  it('测试修改密码内容正确', () => {
    expect(changepwd.isequal('123', '245', '245')).toBe(true)
  })
})
