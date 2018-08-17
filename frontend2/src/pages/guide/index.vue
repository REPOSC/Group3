<template>
  <div>
    <i-collapse simple>
      <i-collapse-item title="教学指导">
        <i-panel class="info" slot="content">
          <p style="font-size: 14px">{{ content1 }}</p>
        </i-panel>
      </i-collapse-item>
      <i-collapse-item title="重点知识">
        <i-panel class="info" slot="content">
          <li v-for="item in items1" :key="item">{{ item.text }}</li>
        </i-panel>
      </i-collapse-item>
      <i-collapse-item class="title" title="今日导读">
        <i-panel class="info" slot="content">
          <p style="font-size: 14px">{{ content2 }}</p>
        </i-panel>
      </i-collapse-item>
      <i-collapse-item class="title" title="词汇表">
        <i-panel class="info" slot="content">
          <li v-for="item in items2" :key="item">{{ item.text }}</li>
        </i-panel>
      </i-collapse-item>
    </i-collapse>
  </div>
</template>

<script>
export default {
  data () {
    return {
      content1: '首先 接着 最后',
      content2: '小红帽与狼外婆',
      items1: [
        { text: '学会日常用语' },
        { text: '学会背诵小鸭子' },
        { text: '预习下一课' }
      ],
      items2: [
        { text: '学会日常用语' },
        { text: '学会背诵小鸭子' },
        { text: '预习下一课' }
      ]
    }
  }
}
</script>

<style>

div {
  margin: 50px auto;
}
.info {
  font-size: 18px;
}
li {
  font-size: 18px;
  border: solid 1px white;
}
i-collapse-item {
  font-size: 24px;
  padding: 20px 20px;
  border: solid 1px white;
}
</style>
