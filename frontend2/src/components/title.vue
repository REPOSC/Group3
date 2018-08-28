<template>
  <div>
    <div class="title">
      <img src="/static/img/rainbow.png">
      <p>{{ booktitle }}</p>
      <button @click="$emit('play_video')">{{ play_info }}</button>
    </div>
    <div v-if="is_play_video" class="video">
      <video :src="src" />
    </div>
  </div>
</template>
<script>
export default {
  props: [
    'play_info',
    'is_play_video',
    'src',
    'booktitle'
  ]
}
</script>
<style>
.title {
  height: 70px;
  line-height: 70px;
  text-align: center;
  display: flex;
  justify-content: center;
}
.title p {
  color: yellow;
  font-size: 25px;
  font-weight: bold;
  text-shadow: 2px 2px 3px #000;
}
.title img {
  width: 70px;
  height: 70px;
}
.title button {
  position: absolute;
  color: white;
  font-size: 10px;
  font-weight: bolder;
  line-height: 20px;
  height: 20px;
  right: 10px;
  background-color: #ffb100;
}
.video {
  text-align: center;
}
</style>
