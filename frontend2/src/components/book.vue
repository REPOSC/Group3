<template>
<div class="book-card">
  <div class="thumb" @click="on_click">
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
  props: ["book"],
  methods: {
	on_click: function() {
		this.$emit('on_click',this.book)
		}
	}
};
</script>

<style scoped>
.book-card {
  padding: 0% 3%;
  margin: 10% 3%;
  width: 20%;
  height: 16%;
  color: #53cce9;
  font-size: 14px;
  text-align: center;
}
img {
  width: 50px;
  height: 60px;
}
</style>
