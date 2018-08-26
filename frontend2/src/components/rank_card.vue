<template>
  <div class="rank_card">
    <div class="rank_number">
      <p>{{ rank_number }}</p>
    </div>
    <div class="head_pic">
      <img :src="head_pic">
    </div>
    <div class="nickname">
      <p>{{ nickname }}</p>
    </div>
    <div class="mark">
      <p>{{ mark }}</p>
    </div>
  </div>
</template>
<script>
export default {
  props: [
    'rank_number',
    'head_pic',
    'nickname',
    'mark'
  ]
}
</script>
<style scoped>
.rank_card {
  display: flex;
  line-height: 100px;
  justify-content: space-between;
  size: 40px;
  height: 100px;
  width: 100%;
  border: 4px solid #53cce9;
  background-color: antiquewhite;
}
.head_pic img {
  width: 90px;
  height: 90px;
  vertical-align: middle;
}
.heart img {
  width: 30px;
  height: 30px;
}
.heart p {
  line-height: 50px;
}
.rank_number {
  width: 10%;
  text-align: center
}
.head_pic {
  width: 30%;
}
.nickname {
  width:30%;
}
.mark {
  width: 30%;
  size: 120px;
  color: #ffb001;
  font-weight: bolder;
}
.heart {
  width: 10%;
  text-align: center;
  line-height: 60px;
}
.lover-number {
  width: 10%;
}
</style>
