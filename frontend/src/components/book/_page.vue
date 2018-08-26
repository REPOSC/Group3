<template>
  <div class='card '>
    <div class="space">
      <div class="title">
        添加书籍第 {{index+1}} 页
      </div>
    </div>
    <img v-bind:src="picture_addr" class="picture">
    <div class="space align">
      <div class="input-title displayed">上传第 {{index+1}} 页图片</div>
      <input class="file-btn displayed" type="file" accept="image/*" @change="get_picture">
    </div>
    <div class="space align">
      <div class="input-title displayed">上传第 {{index+1}} 页音频</div>
      <input class="file-btn displayed" type="file" accept="audio/*" @change="get_audio">
    </div>
    <div class="input-title space">
      输入第 {{index+1}} 页英文
    </div>
    <textarea class="texts" @change="get_english_text" v-model="english_text"></textarea>
    <div class="input-title space">
      输入第 {{index+1}} 页中文
    </div>
    <textarea class="texts" @change="get_chinese_text" v-model="chinese_text"></textarea>
  </div>
</template>
<script>
export default {
  props: ['index'],
  data: function() {
    return {
      picture_addr: null,
      english_text: '',
      chinese_text: ''
    }
  },
  methods: {
    get_audio: function(e) {
      let audio = e.target.files[0]
      this.$emit('get_audio', { value: audio, index: this.index })
    },
    get_picture: function(e) {
      let picture = e.target.files[0]
      let reader = new FileReader()
      reader.readAsDataURL(picture)
      let saved = this
      reader.onload = function(e) {
        saved.picture_addr = e.target.result
      }
      this.$emit('get_picture', { value: picture, index: this.index })
    },
    get_english_text: function() {
      this.$emit('get_english', { value: this.english_text, index: this.index })
    },
    get_chinese_text: function() {
      this.$emit('get_chinese', { value: this.chinese_text, index: this.index })
    }
  }
}
</script>
<style scoped>
</style>
