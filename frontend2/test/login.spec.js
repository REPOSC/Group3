jest.mock('qs', () => ({
  stringify: jest.fn(() => Promise.resolve(mockData1))
}));
import { mount } from '@vue/test-utils'
import login from '../src/pages/login/index'
import qs from 'qs';

describe('测试登录界面', () => {
  let wrapper,vm;

  beforeEach(() => {
    wrapper = mount (login);
    vm = wrapper.vm;
    wrapper.setData(
      {
        username: ['12345'],
        password: ['11111']
      })
  });

  it('测试账号输入', () => {
    expect(vm.username).toEqual(['12345'])
  });

  it('测试密码输入', () => {
    expect(vm.password).toEqual(['11111'])
  });

  it('测试显示登录按钮', () => {
    expect(wrapper.contains('button')).toBe(true);
  });

  it('测试使用表单', () => {
    expect(wrapper.contains('form')).toBe(true);
  });

  it('测试p标签的显示', () => {
    expect(wrapper.contains('p')).toBe(true);
  });

  it('测试div的显示', () => {
    expect(wrapper.contains('div')).toBe(true);
  });

  it('测试点击登录按钮触发handlelogin方法', () => {
    const mockFn = jest.fn();
    wrapper.setMethods({
      handlelogin: mockFn
    });
    wrapper.find('button').trigger('click');
    expect(mockFn).toBeCalled();
    expect(mockFn).toHaveBeenCalledTimes(1);
  });

  it('测试点击登录按钮调用了qs.stringify方法', () => {
    wrapper.find('button').trigger('click');
    expect(qs.stringify).toBeCalled();
  });

  it('为login单元测试增加快照', () => {
    expect(vm.$el).toMatchSnapshot()
  });
})
