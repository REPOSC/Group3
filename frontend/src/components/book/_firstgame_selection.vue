<template>
  <div class="align">
    <div class="space">
      <el-input v-model="text" @change="get_english_text" placeholder="请输入单词"></el-input>
    </div>
    <div class="input-title displayed">
      上传对应的图片
    </div>
    <input class="file-btn displayed" type="file" accept="image/*" @change="get_picture">
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
    get_english_text: function() {
      this.$emit('get_text', { index: this.index, value: this.text })
    },
    get_picture: function(e) {
      let picture = e.target.files[0]
      this.$emit('get_picture', { index: this.index, value: picture })
    }
  }
}
</script>
<style scoped>
</style>
