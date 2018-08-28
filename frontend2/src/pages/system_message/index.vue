<template>
  <div class="all-message">
    <div class="messsage-card" v-for="n in messages.length">
      <sys_message v-bind="messages[n-1]" @more="more(messages[n-1])" @delete_message="delete_message(n-1)" @mark_message="mark(messages[n-1])">
      </sys_message>
    </div>
  </div>
</template>

<script>
import sys_message from '@/components/sys_message'
import * as Tools from '../../components/Tools.js'
import qs from 'qs'

export default {
  components: {
    sys_message
  },
  data() {
    return {
      username: null,
      messages: []
    }
  },
  onLoad: function(status) {
    this.username = status.username
  },
  onShow: function() {
    this.init()
  },
  methods: {
    init() {
      this.messages = []
      let fly = Tools.get_fly()
      let save = this
      fly
        .post(
          Tools.get_url() + 'get_message',
          qs.stringify({
            username: save.username
          })
        )
        .then(function(response) {
          let tmp_response = response.data.messages
          if (tmp_response.length === 0) {
            wx.showToast({
              title: '暂时没有消息哦~'
            })
          } else {
            for (let i = 0; i < tmp_response.length; ++i) {
              save.messages.push({
                number: tmp_response[i].number,
                send_time: tmp_response[i].time,
                content: tmp_response[i].content,
                content_status: 'false',
                expand_info: '展开更多',
                isread_info:
                  '标记为' +
                  (tmp_response[i].isread === 'true' ? '未读' : '已读'),
                isread: tmp_response[i].isread === 'true' ? 'read' : 'notread'
              })
            }
          }
        })
    },
    read(message) {
      let fly = Tools.get_fly()
      let save = this
      fly.post(
        Tools.get_url() + 'read_message',
        qs.stringify({
          username: save.username,
          message: message.number
        })
      )
    },
    unread(message) {
      let fly = Tools.get_fly()
      let save = this
      fly.post(
        Tools.get_url() + 'unread_message',
        qs.stringify({
          username: save.username,
          message: message.number
        })
      )
    },
    del(index) {
      let fly = Tools.get_fly()
      let save = this
      fly
        .post(
          Tools.get_url() + 'delete_message',
          qs.stringify({
            username: save.username,
            message: save.messages[index].number
          })
        )
        .then(function() {
          save.messages.splice(index, 1)
        })
    },
    more(message) {
      if (message.content_status === 'false') {
        message.content_status = 'true'
        message.expand_info = '收起'
        message.isread = 'read'
        message.isread_info = '标记为未读'
      } else {
        message.content_status = 'false'
        message.expand_info = '展开更多'
      }
      this.read(message)
    },
    delete_message(index) {
      let save = this
      wx.showModal({
        title: '确定删除此消息吗？',
        success: function(response) {
          if (response.confirm) {
            save.del(index)
          }
        }
      })
    },
    mark(message) {
      if (message.isread === 'read') {
        message.isread_info = '标记为已读'
        message.isread = 'notread'
        this.unread(message)
      } else {
        message.isread_info = '标记为未读'
        message.isread = 'read'
        this.read(message)
      }
    }
  }
}
</script>

<style>
page {
  background-size: 100% 100%;
  background-image: url('https://daisy-donald.cn/image/sky.jpg');
}
.all-message {
  margin: 10px 20px;
}
.message-card {
  width: 100px;
  height: 100px;
}
</style>
