<template>
  <div>
    <div class="function">
      <button @click="translate">翻译</button>
      <button @click="speak">讲解</button>
    </div>
    <div class="text english">
      <p :key="text.id" v-for="text in texts">
        {{ text.id }}、{{ text.english }}
      </p>
    </div>
    <div class="text chinese" v-if="translated === 1">
      <p :key="text.id" v-for="text in texts">
        {{ text.id }}、{{ text.chinese }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      translated: -1,
      texts: [
        {
          id: 1,
          english: 'It is dark.',
          chinese: '天黑了。'
        },
        {
          id: 2,
          english: 'It is dark in the park.',
          chinese: '公园里天黑了。'
        },
        {
          id: 3,
          english: 'It is dark in the wood.',
          chinese: '树林里天黑了。'
        },
        {
          id: 4,
          english: 'It is dark in the street.',
          chinese: '大街上天黑了。'
        },
        {
          id: 5,
          english: 'Where is it dark?',
          chinese: '哪里天黑了呢？'
        }
      ]
    }
  },
  methods: {
    translate () {
      this.translated = -this.translated
    },
    speak () {

    }
  }
}
</script>

<style>
.function {
  display: flex;
  justify-content: space-between;
}
button {
  width: 48%;
  height: 40px;
  line-height: 40px;
  margin: 5px 5px;
  font-size: 18px;
  font-weight: bold;
  color: #fff;
  background-color: #fe4f4c;
  border-radius: 20px;
}
button:active {
  background-color: #fe1a4c;
}
p {
  width: 100%;
  margin: 2px;
}
.text {
  display: flex;
  flex-wrap: wrap;
  color: #000;
  font-size: 25px;
  margin: 5px 5px;
  border-radius: 10px;
}
.english {
  border: 5px solid #0199d6;
}
.chinese {
  border: 5px solid #f67c30;
}
</style>
