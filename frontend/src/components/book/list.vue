<template>
  <div>
    <div class="card">
      <div class="title"> 基本信息 </div>
      <br><br>
      <div class="input-title"> 书籍名称 </div>
      <br><br>
      <el-input v-model="bookname" placeholder="请输入名称"></el-input>
      <br><br>
      <div class="input-title"> 书籍简介 </div>
      <br><br>
      <textarea class="texts" v-model="introduction"></textarea>
      <br><br>
      <div class="input-title"> 是否为精读书 </div>
      <br><br>
      <div>
        <el-radio v-model="persual" label="true" border>精读</el-radio>
        <el-radio v-model="persual" label="false" border>泛读</el-radio>
      </div>
      <div class="input-title"> 书籍等级 </div>
      <br><br>
      <el-input-number v-model="level" :min="1" :max="MAX_VALUE"></el-input-number>
      <br><br>
    </div>
    <div class="card">
      <div class="title"> 亲子阅读指导 </div>
      <br><br>
      <div v-for="(guide,index) in guides">
        <textarea class="texts" v-model="guides[index]"></textarea>
        <br><br>
      </div>
      <br><br>
      <el-button @click="add_guide"> 添加新指导条目 </el-button>
      <br><br>
    </div>
    <div class="card">
      <div class="title"> 本书重点知识 </div>
      <br><br>
      <div v-for="(knowledge,index) in knowledges">
        <textarea class="texts" v-model="knowledges[index]"></textarea>
        <br><br>
      </div>
      <br><br>
      <el-button @click="add_knowledge"> 添加新知识 </el-button>
      <br><br>
    </div>
    <div class="card">
      <div class="title"> 词汇表 </div>
      <br><br>
      <div v-for="(word,index) in words">
        <Word_list
        v-bind:word_text="words[index].text"
        v-bind:word_audio="words[index].audio"
        v-bind:index="index"
        @get_text="get_text" @get_audio="get_audio"></Word_list>
        <br><br>
      </div>
      <br><br>
      <el-button @click="add_word"> 添加新单词 </el-button>
      <br><br>
    </div>

    <el-button type="primary" @click="submit"> 上传书籍 </el-button>
    <br><br>
  </div>
</template>
<script>
import * as Tools from '../Tools/Tools'
import word_list from './_word_list.vue'
import axios from 'axios'
export default {
  data: function() {
    return {
      bookname: '',
      introduction: '',
      MAX_VALUE: Tools.MAX_VALUE,
      level: 1,
      guides: [''],
      knowledges: [''],
      words: [{ text: '', audio: null}],
      persual: 'true'
    }
  },
  mounted: function() {
  },
  methods: {
    add_knowledge: function() {
      this.knowledges.push('')
    },
    add_guide: function() {
      this.guides.push('')
    },
    add_word: function() {
      this.words.push({ word_text: '', audio_file: null})
    },
    get_audio: function(obj) {
      this.words[obj.index].audio = obj.value
    },
    get_text: function(obj) {
      this.words[obj.index].text = obj.value
    },
    submit: function() {
      if (!confirm('确定要上传所有的内容吗？')) {
        return
      }
      let my_values = new URLSearchParams()
      my_values.append('bookname', this.bookname)
      my_values.append('introduction', this.introduction)
      my_values.append('level', this.level)
      my_values.append('persual', this.persual === 'true')
      for (let i = 0; i < this.guides.length; ++i) {
        my_values.append('guides', this.guides[i])
      }
      for (let i = 0; i < this.knowledges.length; ++i) {
        my_values.append('knowledges', this.knowledges[i])
      }
      for (let i = 0; i < this.words.length; ++i) {
        my_values.append('word_text', this.words[i].text)
        my_values.append('word_audio', this.words[i].audio)
      }
      let saved = this
      axios
        .post(Tools.get_url() + 'get_book', my_values)
        .then(function(response) {
          saved.$notify({
            title: '上传成功！',
            position: 'bottom-right'
          })
        })
    }
  },
  components: {
    Word_list: word_list
  }
}
</script>
<style>
.demo-table-expand label {
  font-weight: bold;
}
</style>
