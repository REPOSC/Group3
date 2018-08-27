<template>
<div class="all-message">
  <div class="messsage-card" v-for="n in messages.length">
    <sys_message v-bind="messages[n-1]" @more="more(messages[n-1])" @delete_mes="delete_mes(n-1)" @mark_notread="mark(messages[n-1])"></sys_message>
  </div>
</div>
</template>

<script>
import sys_message from '@/components/sys_message'
export default {
  components: {
    sys_message
  },
  data() {
    return {
      messages: [
        {
          send_time: '2018年8月27日',
          content: '啦啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊',
          content_status: 'false',
          expand_info: '展开更多',
          isread_info: '标记为未读',
          isread: 'notread'
        },
        {
          send_time: '2018年8月29日',
          content: '啦啦啦啦啦啦啦啦啦啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊',
          content_status: 'false',
          expand_info: '展开更多',
          isread_info: '标记为未读',
          isread: 'notread'
        }
      ]
    }
  },
  methods: {
    more(message) {
      if (message.content_status === 'false') {
        message.content_status = 'true'
        message.expand_info = '收起'
        message.isread = 'haveread'
        message.isread_info = '标记为未读'
      } else {
        message.content_status = 'false'
        message.expand_info = '展开更多'
      }
    },
    delete_mes(index) {
      this.messages.splice(index, 1)
    },
    mark(message) {
      if (message.isread_info === '标记为未读') {
        message.isread_info = '标记为已读'
        message.isread = 'notread'
      } else {
        message.isread_info = '标记为未读'
        message.isread = 'haveread'
      }
    }
  }
}
</script>

<style>
page {
  background-size: 100% 100%;
  background-image: url('https://daisy-donald.cn/image/back.jpg');
}
.all-message {
  margin: 10px 20px;
}
.message-card {
  width: 100px;
  height: 100px;
}
</style>
