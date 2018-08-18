<template>
  <div>
    <i-row>
      <div class="head">
        <i-col span="5" offset="5">
          <img src="/static/img/blue-star.png">
        </i-col>
        <i-col span="5">
          <div class="title">
            <h1>{{ booktitle }}</h1>
          </div>
        </i-col>
      </div>
    </i-row>
    <div class="firstpart">
      <img src="/static/img/yellow-tap.png">
      <h1>本课重点知识</h1>
      <p :key="one.index" v-for="one in ones">{{ one.index }}、{{ one.text }}</p>
    </div>
    <div class="secpart">
      <img src="/static/img/green-tap.png">
      <h1>今日导读</h1>
      <p :key="two.index" v-for="two in twos">{{ two.index }}、{{ two.text }}</p>
    </div>
    <div class="thirdpart">
      <div class="subtitle">
        <img src="/static/img/red-tap.png">
        <h1>词汇表与配音讲解</h1>
      </div>
      <p :key="three.index" v-for="three in threes">{{ three.text }}</p>
    </div>
    <div class="bottom">
      <i-row>
        <i-col span="6" offset="9">
          <div class="toMeBtn" @click="toMe">
            <img src="/static/img/man.png">
            <p>我的</p>
          </div>
        </i-col>
      </i-row>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      booktitle: ' BOOK1 ',
      ones: [
        {
          index: 1,
          text: '学会拼读简单dark'
        },
        {
          index: 2,
          text: '背诵句子It is dark'
        },
        {
          index: 3,
          text: '抄写课本一遍'
        }
      ],
      twos: [
        {
          index: 1,
          text: '与孩子一起看封面，并讨论自己居住的社区在天黑之后是什么样子的，谁晚上还不在家里，哪些动物夜晚才出来活动。'
        },
        {
          index: 2,
          text: '引导孩子仔细观察书的封面，让孩子讲一讲图片中的哪些细节可以显示天黑了，例如：天空的颜色，大钟显示的时间是6点，太阳刚刚下山，天上的星星刚刚显露出来。'
        }
      ],
      threes: [
        {
          index: 1,
          text: 'dark'
        },
        {
          index: 2,
          text: 'park'
        },
        {
          index: 3,
          text: 'mark'
        },
        {
          index: 4,
          text: 'last'
        }
      ]
    }
  }
}
</script>

<style>
page {
  background-size: 100% 100%;
  background-image: url('https://thumbnail0.baidupcs.com/thumbnail/208d7bfe35c662f32a88a1fe206d44e9?fid=3911358295-250528-398515735348763&time=1534424400&rt=sh&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-mj%2BYVt%2Fbo9W%2BSqMC7ImwhtUDIcs%3D&expires=8h&chkv=0&chkbd=0&chkpc=&dp-logid=5285426163203658882&dp-callid=0&size=c710_u400&quality=100&vuk=-&ft=video');
}
.head img {
  width: 60px;
  height: 60px;
}
.head h1 {
  font-size: 25px;
  font-weight: bolder;
  font-family: fantasy;
  color: white;
  background-color: #019dd6
}
.title {
  margin-top: 15px;
}
.firstpart {
  color: #eff000;
  align-content: center;
  margin: 30px;
  margin-top: 0px;
}
.secpart {
  color: #02c45d;
  align-content: center;
  margin: 30px;
}
.thirdpart {
  color: #de6648;
  align-content: center;
  margin: 30px;
}
.subtitle {
  display: block;
}
h1 {
  display: inline;
  font-size: 22px;
  font-weight: bolder;
  font-family: fantasy;
}
p {
  display: block;
  margin-right: 15px;
  font-size: 16px;
  font-weight: bold;
}
img {
  width: 30px;
  height: 30px;
}
.thirdpart p {
  display: inline-block;
  font-size: 20px;
  font-weight: bold;
  margin-right: 50px;
  margin-bottom: 10px;
}
.toMeBtn {
  position: fixed;
  width: 70px;
  height: 90px;
  font-weight: bolder;
  color: white;
  font-size: 18px;
  text-align: center;
  bottom: 10px;
}
.toMeBtn img {
  width: 70px;
  height: 70px;
}
.toMeBtn p {
  background-color: #ffb001;
  margin-left: 10px;
}
</style>
