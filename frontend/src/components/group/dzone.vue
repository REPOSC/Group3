<!--suppress ALL -->
<template >
  <div id="APP">
    <div>
      <div class="head">
        <el-input v-model="TableDataName" placeholder="请输入账号" style="width:240px"></el-input>
        <el-button type="primary" @click="doFilter">搜索</el-button>
        <el-button type="primary" @click="doFilter1">返回</el-button>
      </div>&nbsp;&nbsp;
      <div class="block head">
        <span class="demonstration">带快捷选项</span>
        <el-date-picker v-model="value7" type="daterange" align="right" unlink-panels range-separator="至" start-placeholder="开始日期" end-placeholder="结束日期" :picker-options="pickerOptions2">
        </el-date-picker>
      </div>
    </div>
    <qkj-body>
      <zone v-bind:items="item" class="all" align="center" v-for="item in my_texts"></zone>
      <div>
        <el-pagination background layout="prev, pager, next, sizes, total, jumper" :page-sizes="[5, 10, 15, 20]" :page-size="pagesize" :total="tabledate.length" @current-change="handleCurrentChange" @size-change="handleSizeChange">
        </el-pagination>
      </div>
    </qkj-body>
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
      tabledate: [],
      my_texts: '',
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
      },
      value6: '',
      value7: ''
    }
  },
  mounted: function() {
    this.dakalist()
    this.change()
  },
  methods: {
    change() {
      this.my_texts = this.tabledate.slice(
        (this.currpage - 1) * this.pagesize,
        this.currpage * this.pagesize
      )
    },
    doFilter() {
      this.tableData1 = this.tableData
      if (this.TableDataName === '') {
        this.$message.warning('查询条件不能为空！')
        return
      }
      // 每次手动将数据置空,因为会出现多次点击搜索情况
      this.filterTableData = []
      this.tableData.forEach((value, index) => {
        if (value.user_name) {
          if (value.user_name.indexOf(this.TableDataName) >= 0) {
            this.filterTableData.push(value)
          }
        }
      })
      // 页面数据改变重新统计数据数量和当前页
      this.pagesize = 10
      this.currpage = 1
      this.tableData = this.filterTableData
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
        let booknums = eval(response.data.book_number_ids)
        let names = eval(response.data.user_names)
        // let comments = eval(response.data.comments)
        let riqis = eval(response.data.riqis)
        let likenums = eval(response.data.likenums)
        for (let i = 0; i < names.length; ++i) {
          saved.tableData.push({
            like_nums: likenums[i],
            book_num: booknums[i],
            user_name: names[i],
            // commenting: comments[i],
            riqi: riqis[i]
          })
        }
      })
    }
  }
}
</script>
<style>
.all {
  width: 100%;
  background: #fff;
}
#APP {
  width: 90%;
  height: auto;
}
.head {
  position: relative;
  display: inline;
}
</style>
