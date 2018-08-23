<!--<template>-->
  <!--<div class="card">-->
    <!--<p>请选择或者拍摄视频上传</p>-->
    <!--<input type="file" accept="video/avi,video/mp4,video/flv,video/3gp,video/swf" capture="camcorder" @change="onFileChange" style="display: none;">-->
    <!--<video ref="video" controls="controls"></video>-->
    <!--<div style="padding: 20px;text-align: center">-->
      <!--<yd-progressbar type="line" :progress="videoProgress" trail-width="4" trail-color="#FE5D51"></yd-progressbar>-->
      <!--<p>{{videoProgress*100}}%</p>-->
    <!--</div>-->
    <!--<el-button style="width: 30%;margin-left: 10%" bgcolor="#09c69c" color="#fff" shape="circle" @click.native="complete" action-type="button">确认上传</el-button>-->
  <!--</div>-->
<!--</template>-->
<!--<script>-->
<!--export default {-->
  <!--props: ['index'],-->
  <!--data: function() {-->
    <!--return {-->
      <!--text: ''-->
    <!--}-->
  <!--},-->
  <!--methods: {-->
    <!--get_audio: function(e) {-->
      <!--let audio = e.target.files[0]-->
      <!--this.$emit('get_audio', { value: audio, index: this.index })-->
    <!--},-->
    <!--get_text: function() {-->
      <!--this.$emit('get_text', { value: this.text, index: this.index })-->
    <!--},-->
    <!--submitUpload() {-->
      <!--this.$refs.upload.submit()-->
    <!--},-->
    <!--handleRemove(file, fileList) {-->
      <!--console.log(file, fileList)-->
    <!--},-->
    <!--handlePreview(file) {-->
      <!--console.log(file)-->
    <!--}-->
  <!--}-->
<!--}-->
<!--</script>-->
<!--<style scoped>-->
  <!--.shangchuan{-->
    <!--text-align: left;-->
  <!--}-->
<!--</style>-->
