<template>
  <div :class="isread">
    <div class="top">
      <p class="time">{{ send_time }}</p>
      <p class="expand" @click="$emit('get_more')">{{ expand_info }}</p>
    </div>
    <div class="body">
      <p :class="content_status">{{ content }}</p>
    </div>
    <div class="function" v-if="content_status === 'true'">
      <button class="mark" @click="$emit('mark_message')">
        {{ isread_info }}
      </button>
      <button class="close" @click="$emit('delete_message')">删除</button>
    </div>
  </div>
</template>

<script>
export default {
  props: [
    'send_time',
    'content',
    'content_status',
    'expand_info',
    'isread_info',
    'isread'
  ]
}
</script>

<style scoped>
.notread {
  color: #ffb100;
  border: 3px solid #ffb100;
  margin: 10px auto;
  border-radius: 10px;
  padding: 5px 19px;
  background-color: antiquewhite;
}

.read {
  color: #53cce9;
  border: 2px solid #53cce9;
  margin: 10px auto;
  border-radius: 10px;
  padding: 5px 19px;
  background-color: antiquewhite;
}

.top {
  height: 30px;
  font-size: 16px;
  display: flex;
  justify-content: space-between;
}

.time {
  height: 30px;
  line-height: 30px;
}

.expand {
  height: 30px;
  line-height: 30px;
}

.function {
  font-size: 16px;
  color: white;
  display: flex;
  margin: 10px auto;
}

.close {
  font-size: 16px;
  width: 40%;
  height: 30px;
  line-height: 30px;
  background-color: #f53076;
}

.mark {
  font-size: 16px;
  width: 40%;
  height: 30px;
  line-height: 30px;
  background-color: #53cce9;
}

.false {
  text-align: justify;
  font-size: 18px;
  text-overflow: -o-ellipsis-lastline;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  align-content: center;
  color: #222;
}

.true {
  text-align: justify;
  font-size: 18px;
  color: #222;
}
</style>
