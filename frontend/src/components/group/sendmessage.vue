<template>
  <div class="card">
    <div class="title space">推送消息给用户</div>
    <div class="input-title space">编辑消息</div>
    <textarea v-model="content" class="texts space"></textarea>
    <el-button type="primary" @click="submit"> 发送 </el-button>
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
      if (!confirm('你确认将此消息推送给所有人吗？')) {
        return
      }
      if (this.content === '') {
        this.$notify.error({
          title: '错误',
          message: '消息为空，无法发送！'
        })
        return
      }
      let saved = this
      axios
        .post(
          Tools.get_url() + 'put_message',
          qs.stringify({
            content: this.content
          })
        )
        .then(function(response) {
          if (response.data.success) {
            saved.$notify({
              title: '成功',
              message: '发送消息成功！',
              type: 'success',
              position: 'bottom-right'
            })
          } else {
            saved.$notify.error({
              title: '错误',
              message: '发送消息失败！'
            })
          }
        })
    }
  }
}
</script>
