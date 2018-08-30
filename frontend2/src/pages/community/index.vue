<template>
  <div class="container">
    <div class="record" v-for="(record, id) in records">
      <div class="user">
        <img :src="imagesource" />
        <p class="username wrap_drop">
          <span v-if="id === -1">id</span>
          {{ record.username }} 《{{record.bookname}}》
        </p>
      </div>
      <p class="punchtext">{{ record.punchtext }}</p>
      <div v-for="imgfile in record.imgfiles" class="file">
        <img :src="imgfile.src" />
      </div>
      <div v-for="videofile in record.videofiles" class="file">
        <video :src="videofile.src" mode='aspectFit'></video>
      </div>
      <div class="action">
        <button id="like" @click="like(record)">赞
          <span v-if="record.has_liked === false"></span>
          <span v-if="record.likenumber !== 0">{{ record.likenumber }}</span>
        </button>
        <button id="comment" @click="comment(record)">
          {{ record.comment_info }}
        </button>
      </div>
      <div class="comment">
        <p v-for="comment in record.commentslist" class="wrap_drop">
          <span class="username">{{ comment.commentusername }}</span>
          : {{ comment.commenttext }}
        </p>
        <div class="new-comment" v-if="record.commented">
          <textarea v-model="record.newcomment" />
          <button id="submit" @click="submit(record)">发送</button>
        </div>
      </div>
    </div>
    <div class="function">
      <div @click="to_ranking">
        <img src="/static/img/tabbar_icon/yellow-rank.png" />
        <span>排行榜</span>
      </div>
    </div>
  </div>
</template>

<script>
import * as Tools from '../../components/Tools'
import qs from 'qs'
export default {
  data() {
    return {
      username: '',
      level: 0,
      records: [],
      now_comment_record: '',
      userimage: [],
      imagesource: '/static/img/game2/cat1.jpg',
      imagefile: '/static/img/file.png',
      now_begin: 0,
      now_item_number: 1
    }
  },
  onLoad: function(option) {
    this.username = option.username
    this.level = option.level
  },
  onShow: function() {
    this.now_begin = 0
    this.now_item_number = 10
    this.get_community()
  },
  onReachBottom: function() {
    this.get_image()
    this.get_video()
    this.now_begin += this.now_item_number
  },
  methods: {
    get_community() {
      this.records = []
      let fly = Tools.get_fly()
      let save = this
      fly
        .post(
          Tools.get_url() + 'get_community',
          qs.stringify({
            username: save.username,
            level: save.level
          })
        )
        .then(function(response) {
          if (response.data.status) {
            save.records = response.data.info
            save.get_image()
            save.get_video()
            save.now_begin += save.now_item_number
          } else {
            wx.showModal({
              title: '获取社群信息时发生错误，请检查网络或联系管理员！',
              success: function(response) {
                wx.navigateBack()
              }
            })
          }
        })
    },
    get_image() {
      let save = this
      wx.showToast({
        title: '加载图片中，请稍候',
        icon: 'loading',
        duration: 1000
      })
      for (
        let i = save.now_begin;
        i <
        (save.now_begin + save.now_item_number < save.records.length
          ? save.now_begin + save.now_item_number
          : save.records.length);
        ++i
      ) {
        for (let j = 0; j < save.records[i].imgfiles.length; ++j) {
          wx.downloadFile({
            url:
              Tools.get_url() +
              'get_punch_image?username=' +
              save.records[i].username +
              '&booknumber=' +
              save.records[i].booknumber +
              '&imgfile=' +
              save.records[i].imgfiles[j].number,
            success: function(picture_response) {
              save.$set(
                save.records[i].imgfiles[j],
                'src',
                picture_response.tempFilePath
              )
            }
          })
        }
      }
    },
    get_video() {
      let save = this
      wx.showToast({
        title: '加载视频中，请稍候',
        icon: 'loading',
        duration: 2000
      })
      for (
        let i = save.now_begin;
        i <
        (save.now_begin + save.now_item_number < save.records.length
          ? save.now_begin + save.now_item_number
          : save.records.length);
        ++i
      ) {
        for (let j = 0; j < save.records[i].videofiles.length; ++j) {
          wx.downloadFile({
            url:
              Tools.get_url() +
              'get_punch_video?username=' +
              save.records[i].username +
              '&booknumber=' +
              save.records[i].booknumber +
              '&videofile=' +
              save.records[i].videofiles[j].number,
            success: function(video_response) {
              save.$set(
                save.records[i].videofiles[j],
                'src',
                video_response.tempFilePath
              )
            }
          })
        }
      }
    },
    like(record) {
      if (record.has_liked === false) {
        record.likenumber += 1
      } else {
        record.likenumber -= 1
      }
      let fly = Tools.get_fly()
      let save = this
      fly
        .post(
          Tools.get_url() + 'like',
          qs.stringify({
            username: record.username,
            booknumber: record.booknumber,
            likeusername: save.username
          })
        )
        .then(function(response) {
          record.has_liked = !record.has_liked
        })
    },
    comment(record) {
      if (record.commented === true) {
        record.comment_info = '评论'
        record.commented = false
        this.now_comment_record = ''
      } else {
        if (this.now_comment_record !== '') {
          this.now_comment_record.comment_info = '评论'
          this.now_comment_record.commented = false
        }
        record.comment_info = '取消'
        record.commented = true
        this.now_comment_record = record
      }
    },
    is_empty(record) {
      if (record.newcomment !== '') {
        return false
      }
      return true
    },
    submit(record) {
      if (this.is_empty(record)) {
        wx.showToast({
          title: '请输入评论内容',
          icon: 'none',
          duration: 1000,
          mask: true
        })
      } else {
        let fly = Tools.get_fly()
        let save = this
        fly
          .post(
            Tools.get_url() + 'add_comment',
            qs.stringify({
              username: record.username,
              booknumber: record.booknumber,
              commentusername: save.username,
              comment: record.newcomment
            })
          )
          .then(function(response) {
            if (response.data.status === 'true') {
              record.commentslist = response.data.commentslist
              record.commented = false
              record.comment_info = '评论'
              record.newcomment = ''
              save.now_comment_record = ''
            } else {
              wx.showToast({
                title: '评论失败，请检查网络~',
                icon: 'none'
              })
            }
          })
      }
    },
    to_ranking() {
      wx.navigateTo({
        url:
          '/pages/ranking/main?username=' +
          this.username +
          '&level=' +
          this.level
      })
    }
  }
}
</script>

<style>
page {
  background-size: 100% 100%;
  background-image: url('https://daisy-donald.cn/image/sky.jpg');
}

.container {
  display: flex;
  height: 100%;
  padding-top: 10px;
}

.record {
  width: 90%;
  margin: 4%;
  background-color: antiquewhite;
  border: 5px solid #53cce9;
  border-radius: 10px;
}

.punchtext {
  margin: 0 5px;
  text-align: justify;
}

.user {
  display: flex;
}

.file {
  margin: 10px;
  text-align: center;
}

.file img {
  height: 300rpx;
  width: 500rpx;
}

.file video {
  margin: 10px auto;
  width: 500rpx;
  height: 300rpx;
}

.username {
  color: #53cce9;
  font-size: 18px;
  height: 40px;
  line-height: 40px;
}

.action {
  margin: 5% 0 5% 40%;
  display: flex;
  justify-content: space-between;
}

.comment {
  margin: 5px;
  border-top: 1px solid #fcf;
}

.new-comment {
  display: flex;
  margin: 5px 0;
}

.function {
  height: 50px;
  width: 100%;
  display: flex;
  justify-content: space-around;
  position: fixed;
  bottom: 0;
  background-color: #53cce9;
}

.function div {
  display: flex;
  flex-wrap: wrap;
  height: 50px;
  width: 50px;
}

.function span {
  height: 20px;
  width: 50px;
  color: #666;
  font-size: 12px;
  text-align: center;
}

.function img {
  width: 30px;
  height: 30px;
  margin: 0 auto;
}

button {
  height: 30px;
  line-height: 30px;
  color: #fff;
  font-weight: bold;
}

#like {
  width: 40%;
  background-color: #f53076;
}

#comment {
  width: 40%;
  background-color: #ffb001;
}

#submit {
  width: 25%;
  background-color: #53cce9;
}

img {
  width: 30px;
  height: 30px;
  margin: 5px;
}

textarea {
  padding: 0 2px;
  border-radius: 10px;
  height: 25px;
  width: 70%;
  border: 2px solid #ffb001;
}

.wrap_drop {
  word-wrap: break-word;
}
</style>
