<template>
  <div>
    <div class="answer">
      <div class="area" :key="area.index" v-for="area in areas"></div>
    </div>
    <div class="picture">
      <img :key="picture.index" v-for="picture in pictures" :src="picture.src" mode="aspectFit" />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      pictures: [
        {
          index: 1,
          src: '/static/img/game3/cat.jpg'
        },
        {
          index: 2,
          src: '/static/img/game3/cat.jpg'
        },
        {
          index: 3,
          src: '/static/img/game3/cat.jpg'
        },
        {
          index: 4,
          src: '/static/img/game3/cat.jpg'
        }
      ],
      areas: [
        {
          index: 1
        },
        {
          index: 2
        },
        {
          index: 3
        },
        {
          index: 4
        }
      ]
    }
  }
}
</script>

<style scoed>
.picture {
  width: 280px;
  margin: 10px auto;
  display: flex;
  flex-wrap: wrap;
  border: 6px solid #53cce9;
  border-radius: 10px;
}
.answer {
  width: 220px;
  height: 206px;
  margin: 20px auto;
  display: flex;
  flex-wrap: wrap;
}
img {
  width: 100px;
  height: 100px;
  margin: 20px 20px;
}
.area {
  width: 100px;
  height: 100px;
  margin: 2px;
  border: 2px dashed #ffb001;
}
</style>
