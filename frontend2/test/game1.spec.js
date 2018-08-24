import { mount } from '@vue/test-utils'
import game1 from '../src/pages/game1/index'

describe('test game1 interface', () => {
  let wrapper,vm;

  beforeEach(() => {
    wrapper = mount (game1);
    vm = wrapper.vm;
  });

  it('test line_end()', () => {
    expect(vm.line_end(1)).toBe(190);
  });

  it('test line_start()', () => {
    expect(vm.line_start(1)).toBe(195);
  });

  it('test for showing div', () => {
    expect(wrapper.contains('div')).toBe(true);
  });

  it('test for showing canvas', () => {
    expect(wrapper.contains('canvas')).toBe(true);
  });
})
