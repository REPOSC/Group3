<template>
  <div>
    <div v-for="name in names">
      <Video v-bind:text="name" @post_video="post_video"></Video>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import video from './_video.vue'
import * as Tools from '../Tools/Tools'
export default {
  data: function() {
    return {
      names: [
        '基本操作',
        '亲子阅读指导',
        'e-book',
        '连线游戏',
        '看词识图',
        '拼图游戏',
        '听音选图',
        '阅读拓展'
      ]
    }
  },
  components: {
    Video: video
  },
  mounted: function() {},
  methods: {
    post_video: function(object) {
      let values = new FormData()
      let saved = this
      if (!object.video) {
        saved.$notify({
          title: '警告',
          message: '视频为空， 无法上传！',
          type: 'warning'
        })
        return
      }
      values.append('name', object.name)
      values.append('video', object.video)
      axios
        .post(Tools.get_url() + 'add_introduction_video', values)
        .then(function() {
          saved.$notify({
            title: '上传成功！',
            position: 'bottom-right'
          })
        })
    }
  }
}
</script>
<style scoped>
</style>
