<!--suppress ALL -->
<template>
  <div class="loginContainer">
    <div class="dynamicsBox">
      <div class="dynamicsHead">
        <div class="userText">
          <span class="userName">{{items.user_name}}</span>
          <!-- <span class="time">{{items.riqi}}</span> -->
          <span class="time">{{items.book_num}}</span>
        </div>
        <div class="headButton">
          <div class="oneButton">
            <el-button @click="deldaka">删除</el-button>
          </div>
        </div>
      </div>
    </div>
    <div class="text">
      <div class="dynamicsContents">
        <div
          class="content"
          v-bind:class="[isOpen ? 'openHeight' : 'foldHeight']"
        >
          {{items.commenting}}
        </div>
        <div @click="toggleContent" class="toggleText">
          {{ toggleText }}
        </div>
      </div>
    </div>
    <div class="dynamicsInfo">
      <div class="likeList">{{ratings}}</div>
      <div class="otherInfo">
        <div class="iconBox ">
          <div>
            点赞人数{{items.like_num}}
          </div>
        </div>
      </div>
      <div class="hello">
        <div class="pinglunInfo" v-for='i in shuoData'>
          <div class="ren"> {{i.shuo_user_id}}</div><br>
          <div class="say">{{i.article}}</div>
          <el-button @click="delcomment(i.commentid)">删除</el-button>
        </div>
        <div @click="showAll = !showAll" class="show-more">{{word}}</div>
      </div>
      <div class="userList"></div>
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
      shuoData: []
    }
  },
  props: ['items'],
  computed: {
    showList: function() {
      if (this.showAll === false) {
        // 当数据不需要完全显示的时候
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
          let nicknames = eval(response.data.like_nicknames)
          saved.ratings = nicknames
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
              article: comments[i],
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
            alert('删除评论成功！')
          } else {
            alert('删除失败！')
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
            alert('删除成功！')
          } else {
            alert('删除失败！')
          }
        })
    }
  },
  mounted() {
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
.loginContainer {
  -webkit-border-radius: 5px;
  border-radius: 5px;
  -moz-border-radius: 5px;
  background-clip: padding-box;
  margin: 180px auto;
  width: 74%;
  padding: 35px 35px 15px 35px;
  background: #fff;
  border: 1px solid #eaeaea;
  box-shadow: 0 0 25px #cac6c6;
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
.dynamicsInfo {
  width: 100%;
}
.otherInfo {
  height: 40px;
  padding-bottom: 15px;
  color: #999;
  line-height: 40px;
  border-bottom: 1px solid #e7e7e7;
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
.ren {
  height: 10px;
}
.say {
  border: double;
  margin-left: 100px;
  width: 700px;
  display: inline-block;
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
</style>
