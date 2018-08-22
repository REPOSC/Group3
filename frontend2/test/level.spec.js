import { mount } from '@vue/test-utils'
import level from '../src/pages/level/index'

describe('测试等级界面', () => {
  let wrapper,vm;

  beforeEach(() => {
    wrapper = mount (level);
    vm = wrapper.vm;
  });

  it('测试显示等级按钮', () => {
    expect(wrapper.contains('button')).toBe(false);
  });

  it('测试样式', () => {
    expect(wrapper.is('.true')).toBe(true);
    expect(wrapper.is('.false')).toBe(true);
    expect(wrapper.is('.levelbtn')).toBe(true);
  })

  it('测试div的显示', () => {
    expect(wrapper.contains('div')).toBe(true);
  });
})
