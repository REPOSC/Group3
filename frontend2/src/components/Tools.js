function get_url() {
  return 'http://192.168.55.33:8000/'
}

function get_fly() {
  let Fly = require('../../node_modules/flyio/dist/npm/wx.js');
  let fly = new Fly();
  return fly
}

export {
  get_url,
  get_fly,
}
