<template>
  <div>
    <el-input @change="get_text" v-model="text" placeholder="请输入单词"></el-input>
    <br><br>
    <div class="input-title">
    上传该单词音频
    </div>
    <input
    class="file-btn"
    type="file"
    accept="audio/*"
    @change="get_audio">
  </div>
</template>
<script>
export default {
  props: ['index'],
  data: function(){
    return {
      text:''
    }
  },
  methods: {
    get_audio: function(e) {
      let audio = e.target.files[0]
      this.$emit('get_audio', { value: audio, index: this.index })
    },
    get_text: function() {
      this.$emit('get_text', { value: this.text, index: this.index })
    }
  }
}
</script>
<style scoped>

</style>
