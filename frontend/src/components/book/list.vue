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
        <Word
        v-bind:index="index"
        @get_text="get_text" @get_audio="get_guide_audio"></Word>
        <br><br>
      </div>
      <br><br>
      <el-button @click="add_word"> 添加新单词 </el-button>
      <br><br>
    </div>
    <div>
      <div v-for="(page,index) in pages">
        <Page
          v-bind:index="index"
          @get_english="get_book_english_text"
          @get_chinese="get_book_chinese_text"
          @get_audio="get_book_audio"
          @get_picture="get_book_picture"
        ></Page>
        <br><br>
      </div>
      <el-button @click="add_page"> 添加新的书页 </el-button>
      <br><br>
    </div>
    <br><br>
    <el-button type="primary" @click="submit"> 上传书籍 </el-button>
    <br><br>
  </div>
</template>
<script>
import * as Tools from '../Tools/Tools'
import word from './_word.vue'
import page from './_page.vue'
import axios from 'axios'
export default {
  data: function() {
    return {
      bookname: '',
      introduction: '',
      MAX_VALUE: Tools.MAX_VALUE,
      level: 1,
      guides: [],
      knowledges: [],
      words: [],
      persual: 'true',
      pages: []
    }
  },
  mounted: function() {},
  methods: {
    add_knowledge: function() {
      this.knowledges.push('')
    },
    add_guide: function() {
      this.guides.push('')
    },
    add_word: function() {
      this.words.push({ text: '', audio: null })
    },
    add_page: function() {
      this.pages.push({ english_text: '', chinese_text: '', audio: null, picture: null })
    },
    get_guide_audio: function(obj) {
      this.words[obj.index].audio = obj.value
    },
    get_text: function(obj) {
      this.words[obj.index].text = obj.value
    },
    get_book_audio: function(obj) {
      this.pages[obj.index].audio = obj.value
    },
    get_book_picture: function(obj) {
      this.pages[obj.index].picture = obj.value
    },
    get_book_english_text: function(obj) {
      this.pages[obj.index].english_text = obj.value
    },
    get_book_chinese_text: function(obj) {
      this.pages[obj.index].chinese_text = obj.value
    },
    submit: function() {
      if (!confirm('确定要上传所有的内容吗？')) {
        return
      } else if (this.bookname === '') {
        alert('没有填写书籍名称，无法上传！')
        return
      } else if (this.pages.length === 0) {
        alert('书籍没有内容书页，无法上传！')
        return
      }
      let my_values = new FormData()
      my_values.append('bookname', this.bookname)
      my_values.append('introduction', this.introduction)
      my_values.append('level', this.level)
      my_values.append('persual', this.persual === 'true')
      for (let i = 0; i < this.guides.length; ++i) {
        if (!Tools.check_warning(this.guides[i], '知识导读', String(i + 1))) {
          return
        }
        my_values.append('guides', this.guides[i])
      }
      for (let i = 0; i < this.knowledges.length; ++i) {
        if (!Tools.check_warning(this.knowledges[i], '重点知识讲解', String(i + 1))) {
          return
        }
        my_values.append('knowledges', this.knowledges[i])
      }
      for (let i = 0; i < this.words.length; ++i) {
        if (!Tools.check_fetal(this.words[i].text, '重点单词文本', String(i + 1))) {
          return
        }
        my_values.append('word_text', this.words[i].text)
        if (!Tools.check_fetal(this.words[i].audio, '重点单词音频', String(i + 1))) {
          return
        }
        my_values.append('word_audio', this.words[i].audio)
      }
      for (let i = 0; i < this.pages.length; ++i) {
        if (!Tools.check_warning(this.pages[i].english_text, '书籍内容英语文本', String(i + 1))) {
          return
        }
        my_values.append('book_english_text', this.pages[i].english_text)
        if (!Tools.check_warning(this.pages[i].chinese_text, '书籍内容中文翻译', String(i + 1))) {
          return
        }
        my_values.append('book_chinese_text', this.pages[i].chinese_text)
        if (!Tools.check_fetal(this.pages[i].audio, '书籍内容配音', String(i + 1))) {
          return
        }
        my_values.append('book_audio', this.pages[i].audio)
        if (!Tools.check_fetal(this.pages[i].picture, '书籍内容图片', String(i + 1))) {
          return
        }
        my_values.append('book_picture', this.pages[i].picture)
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
    Word: word,
    Page: page
  }
}
</script>
<style>
</style>
