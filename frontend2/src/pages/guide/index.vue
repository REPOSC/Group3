<template>
  <div>
    <div class="firstpart">
      <p>本课重点知识</p>
      <p :key="one.index" v-for="one in ones">{{ one.index }}、{{ one.text }}</p>
    </div>
    <div class="secpart">
      <p>今日导读</p>
      <p :key="two.index" v-for="two in twos">{{ two.index }}、{{ two.text }}</p>
    </div>
    <div class="threepart">
      <p>词汇表与配音讲解</p>
      <p :key="three.index" v-for="three in threes">{{ three.index }}、{{ three.text }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      ones: [
        {
          index: 1,
          text: '拼读'
        },
        {
          index: 2,
          text: '背诵'
        },
        {
          index: 3,
          text: '抄写'
        }
      ],
      twos: [
        {
          index: 1,
          text: '拼读'
        },
        {
          index: 2,
          text: '背诵'
        },
        {
          index: 3,
          text: '抄写'
        }
      ],
      three: [

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
</style>
