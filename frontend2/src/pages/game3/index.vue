<template>
  <div>
    <div class="area">
      <img :key="area.index" v-for="area in areas" :class="areas_static+picture_number" :src='area.src' @click="choose_area(area)" />
      <img :class='answer_static' :src='completed_picture' />
    </div>
    <div class="pic">
      <img :key="pics.index" v-for="pic in pics" :src="pic.src" mode="aspectFit" :class="pic.status+picture_number" @click="choose_pic(pic)" />
    </div>
    <div class="texts">{{word_text}}</div>
  </div>
</template>
<script>
import * as Tools from '../../components/Tools.js'
import qs from 'qs'
export default {
  data() {
    return {
      booknumber: null,
      now_pic: '',
      completed_picture: null,
      answer_static: null,
      areas_static: null,
      picture_number: 4,
      word_text: '',
      pics: [],
      areas: []
    }
  },
  onLoad: function(status) {
    this.booknumber = status.booknumber
  },
  onShow: function() {
    this.init()
  },
  methods: {
    init() {
      this.now_pic = ''
      this.answer_static = 'not_show_answer'
      this.areas_static = 'not_fill'
      this.completed_picture = null
      this.pics = []
      this.areas = []
      let fly = Tools.get_fly()
      let save = this
      fly
        .post(
          Tools.get_url() + 'get_third_game_text',
          qs.stringify({
            book_id: save.booknumber
          })
        )
        .then(function(response) {
          save.word_text = response.data.text
        })
      fly
        .post(
          Tools.get_url() + 'get_third_game_number',
          qs.stringify({
            book_id: save.booknumber
          })
        )
        .then(function(response) {
          save.picture_number = parseInt(response.data.number)
          let random_indexs = Tools.generate_random_list(save.picture_number)
          for (let i = 0; i < save.picture_number; ++i) {
            save.areas.push({
              index: i,
              now_index: '',
              src: ''
            })
            save.pics.push({
              index: i,
              match_index: random_indexs[i],
              src: null,
              status: 'not_choosed'
            })
          }
          for (let i = 0; i < save.picture_number; ++i) {
            wx.downloadFile({
              url:
                Tools.get_url() +
                'get_third_game_image?book_id=' +
                save.booknumber +
                '&number=' +
                save.pics[i].match_index,
              success: function(picture_response) {
                if (picture_response.statusCode === 200) {
                  let pic_tmp_obj = save.pics[i]
                  pic_tmp_obj.src = picture_response.tempFilePath
                  save.$set(save.pics, i, pic_tmp_obj)
                }
              }
            })
          }
          wx.downloadFile({
            url:
              Tools.get_url() +
              'get_third_game_image?book_id=' +
              save.booknumber +
              '&number=' +
              '-1',
            success: function(picture_response) {
              if (picture_response.statusCode === 200) {
                save.completed_picture = picture_response.tempFilePath
              }
            }
          })
        })
    },
    choose_pic(pic) {
      if (pic.status === 'choosing') {
        pic.status = 'not_choosed'
        this.now_pic = ''
      } else if (pic.status === 'not_choosed') {
        pic.status = 'choosing'
        if (this.now_pic !== '') {
          this.pics[this.now_pic].status = 'not_choosed'
        }
        this.now_pic = pic.index
      }
    },
    choose_area(area) {
      if (this.now_pic !== '') {
        this.fill_area(area)
        if (this.is_finished()) {
          this.show_isright_message()
        }
      } else if (this.now_pic === '' && area.now_index !== '') {
        this.unfill_area(area)
      } else {
        this.show_notchoose_message()
      }
    },
    is_finished() {
      for (let i = 0; i < this.areas.length; i++) {
        if (this.areas[i].now_index === '') {
          return false
        }
      }
      return true
    },
    is_right() {
      console.log(this.pics.length)
      for (let i = 0; i < this.pics.length; i++) {
        if (this.pics[this.areas[i].now_index].match_index !== i) {
          return false
        }
      }
      return true
    },
    show_complete_picture() {
      this.answer_static = 'show_answer'
      this.areas_static = 'all_fill'
    },
    show_isright_message() {
      if (this.is_right()) {
        this.show_complete_picture()
        wx.showModal({
          title: '宝宝真棒！',
          content: '已完成该练习，是否退出~',
          cancelText: '再看看',
          confirmText: '退出',
          confirmColor: '#ffb001',
          success: function(res) {
            if (res.confirm) {
              wx.navigateBack({
                url: '../practice/main'
              })
            }
          }
        })
      } else {
        wx.showModal({
          title: '啊噢，就差一点点噢...',
          content: '再试一次吧~',
          cancelText: '不了',
          confirmText: '再试一次',
          confirmColor: '#ffb001',
          success: function(res) {
            if (res.cancel) {
              wx.navigateBack({
                url: '../practice/main'
              })
            }
          }
        })
      }
    },
    fill_area(area) {
      if (area.now_index !== '') {
        this.pics[area.now_index].status = 'not_choosed'
      }
      area.now_index = this.now_pic
      area.src = this.pics[this.now_pic].src
      this.pics[this.now_pic].status = 'choosed'
      this.now_pic = ''
    },
    unfill_area(area) {
      this.pics[area.now_index].status = 'not_choosed'
      area.now_index = ''
      area.src = ''
    },
    show_notchoose_message() {
      wx.showToast({
        title: '还没选择拼图噢~',
        image: '/static/game2/lock.png',
        duration: 1500,
        mask: true
      })
    }
  }
}
</script>
<style scoped>
.pic {
  width: 280px;
  margin: 10px auto;
  display: flex;
  flex-wrap: wrap;
  border-radius: 10px;
}
.area {
  width: 220px;
  height: 206px;
  margin: 20px auto;
  display: flex;
  flex-wrap: wrap;
}
.show_answer {
  width: 220px;
  height: 206px;
  margin: 20px auto;
}
.not_show_answer {
  display: none;
}
.not_fill4 {
  width: 96px;
  height: 96px;
  margin: 2px;
  border: 2px dashed #ffb001;
}
.not_fill9 {
  width: 60px;
  height: 60px;
  margin: 2px;
  border: 2px dashed #ffb001;
}
.all_fill4,
.all_fill9 {
  display: none;
}

.not_choosed4 {
  border: #53cce9 solid 2px;
  width: 96px;
  height: 96px;
  margin: 20px 20px;
}
.choosing4 {
  border: #ffb001 solid 2px;
  width: 96px;
  height: 96px;
  margin: 20px 20px;
}
.not_choosed9 {
  border: #53cce9 solid 2px;
  width: 60px;
  height: 60px;
  margin: 12px 12px;
}
.choosing9 {
  border: #ffb001 solid 2px;
  width: 60px;
  height: 60px;
  margin: 12px 12px;
}
.texts {
  text-align: center;
  margin: 20px auto;
}
.choosed4,
.choosed9 {
  display: none;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen,
    Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  font-size: 20px;
}
</style>
