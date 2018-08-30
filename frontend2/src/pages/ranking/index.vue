<template>
  <div class='all-ranklist'>
    <div class="title">
      <img src="https://daisy-donald.cn/image/rainbow.png">
      <p>排行榜</p>
    </div>
    <div :class="my-ranklist">
      <my_rank_card v-bind="my_rankinfo"></my_rank_card>
    </div>
    <div class="their-ranklist" v-for="n in showed_rankinfo.length">
      <rank_card v-bind="showed_rankinfo[n-1]"></rank_card>
    </div>
  </div>
</template>
<script>
import rank_card from '@/components/rank_card'
import my_rank_card from '@/components/my_rank_card'
import * as Tools from '../../components/Tools.js'
import qs from 'qs'
export default {
  data() {
    return {
      username: null,
      level: null,
      my_rankinfo: {
        rank_number: 0,
        head_pic: '正在获取...',
        nickname: '正在获取...',
        mark: '正在获取...'
      },
      rankinfo: [],
      showed_rankinfo: [],
      now_begin: 0,
      now_item_number: 10
    }
  },
  onLoad(status) {
    this.username = status.username
    this.level = status.level
  },
  onShow() {
    this.init()
  },
  onReachBottom: function() {
    this.get_image()
  },
  methods: {
    init() {
      let fly = Tools.get_fly()
      let save = this
      save.now_begin = 0
      save.showed_rankinfo = []
      save.rankinfo = []
      fly
        .post(
          Tools.get_url() + 'get_all_ranks',
          qs.stringify({
            level: save.level
          })
        )
        .then(function(response) {
          if (response.status === 200) {
            for (let i = 0; i < response.data.people.length; ++i) {
              save.rankinfo.push({
                username: response.data.people[i].username,
                rank_number: i + 1,
                head_pic: null,
                nickname: response.data.people[i].nickname,
                mark: response.data.people[i].mark
              })
              if (response.data.people[i].username === save.username) {
                save.my_rankinfo.rank_number = i + 1
                save.my_rankinfo.head_pic = null
                save.my_rankinfo.nickname = response.data.people[i].nickname
                save.my_rankinfo.mark = response.data.people[i].mark
              }
            }
            save.get_image(
              save.now_begin,
              save.now_begin + save.now_item_number
            )
          }
        })
    },
    get_image() {
      let save = this
      wx.showToast({
        title: '加载中，请稍候',
        icon: 'loading',
        duration: 1000
      })
      for (
        let i = save.now_begin;
        i < save.now_begin + save.now_item_number;
        ++i
      ) {
        wx.downloadFile({
          url:
            Tools.get_url() +
            'get_user_image?username=' +
            save.rankinfo[i].username,
          success: function(picture_response) {
            let pic_tmp_obj = save.rankinfo[i]
            pic_tmp_obj.head_pic = picture_response.tempFilePath
            save.showed_rankinfo.push(pic_tmp_obj)
          }
        })
      }
      this.now_begin += this.now_item_number
    }
  },
  components: {
    rank_card,
    my_rank_card
  }
}
</script>
<style>
page {
  background-size: 100% 100%;
  background-image: url('https://daisy-donald.cn/image/sky.jpg');
}

.title {
  height: 70px;
  line-height: 70px;
  text-align: center;
  display: flex;
  justify-content: center;
}

.title p {
  color: yellow;
  font-size: 25px;
  font-weight: bold;
}

.title img {
  width: 70px;
  height: 70px;
}

.all-ranklist {
  margin: 20px 20px;
}

.my-ranklist {
  padding: 5px;
  margin: 20px auto;
}

.their-ranklist {
  margin: 10px auto;
}

rank_card {
  height: 100px;
  margin: 5px;
}
</style>
