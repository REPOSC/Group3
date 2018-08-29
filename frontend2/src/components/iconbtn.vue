<template>
  <div class="left" @click="clickhandel">
    <div class="detail" @click="todetail">
      <img src="https://daisy-donald.cn/image/detail.png"
        @click="$emit('persual')">
      <p class="text">精读</p>
    </div>
    <div class="extensive" @click="$emit('not_persual')">
      <img src="https://daisy-donald.cn/image/extend.png">
      <p class="text">泛读</p>
    </div>
    <div class="previous" @click="$emit('toprevious')">
      <img src="https://daisy-donald.cn/image/left.png">
      <p class="text">上一页</p>
    </div>
    <div class="next" @click="$emit('tonext')">
      <img src="https://daisy-donald.cn/image/right.png">
      <p class="text">下一页</p>
    </div>
  </div>
</template>

<script>
export default {}
</script>

<style>
.text {
  color: #ff9000;
}

.detail,
.extensive {
  width: 50px;
  height: 60px;
  font-weight: bolder;
  color: white;
  margin-top: 20px;
  margin-bottom: 20px;
  font-size: 18px;
  text-align: center;
}

.previous,
.next {
  width: 50px;
  height: 60px;
  font-weight: bolder;
  color: white;
  font-size: 16px;
  text-align: center;
  margin-top: 20px;
  margin-bottom: 20px;
}

.left img {
  width: 50px;
  height: 50px;
}
</style>
