<template>
  <div class="book-card">
    <div class="thumb" @click="on_click">
      <img :src="'/static/img/english1.jpg'" mode="aspectFit" />
    </div>
    <div>
      <p class="book-name">{{ book.name }}</p>
    </div>
    <div>
      <progress
        :percent="book.process"
        stroke-width="5"
        activeColor="#00c544">
      </progress>
    </div>
  </div>
</template>

<script>
export default {
  props: ['book'],
  methods: {
    on_click: function() {
      this.$emit('on_click', this.book)
    }
  }
}
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

.book-name {
  font-size: 12px;
  text-overflow: -o-ellipsis-lastline;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 1;
  -webkit-box-orient: vertical;
}

progress {
  margin: 5px auto;
  border-radius: 10px;
  border: 1px solid #00c544;
}
</style>
