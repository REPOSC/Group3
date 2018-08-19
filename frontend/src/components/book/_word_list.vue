<template>
  <div>
    <el-input @change="get_text" placeholder="请输入单词"></el-input>
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
  props: [
    'word_text',
    'word_audio',
    'index'
  ],
  methods: {
    get_audio: function(e) {
      let audio = e.target.files[0]
      this.$emit('get_audio', {value: audio, index: this.index})
    },
    get_text: function(text) {
      let saved = this
      this.$nextTick(() => {
        this.$emit('get_text', {value: text, index: saved.index})
      })
    }
  }
}
</script>
<style scope>
.file-btn {
  float: right;
}
</style>
