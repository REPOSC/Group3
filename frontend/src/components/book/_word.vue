<template>
  <div>
    <div class="space">
      <el-input @change="get_text" v-model="text" placeholder="请输入单词"></el-input>
    </div>
    <div class="align">
      <div class="input-title displayed">
        上传该单词音频
      </div>
      <input class="file-btn displayed" type="file" accept="audio/*" @change="get_audio">
    </div>
  </div>
</template>
<script>
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
    }
  }
}
</script>
<style scoped>
</style>
