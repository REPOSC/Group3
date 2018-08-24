import { mount } from '@vue/test-utils'
import level from '../src/pages/level/index'

describe('test level interface', () => {
  let wrapper,vm;

  beforeEach(() => {
    wrapper = mount (level);
    vm = wrapper.vm;
  });

  it('test for showing button', () => {
    expect(wrapper.contains('button')).toBe(false);
  });

  it('test for showing div', () => {
    expect(wrapper.contains('div')).toBe(true);
  });
})
