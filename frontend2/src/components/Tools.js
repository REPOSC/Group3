function get_url() {
  return 'http://139.199.106.168:8000/'
}

function get_fly() {
  let Fly = require('../../node_modules/flyio/dist/npm/wx.js')
  let fly = new Fly()
  return fly
}

function generate_random_list(number) {
  let list = []
  for (let i = 0; i < number; ++i) {
    list.push({
      key: i,
      value: Math.random()
    })
  }
  list.sort(function (a, b) {
    return a.value > b.value ? 1 : (a.value === b.value ? 0 : -1)
  })
  for (let i = 0; i < number; ++i) {
    list[i] = list[i].key
  }
  return list
}

export {
  get_url,
  get_fly,
  generate_random_list
}
