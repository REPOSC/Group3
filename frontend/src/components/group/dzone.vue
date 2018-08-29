<template >
  <div id="APP">
    <div>
      <div class="head">
        <el-input
          v-model="tableDataName"
          placeholder="请输入账号"
          class="wide"
        ></el-input>
        <el-button type="primary" @click="doFilter">搜索</el-button>
        <el-button type="primary" @click="doback">返回</el-button>
      </div>&nbsp;&nbsp;
      <div class="block head file-btn">
        <span class="demonstration">带快捷选项</span>
        <el-date-picker
          v-model="visitDate"
          value-format="yyyy-MM-dd"
          type="daterange"
          align="right"
          unlink-panels range-separator="至"
          start-placeholder="开始日期" end-placeholder="结束日期"
          :picker-options="pickerOptions2"
        >
        </el-date-picker>
        <el-button type="primary" @click="doFilter2">搜索</el-button>
        <el-button type="primary" @click="doback">返回</el-button>
      </div>
    </div>
    <qkj-body>
      <zone
        v-bind:items="item"
        class="all" align="center"
        @dakalist="dakalist"
        v-for="item in my_texts"
        ></zone>
      <!--将item双向绑定item为打卡分享中的每一项-->
      <div>
        <el-pagination
          background layout="prev, pager, next, sizes, total, jumper"
          :page-sizes="[5, 10, 15, 20]"
          :page-size="pagesize"
          :total="this.tableData.length"
          @current-change="handleCurrentChange"
          @size-change="handleSizeChange"
        >
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
      all_tabledata: null,
      tableData1: [],
      tableDataName: '',
      filterTableData: [],
      my_texts: [],
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
      this.my_texts = this.tableData.slice(
        (this.currpage - 1) * this.pagesize,
        this.currpage * this.pagesize
      )
    },
    doFilter() {
      if (this.tableDataName === '') {
        this.$notify.error({
          title: '错误',
          message: '查询条件不能为空！'
        })
        return
      }
      this.tableData = []
      let saved = this
      saved.all_tabledata.forEach((value, index) => {
        if (String(value.user_name).indexOf(saved.tableDataName) >= 0) {
          saved.tableData.push(value)
        }
      })
      this.pagesize = 10
      this.currpage = 1
      this.change()
    },
    doback() {
      this.tableData = this.all_tabledata
      this.pagesize = 10
      this.currpage = 1
      this.tableDataName = ''
      this.change()
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
      this.tableData = []
      let saved = this
      saved.all_tabledata.forEach((value, index) => {
        let newdate = parseInt(
          value.riqi.slice(0, 4) +
            value.riqi.slice(5, 7) +
            value.riqi.slice(8, 10)
        )
        if (newdate <= data2 && newdate >= data1) {
          this.tableData.push(value)
        }
      })
      this.pagesize = 10
      this.currpage = 1
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
        let booknums = eval(response.data.booknums)
        let names = eval(response.data.usernums)
        let comments = eval(response.data.comments)
        let riqis = eval(response.data.riqis)
        let likenums = eval(response.data.likenums)
        for (let i = 0; i < names.length; ++i) {
          saved.tableData.push({
            like_num: likenums[i],
            book_num: booknums[i],
            user_name: names[i],
            commenting: comments[i],
            riqi: riqis[i]
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
