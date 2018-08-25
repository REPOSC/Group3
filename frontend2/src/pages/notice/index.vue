<template>
  <div class="container">
    <div class="record" v-for="record in records" @click="read">
      <p class="name">{{ record.name }}</p>
      <p class="content">{{ record.content }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      records: [
        {
          id: 1,
          name: '弗恩英语',
          content: '小程序新上线，快来体验吧~'
        },
        {
          id: 2,
          name: '弗恩英语',
          content: '1111'
        },
        {
          id: 3,
          name: '弗恩英语',
          content: '222'
        }
      ]
    }
  },
  methods: {
    read () {}
  }
}
</script>

<style scoped>
page {
  background-size: 100% 100%;
  background-image: url('https://139.199.106.168/image/back.jpg');
}
.container {
  display: flex;
  height: 100%;
  padding-top: 10px;
}
.record {
  width: 90%;
  margin: 4%;
  border: 5px solid #53cce9;
  border-radius: 10px;
}
.name {
  font-weight: bold;
  margin-bottom: 10px;
}
</style>
