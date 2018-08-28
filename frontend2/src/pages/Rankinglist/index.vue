<template>
  <div class='all-ranklist'>
    <div class="title">
      <img src="https://daisy-donald.cn/image/rainbow.png">
      <p>排行榜</p>
    </div>
    <div :class="my-ranklist">
      <my_rank_card v-bind="my_rankinfo"></my_rank_card>
    </div>
    <div class="their-ranklist" v-for="n in length">
      <rank_card v-bind="rankinfo[n-1]"></rank_card>
    </div>
  </div>
</template>
<script>
import rank_card from '@/components/rank_card'
import my_rank_card from '@/components/my_rank_card'
export default {
  data() {
    return {
      length: 8,
      my_rankinfo: {
        rank_number: 3,
        head_pic: 'https://daisy-donald.cn/image/cat1.jpg',
        nickname: 'cfl',
        mark: 98
      },
      rankinfo: [
        {
          rank_number: 1,
          head_pic: 'https://daisy-donald.cn/image/cat1.jpg',
          nickname: 'yym',
          mark: 98
        },
        {
          rank_number: 2,
          head_pic: 'https://daisy-donald.cn/image/cat1.jpg',
          nickname: 'zth',
          mark: 98
        },
        {
          rank_number: 3,
          head_pic: 'https://daisy-donald.cn/image/cat1.jpg',
          nickname: 'cfl',
          mark: 98
        },
        {
          rank_number: 4,
          head_pic: 'https://daisy-donald.cn/image/cat1.jpg',
          nickname: 'zyz',
          mark: 98
        },
        {
          rank_number: 5,
          head_pic: 'https://daisy-donald.cn/image/cat1.jpg',
          nickname: 'yym',
          mark: 98
        },
        {
          rank_number: 6,
          head_pic: 'https://daisy-donald.cn/image/cat1.jpg',
          nickname: 'zth',
          mark: 98
        },
        {
          rank_number: 7,
          head_pic: 'https://daisy-donald.cn/image/cat1.jpg',
          nickname: 'cfl',
          mark: 98
        },
        {
          rank_number: 8,
          head_pic: 'https://daisy-donald.cn/image/cat1.jpg',
          nickname: 'zyz',
          mark: 98
        }
      ]
    }
  },
  components: {
    rank_card,
    my_rank_card
  },
  onload() {
    this.length = this.rankinfo.length
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
  color: #ffb001;
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
