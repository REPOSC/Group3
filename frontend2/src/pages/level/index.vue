<template>
  <div class="choose">
    <div class="levelbtn">
      <div v-for="level in levels"
        :key=level.id
        :class="level.check"
        @click="submit(level.id)">K{{ level.id + 1 }}</div>
    </div>
  </div>
</template>

<script>
import * as Tools from '../../components/Tools.js'
import qs from 'qs'
export default {
  data() {
    return {
      max_value: 12,
      username: '',
      levels: [],
      last_level: '',
      judge_level: false
    }
  },
  onLoad: function(option) {
    this.username = option.username
    this.last_level = option.last_level
  },
  onShow: function(option) {
    this.get_level()
  },
  methods: {
    get_level() {
      let fly = Tools.get_fly()
      let save = this
      fly
        .post(
          Tools.get_url() + 'user_level',
          qs.stringify({
            id: save.username
          })
        )
        .then(function(response) {
          save.levels = []
          let temp = response.data.levels
          for (let i = 0; i < save.max_value; ++i) {
            if (temp.indexOf(i) !== -1) {
              if (save.judge_level === false) {
                if (save.last_level < i) {
                  save.last_level = i
                }
                save.judge_level = true
              }
              if (i === parseInt(save.last_level)) {
                save.levels.push({ check: 'last', id: i })
              } else {
                save.levels.push({ check: 'true', id: i })
              }
            } else {
              save.levels.push({ check: 'false', id: i })
            }
          }
        })
    },
    submit: function(level) {
      if (this.levels[level].check === 'false') {
        wx.showModal({
          content: '您未解锁该等级，请选择其他等级。',
          showCancel: false
        })
      } else {
        let fly = Tools.get_fly()
        let save = this
        fly
          .post(
            Tools.get_url() + 'change_last_level',
            qs.stringify({
              id: save.username,
              newlevel: level
            })
          )
          .then(function(response) {
            save.last_level = level
            wx.navigateTo({
              url: '../bookshelf/main?username=' +
              save.username + '&level=' + level
            })
          })
      }
    }
  }
}
</script>

<style>
page {
  background-size: 100% 100%;
  background-image: url('https://daisy-donald.cn/image/sky.jpg');
}
.levelbtn {
  width: 100%;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin: 60px auto;
}
.levelbtn div {
  width: 80px;
  height: 80px;
  line-height: 80px;
  text-align: center;
  color: #fff;
  font-size: 25px;
  font-weight: bold;
  margin: 20px;
  border-radius: 100%;
}
.true {
  background-color: #00c544;
}
.false {
  background-color: #ccc;
}
.last {
  background-color: #ffb001;
}
</style>
