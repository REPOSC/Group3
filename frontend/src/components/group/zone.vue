<template>
  <div class="login-container">
    <div>
      <div class="dynamicsHead">
        <div class="userText">
          <span class="userName">{{name}}</span>
          <span class="time">{{time}}</span>
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
          《财经》记者就该消息向保监会和安邦集团新闻宣传部门求证，保监会新闻部门未予置评。截至发稿时，安邦保险集团对此未予回应否认。记者就该消息向保监会和安邦集团新闻宣传部门求证，保监会新闻部门未予置评。截至发稿时，安邦保险集团对此未予回应否认。 《财经》记者就该消息向保监会和安邦集团新闻宣传部门求证，保监会新闻部门未予置评。截至发稿时，安邦保险集团对此未予回应否认。记者就该消息向保监会和安邦集团新闻宣传部门求证，保监会新闻部门未予置评。截至发稿时，安邦保险集团对此未予回应否认。 《财经》记者就该消息向保监会和安邦集团新闻宣传部门求证，保监会新闻部门未予置评。截至发稿时，安邦保险集团对此未予回应否认。记者就该消息向保监会和安邦集团新闻宣传部门求证，保监会新闻部门未予置评。截至发稿时，安邦保险集团对此未予回应否认。 《财经》记者就该消息向保监会和安邦集团新闻宣传部门求证，保监会新闻部门未予置评。截至发稿时，安邦保险集团对此未予回应否认。记者就该消息向保监会和安邦集团新闻宣传部门求证，保监会新闻部门未予置评。截至发稿时，安邦保险集团对此未予回应否认。 《财经》记者就该消息向保监会和安邦集团新闻宣传部门求证，保监会新闻部门未予置评。截至发稿时，安邦保 《财经》记者就该消息向保监会和安邦集团新闻宣传部门求证，保监会新闻部门未予置评。截至发稿时，安邦保 《财经》记者就该消息向保监会和安邦集团新闻宣传部门求证，保监会新闻部门未予置评。截至发稿时，安邦保 《财经》记者就该消息向保监会和安邦集团新闻宣传部门求证，保监会新闻部门未予置评。截至发稿时，安邦保 《财经》记者就该消息向保监会和安邦集团新闻宣传部门求证，保监会新闻部门未予置评。截至发稿时，安邦保险集团对此未予回应否认。记者就该消息向保监会和安邦集团新闻宣传部门求证，保监会新闻部门未予置评。截至发稿时，安邦保险集团对此未予回应否认。
        </div>
        <div @click="toggleContent" class="toggleText">
          {{ toggleText }}
        </div>
      </div>
    </div>
  </div>
</template>

<script >
export default {
  data() {
    return {
      isOpen: false,
      toggleText: '展开全文',
      name: 'jiazi',
      time: '12:00',
      confirm_pwd: ''
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
    }
  }
}
</script>

<style scoped>
.dynamicsContents {
  width: 100%;
  height: auto;
}
.login-container {
  -webkit-border-radius: 5px;
  border-radius: 5px;
  -moz-border-radius: 5px;
  background-clip: padding-box;
  margin: 180px auto;
  width: 80%;
  padding: 35px 35px 15px 35px;
  background: #fff;
  border: 1px solid #eaeaea;
  box-shadow: 0 0 25px #cac6c6;
}
.text {
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
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
</style>
