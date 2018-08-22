<template>
<div class="left" @click="clickhandel">
  <div class="detail" @click="todetail">
	<img src="/static/img/detail.png" @click="$emit('persual')">
	<p class="text">精读</p>
  </div>
  <div class="extensive" @click="$emit('not_persual')">
	<img src="/static/img/extend.png">
	<p class="text">泛读</p>
  </div>
  <div class="previous" @click="$emit('toprevious')">
	<img src="/static/img/left.png">
	<p class="text">上一页</p>
  </div>
  <div class="next" @click="$emit('tonext')">
	<img src="/static/img/right.png">
	<p class="text">下一页</p>
  </div>
</div>
</template>

<script>
export default {
}
</script>

<style>
.text{
  color:black;
}
.detail, .extensive {
  width: 50px;
  height: 60px;
  font-weight: bolder;
  color: white;
  margin-top: 20px;
  margin-bottom: 20px;
  font-size: 18px;
  text-align: center;
}
.previous, .next {
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
