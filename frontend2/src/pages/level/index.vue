<template>
  <div class='choose'>
    <div class='levelbtn'>
      <span v-for="level in levels">
        <button :class="level.check" @click="submit(level.id)">{{level.id + 1}}</button>
      </span>
    </div>
  </div>
</template>

<script>
import * as Tools from "../../components/Tools.js";
import qs from "qs";
export default {
  data() {
    return {
      max_value: 12,
      username: "",
      levels: [],
      last_level: "",
      judge_level: false
    };
  },
  onLoad: function(option) {
    this.username = option.username;
    this.last_level = option.last_level;
    let fly = Tools.get_fly();
    let save = this;
    fly
      .post(
        Tools.get_url() + "user_level",
        qs.stringify({
          id: save.username
        })
      )
      .then(function(response) {
        save.levels = [];
        let temp = response.data.levels;
        for (let i = 0; i < save.max_value; ++i) {
          if (temp.indexOf(i) !== -1) {
            if (save.judge_level === false) {
              if (save.last_level < i) {
                save.last_level = i;
              }
              save.judge_level = true;
            }
            save.levels.push({ check: "true", id: i });
          } else {
            save.levels.push({ check: "false", id: i });
          }
        }
      });
  },
  methods: {
    submit: function(level) {
      if (this.levels[level].check === "true") {
        wx.navigateTo({
          url: "../bookshelf/main?username=" + this.username + "&level=" + level
        });
      } else {
        wx.showModal({
          content: "您还没有拥有此等级的书籍，请选择其他等级。"
        });
      }
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
  width: 33%;
  height: 50%;
  padding: 20px;
  margin: 30px 20px;
  border-radius: 100%;
}
.true {
  width: 33%;
  height: 50%;
  padding: 20px;
  margin: 30px 20px;
  background-color: green;
  border-radius: 100%;
}
.false {
  background-color: gray;
  width: 33%;
  height: 50%;
  padding: 20px;
  margin: 30px 20px;
  border-radius: 100%;
}
</style>
