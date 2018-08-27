<!--suppress ALL -->
<template >
  <div id="APP">
    <div>
      <div class="head">
        <el-input v-model="tableDataName" placeholder="请输入账号" style="width:240px"></el-input>
        <el-button type="primary" @click="doFilter">搜索</el-button>
        <el-button type="primary" @click="doFilter1">返回</el-button>
      </div>&nbsp;&nbsp;
      <div class="block head file-btn">
        <span class="demonstration">带快捷选项</span>
        <el-date-picker v-model="visitDate" value-format="yyyy-MM-dd" type="daterange" align="right" unlink-panels range-separator="至" start-placeholder="开始日期" end-placeholder="结束日期" :picker-options="pickerOptions2" @change="getTime">
        </el-date-picker>
        <el-button type="primary" @click="doFilter2">搜索</el-button>
        <el-button type="primary" @click="doFilter3">返回</el-button>
      </div>
    </div>
    <qkj-body>
      <zone v-bind:items="item" class="all" align="center" v-for="item in my_texts"></zone>
      <!--将item双向绑定item为打卡分享中的每一项-->
      <div>
        <el-pagination background layout="prev, pager, next, sizes, total, jumper" :page-sizes="[5, 10, 15, 20]" :page-size="pagesize" :total="this.tableData.length" @current-change="handleCurrentChange" @size-change="handleSizeChange">
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
      visitDate: ['', ''], // 日期
      tableData: [],
      tableData1: [],
      tableDataName: '',
      filterTableData: [],
      my_texts: '',
      pagesize: 10,
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
      value7: ''
    }
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
      if (this.tableDataName === '') {
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
      this.pagesize = 5
      this.currpage = 1
      this.tableData = this.filterTableData
    },
    doFilter1() {
      this.tableData = this.tableData1
      this.pagesize = 10
      this.currpage = 1
      this.TableDataName = ''
    },
    doFilter2() {
      this.tableData1 = this.tableData
      if (this.visitDate[0] === '' || this.visitDate[1] === '') {
        this.$message.warning('查询条件不能为空！')
        return
      }

      let data1 = parseInt(
        this.visitDate[0].slice(0, 4) +
          this.visitDate[0].slice(5, 7) +
          this.visitDate[0].slice(8, 10)
      )
      let data2 = parseInt(
        this.visitDate[1].slice(0, 4) +
          this.visitDate[1].slice(5, 7) +
          this.visitDate[1].slice(8, 10)
      )
      alert(data1)
      alert(data2)
      // 每次手动将数据置空,因为会出现多次点击搜索情况
      this.filterTableData = []
      this.tableData.forEach((value, index) => {
        let newdate = parseInt(
          this.value.riqi.slice(0, 4) +
            this.value.riqi.slice(5, 7) +
            this.value.riqi.slice(8, 10)
        )
        if (newdate < data2 && newdate > data1) {
          this.filterTableData.push(value)
        }
      })
      // 页面数据改变重新统计数据数量和当前页
      this.pagesize = 10
      this.currpage = 1
      this.tableData = this.filterTableData
    },
    doFilter3() {
      this.tableData = this.tableData1
      this.pagesize = 10
      this.currpage = 1
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
        let booknums = eval(response.data.booknums)
        let names = eval(response.data.usernums)
        let conents = eval(response.data.conents)
        let riqis = eval(response.data.riqis)
        let likenums = eval(response.data.likenums)
        for (let i = 0; i < names.length; ++i) {
          saved.tableData.push({
            like_num: likenums[i],
            book_num: booknums[i],
            user_name: names[i],
            commenting: conents[i],
            riqi: riqis[i]
          })
        }
      })
    }
  },
  mounted: function() {
    this.dakalist()
    this.change()
    let nowDate = new Date()
    let year = nowDate.getFullYear()
    let month = nowDate.getMonth() + 1
    let day = nowDate.getDate()
    let endTime = `${year}-${month}-${day}`
    this.nowTime = endTime // 当前的时间点
    let befDate = new Date(nowDate.getTime() - 7 * 24 * 3600 * 1000)
    let byear = befDate.getFullYear()
    let bmonth = befDate.getMonth() + 1
    let bday = befDate.getDate()
    let startTime = `${byear}-${bmonth}-${bday}`
    this.weekBeforeTime = startTime // 向前推迟一周的时间点
    this.visitDate = [
      new Date(byear + ', ' + bmonth + ', ' + bday),
      new Date(year + ', ' + month + ', ' + day)
    ]
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
