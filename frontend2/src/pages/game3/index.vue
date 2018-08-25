<template>
  <div>
    <div class="area">
      <img :key="area.index" v-for="area in areas"
      :class="areas_static"  :src='area.src' @click="choose_area(area)"/>
      <img :class='answer_static' :src='completed_picture'/>
    </div>
    <div class="pic">
      <img :key="pic.index" v-for="pic in pics" :src="pic.src" mode="aspectFit"
      :class="pic.status" @click="choose_pic(pic)"/>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      now_pic: '',
      completed_picture: '/static/img/game2/cat1.jpg',
      answer_static: 'not_show_answer',
      areas_static: 'not_fill',
      pics: [
        {
          index: 0,
          src: '/static/img/game2/cat1.jpg',
          status: 'not_choosed'
        },
        {
          index: 1,
          src: '/static/img/game2/cat2.jpg',
          status: 'not_choosed'
        },
        {
          index: 2,
          src: '/static/img/game2/cat3.jpg',
          status: 'not_choosed'
        },
        {
          index: 3,
          src: '/static/img/game2/cat4.jpg',
          status: 'not_choosed'
        }
      ],
      areas: [
        {
          index: 0,
          match_index: 0,
          now_index: '',
          src: ''
        },
        {
          index: 1,
          match_index: 1,
          now_index: '',
          src: ''
        },
        {
          index: 2,
          match_index: 2,
          now_index: '',
          src: ''
        },
        {
          index: 3,
          match_index: 3,
          now_index: '',
          src: ''
        }
      ]
    }
  },
  methods: {
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
      for (let i = 0; i < this.pics.length; i++) {
        if (this.areas[i].now_index !== this.areas[i].match_index) {
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
<style scoed>
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
.pic img {
  width: 96px;
  height: 96px;
  margin: 20px 20px;
}
.show_answer {
  width: 220px;
  height: 206px;
  margin: 20px auto;
}
.not_show_answer {
  display: none
}
.not_fill {
  width: 96px;
  height: 96px;
  margin: 2px;
  border: 2px dashed #ffb001;
}
.all_fill {
  display: none
}
.not_choosed {
  border: #53cce9 solid 2px;
}
.choosing {
  border: #ffb001 solid 2px;
}
.choosed {
  display: none;
}
</style>
