function get_url() {
  return 'http://139.199.106.168:8000/'
}

function get_fly() {
  let Fly = require('../../node_modules/flyio/dist/npm/wx.js')
  let fly = new Fly()
  return fly
}

export { get_url, get_fly }
