<template>
  <div>
    <div class="card">
      <div class="title sapce"> 基本信息 </div>
      <div class="input-title space"> 书籍名称 </div>
      <el-input v-model="bookname" placeholder="请输入名称"></el-input>
      <div class="input-title space"> 书籍简介 </div>
      <textarea class="texts" v-model="introduction"></textarea>
      <div class="input-title space"> 是否为精读书 </div>
      <div class="space">
        <el-radio v-model="persual" label="true" border>精读</el-radio>
        <el-radio v-model="persual" label="false" border>泛读</el-radio>
      </div>
      <div class="input-title"> 书籍等级 </div>
      <el-input-number v-model="level" :min="1" :max="MAX_VALUE"></el-input-number>
    </div>
    <div class="card">
      <div class="title space"> 本书导读 </div>
      <div class="space" v-for="(guide,index) in guides">
        <textarea class="texts" v-model="guides[index]"></textarea>
      </div>
      <el-button @click="add_guide"> 添加新指导条目 </el-button>
    </div>
    <div class="card">
      <div class="title space"> 本书重点知识 </div>
      <div class="space" v-for="(knowledge,index) in knowledges">
        <textarea class="texts" v-model="knowledges[index]"></textarea>
      </div>
      <el-button @click="add_knowledge"> 添加新知识 </el-button>
    </div>
    <div class="card">
      <div class="title space"> 词汇表 </div>
      <div class="space" v-for="(word,index) in words">
        <Word v-bind:index="index" @get_text="get_text" @get_audio="get_guide_audio"></Word>
      </div>
      <el-button @click="add_word"> 添加新单词 </el-button>
    </div>
    <div class="space">
      <div class="space" v-for="(page,index) in pages">
        <Page v-bind:index="index" @get_english="get_book_english_text" @get_chinese="get_book_chinese_text" @get_audio="get_book_audio" @get_picture="get_book_picture"></Page>
      </div>
      <el-button @click="add_page"> 添加新的书页 </el-button>
    </div>
    <div class="card">
      <div class="title space">添加第一个游戏</div>
      <div class="space" v-for="(page,index) in first_selections">
        <First_item v-bind:index="index" @get_text="get_firstgame_text" @get_picture="get_firstgame_picture"></First_item>
      </div>
      <el-button @click="add_first_selection"> 添加新的连线组合 </el-button>
    </div>
    <div class="card">
      <div class="title">添加第二个游戏</div>
      <div class="input-title space">在这里输入单词</div>
      <el-input v-model="second_selections.text"></el-input>
      <div class="input-title space">在这里放入四张图片文件，并选择正确的选项</div>
      <el-radio-group class="space" v-model="second_selections.answer" @change="get_secondgame_answer">
        <el-radio v-for="(item, index) in 4" :label=index>
          <Picture_item v-bind:index=index @get_picture="get_secondgame_picture"></Picture_item>
        </el-radio>
      </el-radio-group>
    </div>
    <div class="card">
      <div class="title">添加第三个游戏</div>
    </div>
    <div class="card">
      <div class="title">添加第四个游戏</div>
      <div class="input-title space">在这里输入单词</div>
      <el-input v-model="fourth_selections.text"></el-input>
      <div class="input-title space">在这里放入四张图片文件，并选择正确的选项</div>
      <el-radio-group class="space" v-model="fourth_selections.answer" @change="get_fourthgame_answer">
        <el-radio v-for="(item, index) in 4" :label=index>
          <Picture_item v-bind:index=index @get_picture="get_fourthgame_picture"></Picture_item>
        </el-radio>
      </el-radio-group>
      <div class="space align">
        <div class="input-title displayed">在这里放入单词的音频</div>
        <input class="file-btn displayed" type="file" accept="audio/*" @change="get_fourthgame_audio">
      </div>
    </div>
    <el-button type="primary" @click="submit"> 上传书籍 </el-button>
  </div>
</template>
<script>
import * as Tools from '../Tools/Tools'
import word from './_word.vue'
import page from './_page.vue'
import axios from 'axios'
import firstgame_selection from './_firstgame_selection.vue'
import picture_selection from './_picture_selection.vue'
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
      pages: [],
      first_selections: [],
      second_selections: {
        text: '',
        answer: 0,
        picture: [null, null, null, null]
      },
      fourth_selections: {
        text: '',
        answer: 0,
        picture: [null, null, null, null],
        audio: null
      }
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
      this.pages.push({
        english_text: '',
        chinese_text: '',
        audio: null,
        picture: null
      })
    },
    add_first_selection: function() {
      this.first_selections.push({
        word: '',
        picture: null
      })
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
    get_firstgame_text: function(obj) {
      this.first_selections[obj.index].text = obj.value
    },
    get_firstgame_picture: function(obj) {
      this.first_selections[obj.index].picture = obj.value
    },
    get_secondgame_picture: function(obj) {
      this.second_selections.picture[obj.index] = obj.value
    },
    get_secondgame_answer: function(value) {
      this.second_selections.answer = value
    },
    get_fourthgame_picture: function(obj) {
      this.fourth_selections.picture[obj.index] = obj.value
    },
    get_fourthgame_audio: function(e) {
      console.log(e.target.files[0])
      this.fourth_selections.audio = e.target.files[0]
    },
    get_fourthgame_answer: function(value) {
      this.fourth_selections.answer = value
    },
    submit: function() {
      if (!confirm('确定要上传所有的内容吗？')) {
        return
      }
      let my_values = new FormData()
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
      for (let i = 0; i < this.pages.length; ++i) {
        my_values.append('book_english_text', this.pages[i].english_text)
        my_values.append('book_chinese_text', this.pages[i].chinese_text)
        my_values.append('book_audio', this.pages[i].audio)
        my_values.append('book_picture', this.pages[i].picture)
      }
      for (let i = 0; i < this.first_selections.length; ++i) {
        my_values.append('first_game_text', this.first_selections[i].text)
        my_values.append('first_game_picture', this.first_selections[i].picture)
      }
      my_values.append('second_game_text', this.second_selections.text)
      my_values.append('second_game_answer', this.second_selections.answer)
      for (let i = 0; i < 4; ++i) {
        my_values.append(
          'second_game_picture',
          this.second_selections.picture[i]
        )
      }
      my_values.append('fourth_game_text', this.fourth_selections.text)
      my_values.append('fourth_game_answer', this.fourth_selections.answer)
      for (let i = 0; i < 4; ++i) {
        my_values.append(
          'fourth_game_picture',
          this.fourth_selections.picture[i]
        )
      }
      my_values.append('fourth_game_audio', this.fourth_selections.audio)
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
    Page: page,
    First_item: firstgame_selection,
    Picture_item: picture_selection
  }
}
</script>
<style>
</style>
