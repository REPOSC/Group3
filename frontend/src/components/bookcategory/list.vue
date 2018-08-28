<!--suppress ALL -->
<template>
  <div>
    <!--为echarts准备一个具备大小的容器dom-->
    <div class="card demonstration">
      <div>
        <el-input v-model="TableDataName" :placeholder="search_method?'账号':'书名'" class="searchbox"></el-input>
        <el-button type="primary" @click="doFilter">搜索</el-button>
        <el-button type="primary" @click="doBack">返回</el-button>
        <div class="space">
          <el-radio-group v-model="search_method">
            <el-radio :label="1">按账号查找</el-radio>
            <el-radio :label="0">按书名查找</el-radio>
          </el-radio-group>
        </div>
      </div>
      <el-table :data="tableData.slice((currpage - 1) * pagesize, currpage * pagesize)" align="center">
        <el-table-column prop="book_number" label="书目编号" sortable>
        </el-table-column>
        <el-table-column prop="book_name" label="书名" sortable>
        </el-table-column>
        <el-table-column prop="level" label="等级" sortable>
        </el-table-column>
        <el-table-column prop="persual" label="精读/泛读" sortable>
        </el-table-column>
        <el-table-column prop="reading" label="浏览过" sortable>
        </el-table-column>
        <el-table-column prop="readed" label="已完成" sortable>
        </el-table-column>
        <el-table-column fixed="right" label="操作">
          <template slot-scope="scope">
            <el-button @click="handleClick(scope.row)" type="text" size="small">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-pagination background layout="prev, pager, next, sizes, total, jumper" :page-sizes="[5, 10, 15, 20]" :page-size="pagesize" :total="tableData.length" @current-change="handleCurrentChange" @size-change="handleSizeChange">
      </el-pagination>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
import * as Tools from '../Tools/Tools'
import qs from 'qs'
export default {
  name: '',
  data() {
    return {
      msg: 8888,
      pagesize: 10,
      currpage: 1,
      chart: null,
      charts: '',
      tableData: [],
      TableDataName: '',
      search_method: 1
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
      this.deletebook(row.book_number)
    },
    handleCurrentChange(cpage) {
      this.currpage = cpage
    },
    handleSizeChange(psize) {
      this.pagesize = psize
    },
    booklist() {
      let saved = this
      this.$notify.info({
        title: '请等待',
        message: '正在初始化数据，请耐心等候……'
      })
      axios.post(Tools.get_url() + 'all_book', null).then(function(response) {
        saved.tableData = []
        let names = eval(response.data.book_name)
        let nums = eval(response.data.book_number)
        let levels = eval(response.data.level)
        let readings = eval(response.data.reading)
        let readeds = eval(response.data.readed)
        let persuals = eval(response.data.persual)
        for (let i = 0; i < names.length; ++i) {
          saved.tableData.push({
            book_name: names[i],
            book_number: nums[i],
            level: levels[i],
            persual: persuals[i],
            reading: readings[i],
            readed: readeds[i]
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
          if (String(value.book_number).indexOf(saved.TableDataName) >= 0) {
            saved.tableData.push(value)
          }
        } else if (saved.search_method === 0) {
          if (value.book_name.indexOf(saved.TableDataName) >= 0) {
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
    },
    deletebook(booknumber) {
      if (!confirm('删除书籍后无法恢复，确认要删除吗？')) {
        return
      }
      let saved = this
      axios
        .post(
          Tools.get_url() + 'del_book',
          qs.stringify({
            book_number: booknumber
          })
        )
        .then(function(response) {
          if (response.data.success === 'true') {
            saved.$notify({
              title: '成功',
              message: '删除书籍成功！',
              type: 'success',
              position: 'bottom-right'
            })
          } else {
            saved.$notify.error({
              title: '失败',
              message: '删除失败！'
            })
          }
          saved.booklist()
        })
    }
  },
  mounted() {
    this.booklist()
  }
}
</script>
<style scoped>
.login-container.chart {
  margin: auto auto 40px;
  height: 600px;
}
.login-container {
  -webkit-border-radius: 5px;
  border-radius: 5px;
  -moz-border-radius: 5px;
  background-clip: padding-box;
  margin: 180px auto;
  width: 80%;
  padding: 35px 35px 15px 35px;
  background: #fff;
  border: 1px solid #eaeaea;
  box-shadow: 0 0 25px #cac6c6;
}
.column {
  width: 80%;
  height: 80%;
}
.searchbox {
  width: 240px;
}
</style>
