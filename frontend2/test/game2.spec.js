import { mount } from '@vue/test-utils'
import game2 from '../src/pages/game2/index'

describe('test game2 interface', () => {
  let wrapper,vm;

  beforeEach(() => {
    wrapper = mount (game2);
    vm = wrapper.vm;
  });

  it('test for showing div', () => {
    expect(wrapper.contains('div')).toBe(true);
  });

  it('test for showing span', () => {
    expect(wrapper.contains('span')).toBe(true);
  });
})
