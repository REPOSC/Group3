<template>
<div class="book-card">
  <div class="thumb">
    <img :src="book.image" mode="aspectFit" />
  </div>
  <div>
    <p :title="book.title">{{ book.title }}</p>
  </div>
  <div>
    <progress :percent="book.percent" stroke-width="5" activeColor=#53cce9 ></progress>
  </div>
</div>
</template>

<script>
export default {
  props: ['book']
}
</script>

<style scoped>
.book-card {
  padding: 0px 10px;
  margin-left: 3px;
  margin-right: 3px;
  margin-top: 40px;
  width: 20%;
  height: 16%;
  color: #53cce9;
  font-size: 16px;
  font-weight: bold;
}
img {
  width:50px;
  height:60px;
}
</style>
