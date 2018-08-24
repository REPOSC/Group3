<!--suppress ALL -->
<template>
  <div class="loginContainer">
    <div class="dynamicsBox">
      <div class="dynamicsHead">
        <div class="userText">
          <span class="userName">{{items.user_name}}</span>
          <span class="time">{{items.riqi}}</span>
        </div>
        <div class="headButton">
          <div class="oneButton">
            <el-button>置顶</el-button>
            <el-button>删除</el-button>
          </div>
        </div>
      </div>
    </div>
    <div class="text">
      <div class="dynamicsContents">
        <div class="content" v-bind:class="[isOpen ? 'openHeight' : 'foldHeight']">
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
          <!--<ul>-->
          <!--<li><img :src="icons.forword" class="img"></li>-->
          <!--</ul>-->
          <div @click="like" class="changecolor">
            点赞
          </div>
          <!--<ul>-->
          <!--<li><img :src="icons.comment" class="img"></li>-->
          <!--</ul>-->
          <div @click="comment" class="changecolor">
            评论
          </div>
        </div>
      </div>
      <div class="hello">
        <div class="pinglunInfo" v-for='i in shuoData'>
          <div class="ren"> {{i.shuo_user_id}}</div><br>
          <div class="say">{{i.article}}</div>
          <button class="shan">删除</button>
        </div>
        <div @click="showAll = !showAll" class="show-more">{{word}}</div>
      </div>
      <div class="userList"></div>
    </div>
    <div @touchend="Input"></div>
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
      icons: {
        rating: [require('./rating1.png'), require('./rating.png')],
        comment: require('./comment.png'),
        forword: require('./forword.png')
      },
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
        if (this.toLearnList.length > 3) {
          for (var i = 0; i < 3; i++) {
            showList.push(this.toLearnList[i])
          }
        } else {
          showList = this.toLearnList
        }
        return showList
      } else {
        return this.toLearnList
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
          qs.stringify({ item: saved.items })
        )
        .then(function(response) {
          let ids = eval(response.data.like_ids)
          for (let i = 0; i < ids.length; ++i) {
            saved.ratings.push({
              id: ids[i]
            })
          }
        })
    },
    commentlist() {
      let saved = this
      axios
        .post(
          Tools.get_url() + 'daka_comment',
          qs.stringify({ item: saved.items })
        )
        .then(function(response) {
          let commentuserids = eval(response.data.comment_user_number_ids)
          let shuocomments = eval(response.data.comments)
          for (let i = 0; i < commentuserids.length; ++i) {
            saved.shuoData.push({
              shuo_user_id: commentuserids[i],
              article: shuocomments[i]
            })
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
