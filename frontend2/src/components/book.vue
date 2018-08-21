<template>
<div class="book-card">
  <div class="thumb">
    <img :src="'/static/img/english1.jpg'" mode="aspectFit" />
  </div>
  <div>
    <p :title="book.name">{{ book.name }}</p>
  </div>
  <div>
    <progress :percent="book.process" stroke-width="5" activeColor=#53cce9 ></progress>
  </div>
</div>
</template>

<script>
export default {
  props: ["book"]
};
</script>

<style scoped>
.book-card {
  padding: 0% 3%;
  margin: 10% 3%;
  width: 20%;
  height: 16%;
  color: #53cce9;
  font-size: 16px;
  font-weight: bold;
}
img {
  width: 50px;
  height: 60px;
}
</style>
