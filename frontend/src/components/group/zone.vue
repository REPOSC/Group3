<!--suppress ALL -->
<template>
  <div>
    <div class="shrink">
      <div class="userText">
        <span class="userName">{{items.user_name}}：『{{items.book_num}}』：
          《{ {items.book_name}}》
        </span>
      </div>
      <div class="align right">
        <el-button type="danger" icon="el-icon-delete" circle
        @click="deldaka"></el-button>
      </div>
    </div>
    <div class="text">
      <div class="content wrap_drop">
        {{items.article}}
        <img :src=img.src class="screen" v-for="img in images">
        <video class="screen" v-for="video in videos" autoplay playsinline>
          <source :src=video.src>
        </video>
      </div>
    </div>
    <div>
      <div class="likeList">{{ratings}}</div>
      <div class="otherInfo">
        <div class="iconBox ">
          <div>
            点赞人数 {{items.like_num}}
          </div>
        </div>
      </div>
      <div class="pinglunInfo shrink" v-for='i in shuoData'>
        <div>
          <div class="userText">
            <span class="userName">{{i.shuo_user_id}}</span>
          </div>
          <div class="align right">
            <el-button type="danger" icon="el-icon-delete" circle
            @click="delcomment(i.commentid)"></el-button>
          </div>
        </div>
        <div class="wrap_drop space">{{i.commenting}}</div>
      </div>
    </div>
  </div>
</template>

<script>
import * as Tools from '../Tools/Tools'
import axios from 'axios'
import qs from 'qs'
export default {
  name: 'zone',
  data() {
    return {
      isOpen: false,
      toggleText: '展开全文',
      ratings: [],
      showAll: false,
      shuoData: [],
      like_usernames: '',
      images: [],
      videos: []
    }
  },
  props: ['items'],
  computed: {
    showList: function() {
      if (this.showAll === false) {
        var showList = []
        if (this.shuoData.length > 3) {
          for (var i = 0; i < 3; i++) {
            showList.push(this.shuoData[i])
          }
        } else {
          showList = this.shuoData
        }
        return showList
      } else {
        return this.shuoData
      }
    },
    word: function() {
      if (this.showAll === false) {
        return '点击展开'
      } else {
        return '点击收起'
      }
    }
  },
  methods: {
    toggleContent: function() {
      if (this.isOpen === false) {
        this.isOpen = true
        this.toggleText = '收起'
      } else {
        this.isOpen = false
        this.toggleText = '展开全文'
      }
    },
    filelist() {
      let saved = this

      axios
        .post(
          Tools.get_url() + 'get_file_numbers',
          qs.stringify({
            booknumber: saved.items.book_num,
            usernumber: saved.items.user_name
          })
        )
        .then(function(response) {
          let tmp_images = response.data.imgfiles
          let tmp_videos = response.data.videofiles
          for (let i = 0; i < tmp_images.length; ++i) {
            tmp_images[i].src =
              Tools.get_url() +
              'get_punch_image?username=' +
              saved.items.user_name +
              '&booknumber=' +
              saved.items.book_num +
              '&imgfile=' +
              tmp_images[i].number
            saved.images.push(tmp_images[i])
          }
          for (let i = 0; i < tmp_videos.length; ++i) {
            tmp_videos[i].src =
              Tools.get_url() +
              'get_punch_video?username=' +
              saved.items.user_name +
              '&booknumber=' +
              saved.items.book_num +
              '&videofile=' +
              tmp_videos[i].number
            saved.videos.push(tmp_videos[i])
          }
        })
    },
    likelist() {
      let saved = this
      axios
        .post(
          Tools.get_url() + 'daka_like',
          qs.stringify({
            book_num: saved.items.book_num,
            user_name: saved.items.user_name
          })
        )
        .then(function(response) {
          saved.ratings = response.data.like_nicknames
        })
    },
    commentlist() {
      let saved = this
      this.shuoData = []
      axios
        .post(
          Tools.get_url() + 'daka_comment',
          qs.stringify({
            book_num: saved.items.book_num,
            user_name: saved.items.user_name
          })
        )
        .then(function(response) {
          let commentusers = response.data.comment_user_numbers
          let comments = response.data.comments
          let commentids = response.data.commentids
          for (let i = 0; i < commentusers.length; ++i) {
            saved.shuoData.push({
              shuo_user_id: commentusers[i],
              commenting: comments[i],
              commentid: commentids[i]
            })
          }
        })
    },
    delcomment(e) {
      if (!confirm('删除评论后无法恢复，确认要删除吗？')) {
        return
      }
      let saved = this
      axios
        .post(
          Tools.get_url() + 'del_comment',
          qs.stringify({
            commentid: e
          })
        )
        .then(function(response) {
          if (response.data.success) {
            saved.commentlist()
            saved.$notify({
              title: '删除评论成功！',
              position: 'bottom-right',
              type: 'success'
            })
          } else {
            saved.$notify({
              title: '删除评论失败',
              type: 'warning'
            })
          }
        })
    },
    deldaka() {
      if (!confirm('删除打卡后无法恢复，确认要删除吗？')) {
        return
      }
      let saved = this
      axios
        .post(
          Tools.get_url() + 'del_punch',
          qs.stringify({
            book_num: saved.items.book_num,
            user_name: saved.items.user_name
          })
        )
        .then(function(response) {
          if (response.data.success) {
            saved.$emit('dakalist')
            saved.$notify({
              title: '删除打卡成功！',
              position: 'bottom-right',
              type: 'success'
            })
          } else {
            saved.$notify({
              title: '删除打卡失败',
              type: 'warning'
            })
          }
        })
    }
  },
  mounted() {
    this.filelist()
    this.likelist()
    this.commentlist()
  }
}
</script>
<style scoped>
.dynamicsContents {
  width: 100%;
  height: auto;
}

.text {
  background-clip: padding-box;
  margin: 10px auto;
  width: 90%;
  padding: 5px 5px 5px 5px;
  border: 1px solid #eaeaea;
  box-shadow: 0 0 5px #cac6c6;
  text-align: left;
}

.dynamicsHead {
  width: 100%;
  height: 50px;
  line-height: 50px;
}

.userText {
  height: 50px;
  float: left;
}

.userName,
.time {
  display: block;
  width: 100%;
  line-height: 25px;
}

.userName {
  color: #333;
}

.time {
  color: #999;
}

.likeList {
  text-align: left;
  margin-left: 50px;
}

.headButton {
  line-height: 50px;
  float: right;
}

.oneButton:first-child {
  margin-right: 32px;
}

.content {
  line-height: 22px;
  overflow: hidden;
}

.toggleText {
  color: #a70008;
  cursor: pointer;
}

.foldHeight {
  height: 110px;
}

.openHeight {
  height: auto;
}

.otherInfo {
  height: 40px;
  padding-bottom: 15px;
  color: #999;
  line-height: 40px;
}

.pinglunInfo {
  height: auto;
  padding-bottom: 15px;
  color: #999;
  line-height: 40px;
  border-bottom: 1px solid #e7e7e7;
  text-align: left;
  margin-left: 50px;
}

.iconBox {
  float: right;
  cursor: pointer;
  margin-right: 50px;
}

.changecolor {
  display: inline;
  margin-right: 50px;
}

.changecolor:hover {
  color: #ba0101;
}

.dynamicsBox {
  width: 90%;
  height: auto;
  margin: 0 auto 20px;
  display: flex;
  flex-flow: column nowrap;
  justify-content: flex-start;
  border: 5px;
}

.wrap_drop {
  word-wrap: break-word;
}

.right {
  text-align: right;
}

.shrink {
  width: 80%;
}

.screen {
  width: 33%;
  height: 300px;
}
</style>
