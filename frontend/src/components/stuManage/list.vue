<template>
  <div>
    <div class="card demonstration">
      <div class="title space">学生数据统计</div>
      <div>
        <el-input v-model="TableDataName" :placeholder="search_method?'账号':'昵称'" class="searchbox"></el-input>
        <el-button type="primary" @click="doFilter">搜索</el-button>
        <el-button type="primary" @click="doBack">返回</el-button>
        <div class="space">
          <el-radio-group v-model="search_method">
            <el-radio :label="1">按账号查找</el-radio>
            <el-radio :label="0">按昵称查找</el-radio>
          </el-radio-group>
        </div>
      </div>
      <el-table :data="tableData.slice((currpage - 1) * pagesize, currpage *
      pagesize)" align="center">
        <el-table-column prop="user_name" label="账号" sortable>
        </el-table-column>
        <el-table-column prop="user_nickname" label="昵称" sortable>
        </el-table-column>
        <el-table-column prop="level" label="等级" sortable>
        </el-table-column>
        <el-table-column prop="book" label="阅读数量" sortable>
        </el-table-column>
        <el-table-column fixed="right" label="查看详情">
          <template slot-scope="scope">
            <el-button @click="handleClick(scope.row)" type="text" size="small">
              查看</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-pagination background layout="prev, pager, next, sizes, total,
      jumper" :page-sizes="[5, 10, 15, 20]" :page-size="pagesize"
      :total="tableData.length" @current-change="handleCurrentChange"
      @size-change="handleSizeChange">
      </el-pagination>
    </div>
  </div>

</template>
<script>
import axios from 'axios'
import * as Tools from '../Tools/Tools'

export default {
  name: '',
  data() {
    return {
      msg: 8888,
      pagesize: 10,
      currpage: 1,
      search_method: 1,
      charts: '',
      tableData: [],
      TableDataName: '',
      all_tabledata: null
    }
  },
  watch: {
    schfilter: function(val, oldVal) {
      this.tableData = this.otableData.filter(
        item => ~item.user_name.indexOf(val)
      )
    }
  },
  methods: {
    handleClick(row) {
      this.$router.push({
        name: '查看学生详情',
        params: { name: row.user_name }
      })
    },
    handleCurrentChange(cpage) {
      this.currpage = cpage
    },
    handleSizeChange(psize) {
      this.pagesize = psize
    },
    stulist() {
      let saved = this
      this.$notify.info({
        title: '请等待',
        message: '正在初始化数据，请耐心等候……'
      })
      axios
        .post(Tools.get_url() + 'all_student', null)
        .then(function(response) {
          let nicknames = eval(response.data.user_nicknames)
          let names = eval(response.data.user_numbers)
          let levels = eval(response.data.levelss)
          let books = eval(response.data.booknums)
          for (let i = 0; i < nicknames.length; ++i) {
            saved.tableData.push({
              user_nickname: nicknames[i],
              user_name: names[i],
              level: levels[i],
              book: books[i]
            })
          }
          saved.$notify({
            title: '初始化成功！',
            type: 'success',
            position: 'bottom-right'
          })
          saved.all_tabledata = saved.tableData
        })
    },
    doFilter() {
      if (this.TableDataName === '') {
        this.$notify.error({
          title: '错误',
          message: '查询条件不能为空！'
        })
        return
      }
      this.tableData = []
      let saved = this
      this.all_tabledata.forEach((value, index) => {
        if (saved.search_method === 1) {
          if (value.user_name.indexOf(saved.TableDataName) >= 0) {
            saved.tableData.push(value)
          }
        } else if (saved.search_method === 0) {
          if (value.user_nickname.indexOf(saved.TableDataName) >= 0) {
            saved.tableData.push(value)
          }
        }
      })
      this.pagesize = 10
      this.currpage = 1
    },
    doBack() {
      this.tableData = this.all_tabledata
      this.pagesize = 10
      this.currpage = 1
      this.TableDataName = ''
    }
  },
  mounted() {
    this.stulist()
  }
}
</script>
<style scoped>
.login-container.chart {
  margin: auto auto 40px;
  height: 600px;
}
.column {
  width: 80%;
  height: 80%;
}
.searchbox {
  width: 240px;
}
</style>
