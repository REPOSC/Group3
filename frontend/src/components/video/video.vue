<template>
  <div class="card">
    <p>请选择或者拍摄视频上传</p>
    <input type="file" accept="video/avi,video/mp4,video/flv,video/3gp,video/swf" capture="camcorder" @change="onFileChange" >
    <video ref="video" controls="controls"></video>
    <div >
      <p>{{videoProgress*100}}%</p>
    </div>
    <el-button  @click.native="complete">确认上传</el-button>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  props: ['index'],
  data: function() {
    return {
      text: ''
    }
  },
  methods: {
    get_audio: function(e) {
      let audio = e.target.files[0]
      this.$emit('get_audio', { value: audio, index: this.index })
    },
    get_text: function() {
      this.$emit('get_text', { value: this.text, index: this.index })
    },
    onFileChange: function(e) {
      var files = e.target.files || e.dataTransfer.files
      if (!files.length) return
      // 视频上传
      if (this.typeName === '视频') {
        let _this = this

        // 视频预览
        var reader = new FileReader()
        this.file = files[0]
        reader.onload = function() {
          _this.$refs.video.src = this.result
        }
        reader.readAsDataURL(this.file)
      }
    },
    complete: function() {
      let _this = this
      if (this.typeName === '视频') {
        let data = new FormData()
        data.append('file', this.file)
        data.append('arr_name', this.file.name)
        // 进度百分比
        var config = {
          onUploadProgress: progressEvent => {
            var complete =
              (progressEvent.loaded / progressEvent.total * 100) | 0
            this.videoProgress = complete / 100
            console.log(this.videoProgress)
          }
        }
        axios
          .post(
            _this.Api + 'Material_management/image/' + _this.material_id + '/1',
            data,
            config
          )
          .then(res => {
            _this.$dialog.toast({
              mes: res.data.tips,
              timeout: 1000,
              icon: 'success'
            })
            _this.$router.push('/source')
          })
          .catch(function(error) {
            _this.$dialog.toast({
              mes: error.response.data.tips,
              timeout: 1000,
              icon: 'error'
            })
          })
      }
    }
  }
}
</script>
<style scoped>
.shangchuan {
  text-align: left;
}
</style>
