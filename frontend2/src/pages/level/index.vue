<template>
  <div class='choose'>
    <div class='levelbtn'>
      <button v-for="level in levels" :key=level.id :class="level.check" @click="submit(level.id)">K{{level.id + 1}}</button>
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
              if (i === save.last_level) {
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
          content: '您还没有拥有此等级的书籍，请选择其他等级。'
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
            wx.navigateTo({
              url: '../bookshelf/main?username=' + this.username + '&level=' + level
            })
          })
      }
    }
  }
}
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
  width: 20%;
  height: 50%;
  padding: 20px;
  margin: 8% 6.5%;
  border-radius: 100%;
}
.true {
  background-color: green;
}
.false {
  background-color: gray;
}
.last {
  background-color: orange;
}
</style>
