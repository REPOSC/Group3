<template >
  <div>
    <div class="card">
      <div>
        <el-input v-model="tableDataName" placeholder="请输入账号"
        class="wide"></el-input>
        <span class="demonstration">带快捷选项</span>
        <el-date-picker v-model="visitDate" value-format="yyyy-MM-dd"
        type="daterange" align="right" unlink-panels range-separator="至"
        start-placeholder="开始日期" end-placeholder="结束日期"
        :picker-options="pickerOptions2">
        </el-date-picker>
        <el-button type="primary" @click="doFilter">搜索</el-button>
        <el-button type="primary" @click="doback">返回</el-button>
      </div>
    </div>
    <div>
      <zone v-bind:items="item" class="card" align="center"
      @dakalist="dakalist" v-for="item in my_texts"></zone>
      <div>
        <el-pagination background layout="prev, pager, next, sizes, total,
        jumper" :page-sizes="[5, 10, 15, 20]" :page-size="pagesize"
        :total="this.tableData.length" @current-change="handleCurrentChange"
        @size-change="handleSizeChange">
        </el-pagination>
      </div>
    </div>
  </div>
</template>
<script>
import Zone from './zone'
import QkjBody from '@/components/QkjBody/QkjBody.vue'
import axios from 'axios'
import * as Tools from '../Tools/Tools'
export default {
  components: { Zone, QkjBody },
  data() {
    return {
      visitDate: ['', ''], // 日期
      tableData: [],
      all_tabledata: null,
      tableData1: [],
      tableDataName: '',
      filterTableData: [],
      my_texts: [],
      pagesize: 5,
      currpage: 1,
      showAll: false,
      pickerOptions2: {
        shortcuts: [
          {
            text: '最近一周',
            onClick(picker) {
              const end = new Date()
              const start = new Date()
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 7)
              picker.$emit('pick', [start, end])
            }
          },
          {
            text: '最近一个月',
            onClick(picker) {
              const end = new Date()
              const start = new Date()
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 30)
              picker.$emit('pick', [start, end])
            }
          },
          {
            text: '最近三个月',
            onClick(picker) {
              const end = new Date()
              const start = new Date()
              start.setTime(start.getTime() - 3600 * 1000 * 24 * 90)
              picker.$emit('pick', [start, end])
            }
          }
        ]
      }
    }
  },
  methods: {
    change() {
      this.my_texts = this.tableData.slice(
        (this.currpage - 1) * this.pagesize,
        this.currpage * this.pagesize
      )
    },
    search_for_name(searching_table_data) {
      let saved = this
      if (this.tableDataName === '') {
        return searching_table_data
      }
      let temp_table_data = []
      searching_table_data.forEach((value, index) => {
        if (String(value.user_name).indexOf(saved.tableDataName) >= 0) {
          temp_table_data.push(value)
        }
      })
      return temp_table_data
    },
    search_for_date(searching_table_data) {
      let saved = this
      if (this.not_visitDate()) {
        return searching_table_data
      }
      let temp_table_data = []
      let begin_time_strs = saved.visitDate[0].split('-')
      let time_begin = parseInt(
        begin_time_strs[0] + begin_time_strs[1] + begin_time_strs[2]
      )
      let end_time_strs = saved.visitDate[1].split('-')
      let time_end = parseInt(
        end_time_strs[0] + end_time_strs[1] + end_time_strs[2]
      )
      searching_table_data.forEach((value, index) => {
        if (value.time >= time_begin && value.time <= time_end) {
          temp_table_data.push(value)
        }
      })
      return temp_table_data
    },
    not_visitDate() {
      return (
        this.visitDate === null ||
        (this.visitDate[0] === '' && this.visitDate[1] === '')
      )
    },
    doFilter() {
      if (this.tableDataName === '' && this.not_visitDate()) {
        this.$notify.error({
          title: '错误',
          message: '查询条件不能为空！'
        })
        return
      }
      this.tableData = this.search_for_name(
        this.search_for_date(this.all_tabledata)
      )
      this.currpage = 1
      this.change()
    },
    doback() {
      this.tableData = this.all_tabledata
      this.currpage = 1
      this.tableDataName = ''
      this.change()
    },
    handleCurrentChange(cpage) {
      this.currpage = cpage
      this.change()
    },
    handleSizeChange(psize) {
      this.pagesize = psize
      this.change()
    },
    dakalist() {
      let saved = this
      axios.post(Tools.get_url() + 'all_daka', null).then(function(response) {
        let booknums = response.data.booknums
        let booknames = response.data.booknames
        let names = response.data.usernums
        let comments = response.data.comments
        let times = response.data.times
        let likenums = response.data.likenums
        for (let i = 0; i < names.length; ++i) {
          saved.tableData.push({
            like_num: likenums[i],
            book_num: booknums[i],
            book_name: booknames[i],
            user_name: names[i],
            article: comments[i],
            time: parseInt(times[i])
          })
        }
        saved.all_tabledata = saved.tableData
        saved.change()
      })
    }
  },
  mounted: function() {
    this.dakalist()
  }
}
</script>
<style>
.wide {
  width: 240px;
}

.head {
  position: relative;
  display: inline;
}
</style>
