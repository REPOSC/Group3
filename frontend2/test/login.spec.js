jest.mock('qs', () => ({
  stringify: jest.fn(() => Promise.resolve(mockData1))
}));
import { mount } from '@vue/test-utils'
import login from '../src/pages/login/index'
import qs from 'qs';

describe('test login interface', () => {
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

  it('test for inputing account', () => {
    expect(vm.username).toEqual(['12345'])
  });

  it('test for password inputing', () => {
    expect(vm.password).toEqual(['11111'])
  });

  it('test login button', () => {
    expect(wrapper.contains('button')).toBe(true);
  });

  it('test the showing of form', () => {
    expect(wrapper.contains('form')).toBe(true);
  });

  it('test the showing of p', () => {
    expect(wrapper.contains('p')).toBe(true);
  });

  it('test the showing of div', () => {
    expect(wrapper.contains('div')).toBe(true);
  });

  it('test clicking handlelogin function', () => {
    const mockFn = jest.fn();
    wrapper.setMethods({
      handlelogin: mockFn
    });
    wrapper.find('button').trigger('click');
    expect(mockFn).toBeCalled();
    expect(mockFn).toHaveBeenCalledTimes(1);
  });

  it('test for qs.stringify using', () => {
    wrapper.find('button').trigger('click');
    expect(qs.stringify).toBeCalled();
  });
})
