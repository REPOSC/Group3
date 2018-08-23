<template>
  <div class="card">
    <div class="title">推送消息给用户</div>
    <div class="space"></div>
    <div class="input-title">编辑消息</div>
    <div class="space"></div>
    <textarea v-model="content" class="texts"></textarea>
    <div class="space"></div>
    <el-button type="primary" @click="submit"> 发送 </el-button>
    <div class="space"></div>
  </div>
</template>
<script>
import * as Tools from '../Tools/Tools'
import axios from 'axios'
import qs from 'qs'
export default {
  data() {
    return {
      content: ''
    }
  },
  methods: {
    submit: function() {
      axios
        .post(
          Tools.get_url() + 'put_message',
          qs.stringify({
            content: this.content
          })
        )
        .then(function(response) {
          if (response.data.success) {
            alert('发送消息成功！')
          } else {
            alert('发送消息失败！')
          }
        })
    }
  }
}
</script>
