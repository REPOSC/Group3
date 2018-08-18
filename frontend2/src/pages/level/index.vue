<template>
  <div class='choose'>
    <div class='levelbtn'>
      <button @click="onetest">K1</button>
      <button>K2</button>
      <button>K3</button>
      <button>K4</button>
      <button>K5</button>
      <button>K6</button>
      <button>K7</button>
      <button>K8</button>
      <button>K9</button>
      <button>K10</button>
      <button>K11</button>
      <button>K12</button>
    </div>
  </div>
</template>

<script>
import qs from 'qs';
export default {
  data() {
    return {
      username: '',
      levels: []
    };
  },
  onLoad: function() {
    let Fly2 = require('../../../node_modules/flyio/dist/npm/wx.js');
    let fly2 = new Fly2();
    let save = this;
    fly2
      .post(
        'http://139.199.106.168:8000/user_level',
        qs.stringify({
          id: '10000245'
        })
      )
      .then(function(response) {
        save.levels = [];
        let temp = response.data.levels;
        let i;
        for (i in temp) {
          save.levels.push(temp[i]);
        }
      });
  },
  methods: {
    onetest: function() {
      console.log(this.levels);
      let Fly2 = require('../../../node_modules/flyio/dist/npm/wx.js');
      let fly2 = new Fly2();
      let save = this;
      fly2
        .post(
          'http://139.199.106.168:8000/user_level',
          qs.stringify({
            id: '10000245',
            password: 'cXmjsy7P6acoWEj'
          })
        )
        .then(function(response) {
          if (response.data.status === 'error') {
            wx.showModal({
              content: '账号或密码错误，请重新登录'
            });
          } else {
            wx.redirectTo({
              url: '../level/main'
            });
          }
        });
    }
  }
};
</script>

<style>
div h1 {
  font-size: 35px;
  margin: 0 auto;
  width: 250px;
}
.levelbtn {
  display: flex;
  flex-wrap: wrap;
  margin: 0 auto;
}
button {
  width: 21%;
  height: 50%;
  padding: 20px;
  margin: 30px 20px;
  border-radius: 100%;
}
</style>
