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
        <el-radio v-model="persual" label="persual" border>精读</el-radio>
        <el-radio v-model="persual" label="not_persual" border>泛读</el-radio>
      </div>
      <div class="input-title"> 书籍等级 </div>
      <el-input-number v-model="level" :min="1" :max="MAX_VALUE">
      </el-input-number>
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
        <Word v-bind:index="index" @get_text="get_text"
        @get_audio="get_guide_audio"></Word>
      </div>
      <el-button @click="add_word"> 添加新单词 </el-button>
    </div>
    <div class="space">
      <div class="space" v-for="(page,index) in pages">
        <Page v-bind:index="index" @get_english="get_book_english_text"
        @get_chinese="get_book_chinese_text" @get_audio="get_book_audio"
        @get_picture="get_book_picture"></Page>
      </div>
      <el-button @click="add_page"> 添加新的书页 </el-button>
    </div>
    <div :class="persual">
      <div class="card">
        <div class="title space">添加第一个游戏</div>
        <div class="space" v-for="(page,index) in first_selections">
          <First_item v-bind:index="index" @get_text="get_firstgame_text"
          @get_picture="get_firstgame_picture"></First_item>
        </div>
        <el-button @click="add_first_selection"> 添加新的连线组合 </el-button>
      </div>
      <div class="card">
        <div class="title">添加第二个游戏</div>
        <div class="input-title space">在这里输入单词</div>
        <el-input v-model="second_selections.text"></el-input>
        <div class="input-title space">
          在这里放入四张图片文件，并选择正确的选项
        </div>
        <el-radio-group class="space" v-model="second_selections.answer">
          <el-radio v-for="(item, index) in 4" :label=index>
            <Picture_item v-bind:index=index
            @get_picture="get_secondgame_picture"></Picture_item>
          </el-radio>
        </el-radio-group>
      </div>
      <div class="card">
        <div class="title">添加第三个游戏</div>
        <div class="input-title space">在这里输入单词</div>
        <el-input v-model="third_selections.text"></el-input>
        <div class="space align">
          <div class="input-title displayed">在这里添加图片</div>
          <input type="file" class="file-btn displayed" accept="image/*"
          @change="get_thirdgame_picture">
        </div>
        <div class="space">
          <img v-bind:src="third_selections.picture_addr"
          :class="third_selections.picture?'picture':'hidden'">
        </div>
        <el-radio-group class="space" v-model="third_selections.splits">
          <el-radio :label=2> 分成 4 张图片（2x2） </el-radio>
          <el-radio :label=3> 分成 9 张图片（3x3） </el-radio>
        </el-radio-group>
      </div>
      <div class="card">
        <div class="title">添加第四个游戏</div>
        <div class="input-title space">在这里输入单词</div>
        <el-input v-model="fourth_selections.text"></el-input>
        <div class="input-title space">
          在这里放入四张图片文件，并选择正确的选项
        </div>
        <el-radio-group class="space" v-model="fourth_selections.answer"
        @change="get_fourthgame_answer">
          <el-radio v-for="(item, index) in 4" :label=index>
            <Picture_item v-bind:index=index
            @get_picture="get_fourthgame_picture"></Picture_item>
          </el-radio>
        </el-radio-group>
        <div class="space align">
          <div class="input-title displayed">在这里放入单词的音频</div>
          <input class="file-btn displayed" type="file" accept="audio/*"
          @change="get_fourthgame_audio">
        </div>
      </div>
    </div>
    <div class="card">
      <div class="title">添加阅读拓展</div>
      <div class="input-title space">在这里写下阅读拓展的要求</div>
      <textarea class="texts" v-model="expands"></textarea>
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
      persual: 'not_persual',
      pages: [],
      first_selections: [],
      second_selections: {
        text: '',
        answer: 0,
        picture: [null, null, null, null]
      },
      third_selections: {
        text: '',
        picture: null,
        picture_addr: '',
        splits: 2
      },
      fourth_selections: {
        text: '',
        answer: 0,
        picture: [null, null, null, null],
        audio: null
      },
      expands: ''
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
    get_thirdgame_picture: function(e) {
      this.third_selections.picture = e.target.files[0]
      let reader = new FileReader()
      reader.readAsDataURL(this.third_selections.picture)
      let saved = this
      reader.onload = function(e) {
        saved.third_selections.picture_addr = e.target.result
      }
    },
    get_fourthgame_picture: function(obj) {
      this.fourth_selections.picture[obj.index] = obj.value
    },
    get_fourthgame_audio: function(e) {
      this.fourth_selections.audio = e.target.files[0]
    },
    get_fourthgame_answer: function(value) {
      this.fourth_selections.answer = value
    },
    set_book_info: function(my_values) {
      if (!Tools.check_error(this.bookname, '本书书名', this)) {
        return false
      }
      my_values.append('bookname', this.bookname)
      if (!Tools.check_warning(this.introduction, '本书介绍')) {
        return false
      }
      my_values.append('introduction', this.introduction)
      my_values.append('level', this.level)
      my_values.append('persual', this.persual)
      return true
    },
    set_book_guides: function(my_values) {
      for (let i = 0; i < this.guides.length; ++i) {
        if (
          !Tools.check_error(
            this.guides[i],
            '第 ' + (i + 1) + ' 个本书导读',
            this
          )
        ) {
          return false
        }
        my_values.append('guides', this.guides[i])
      }
      return true
    },
    set_book_knowledges: function(my_values) {
      for (let i = 0; i < this.knowledges.length; ++i) {
        if (
          !Tools.check_error(
            this.knowledges[i],
            '第 ' + (i + 1) + ' 个重点知识',
            this
          )
        ) {
          return false
        }
        my_values.append('knowledges', this.knowledges[i])
      }
      return true
    },
    set_book_words: function(my_values) {
      for (let i = 0; i < this.words.length; ++i) {
        if (
          !Tools.check_error(
            this.words[i].text,
            '第 ' + (i + 1) + ' 个单词的文本内容',
            this
          )
        ) {
          return false
        }
        my_values.append('word_text', this.words[i].text)
        if (
          !Tools.check_error(
            this.words[i].audio,
            '第 ' + (i + 1) + ' 个单词的音频内容',
            this
          )
        ) {
          return false
        }
        my_values.append('word_audio', this.words[i].audio)
      }
      return true
    },
    set_book_pages: function(my_values) {
      if (this.pages.length <= 0) {
        this.$notify({
          title: '警告',
          message: '页数为0，不能上传。请至少添加一页！',
          type: 'warning'
        })
        return false
      }
      for (let i = 0; i < this.pages.length; ++i) {
        if (
          !Tools.check_error(
            this.pages[i].english_text,
            '第 ' + (i + 1) + '页的英文内容',
            this
          )
        ) {
          return false
        }
        my_values.append('book_english_text', this.pages[i].english_text)
        if (
          !Tools.check_warning(
            this.pages[i].chinese_text,
            '第 ' + (i + 1) + '页的中文内容'
          )
        ) {
          return false
        }
        my_values.append('book_chinese_text', this.pages[i].chinese_text)
        if (
          !Tools.check_error(
            this.pages[i].audio,
            '第 ' + (i + 1) + '页的音频内容',
            this
          )
        ) {
          return false
        }
        my_values.append('book_audio', this.pages[i].audio)
        if (
          !Tools.check_error(
            this.pages[i].picture,
            '第 ' + (i + 1) + '页的书籍图片',
            this
          )
        ) {
          return false
        }
        my_values.append('book_picture', this.pages[i].picture)
      }
      return true
    },
    set_book_firstgame: function(my_values) {
      for (let i = 0; i < this.first_selections.length; ++i) {
        if (
          !Tools.check_error(
            this.first_selections[i].text,
            '连线游戏的第 ' + (i + 1) + ' 个单词文本部分',
            this
          )
        ) {
          return false
        }
        my_values.append('first_game_text', this.first_selections[i].text)
        if (
          !Tools.check_error(
            this.first_selections[i].picture,
            '连线游戏的第 ' + (i + 1) + ' 个单词图片部分',
            this
          )
        ) {
          return false
        }
        my_values.append('first_game_picture', this.first_selections[i].picture)
      }
      return true
    },
    set_book_secondgame: function(my_values) {
      if (
        !Tools.check_error(
          this.second_selections.text,
          '看词识图的单词文本部分',
          this
        )
      ) {
        return false
      }
      my_values.append('second_game_text', this.second_selections.text)
      my_values.append('second_game_answer', this.second_selections.answer)
      for (let i = 0; i < 4; ++i) {
        if (
          !Tools.check_error(
            this.second_selections.picture[i],
            '看词识图的第 ' + (i + 1) + ' 个选项的图片',
            this
          )
        ) {
          return false
        }
        my_values.append(
          'second_game_picture',
          this.second_selections.picture[i]
        )
      }
      return true
    },
    set_book_thirdgame: function(my_values) {
      if (
        !Tools.check_warning(
          this.third_selections.text,
          '拼图游戏的单词文本部分'
        )
      ) {
        return false
      }
      my_values.append('third_game_text', this.third_selections.text)
      my_values.append('third_game_splits', this.third_selections.splits)
      if (
        !Tools.check_error(
          this.third_selections.picture,
          '拼图游戏的图片部分',
          this
        )
      ) {
        return false
      }
      my_values.append('third_game_picture', this.third_selections.picture)
      return true
    },
    set_book_fourthgame: function(my_values) {
      if (
        !Tools.check_warning(
          this.fourth_selections.text,
          '听音选图的单词文本部分'
        )
      ) {
        return false
      }
      my_values.append('fourth_game_text', this.fourth_selections.text)
      my_values.append('fourth_game_answer', this.fourth_selections.answer)
      for (let i = 0; i < 4; ++i) {
        if (
          !Tools.check_error(
            this.fourth_selections.picture[i],
            '听音选图的第 ' + (i + 1) + ' 个选项的图片',
            this
          )
        ) {
          return false
        }
        my_values.append(
          'fourth_game_picture',
          this.fourth_selections.picture[i]
        )
      }
      if (
        !Tools.check_error(
          this.fourth_selections.audio,
          '听音选图的音频内容',
          this
        )
      ) {
        return false
      }
      my_values.append('fourth_game_audio', this.fourth_selections.audio)
      return true
    },
    set_book_expand: function(my_values) {
      if (!Tools.check_warning(this.expands, '阅读拓展的内容')) {
        return false
      }
      my_values.append('expand', this.expands)
      return true
    },
    upload: function(my_values) {
      let saved = this
      axios
        .post(Tools.get_url() + 'get_book', my_values)
        .then(function(response) {
          saved.$notify({
            title: '上传成功！',
            position: 'bottom-right',
            type: 'success'
          })
        })
    },
    submit: function() {
      if (!confirm('确定要上传所有的内容吗？')) {
        return
      }
      let my_values = new FormData()
      if (this.set_book_info(my_values) === false) {
        return
      }
      if (this.set_book_guides(my_values) === false) {
        return
      }
      if (this.set_book_knowledges(my_values) === false) {
        return
      }
      if (this.set_book_words(my_values) === false) {
        return
      }
      if (this.set_book_pages(my_values) === false) {
        return
      }
      if (this.persual === 'persual') {
        if (this.set_book_firstgame(my_values) === false) {
          return
        }
        if (this.set_book_secondgame(my_values) === false) {
          return
        }
        if (this.set_book_thirdgame(my_values) === false) {
          return
        }
        if (this.set_book_fourthgame(my_values) === false) {
          return
        }
      }
      if (this.set_book_expand(my_values) === false) {
        return
      }
      this.upload(my_values)
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
.persual {
  display: inline;
}
.not_persual {
  display: none;
}
</style>
