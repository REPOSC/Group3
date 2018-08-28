<template>
  <div class="card">
    <div class="space title">
      {{'上传 '+text+' 的介绍视频'}}
    </div>
    <div class="space align">
      <div class="input-title displayed">请选择视频上传</div>
      <input type="file" accept="video/avi,video/mp4,video/flv,video/3gp,video/swf" class="file-btn displayed" capture="camcorder" @change="onFileChange">
    </div>
    <div class="space">
      <video ref="video" controls="controls" :src="video_src" class="fill"></video>
    </div>
    <el-button @click.native="complete">确认上传</el-button>
  </div>
</template>
<script>
export default {
  props: ['text'],
  data: function() {
    return {
      video_src: null,
      video: null
    }
  },
  methods: {
    onFileChange: function(e) {
      this.video = e.target.files[0]
      let reader = new FileReader()
      reader.readAsDataURL(this.video)
      let saved = this
      reader.onload = function(e) {
        saved.video_src = e.target.result
      }
    },
    complete: function() {
      this.$emit('post_video', { name: this.text, video: this.video })
    }
  }
}
</script>
<style scoped>
.shangchuan {
  text-align: left;
}
.fill {
  width: 100%;
}
</style>
