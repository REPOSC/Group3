<!--suppress ALL -->
<template>
  <div>
    <!--为echarts准备一个具备大小的容器dom-->
    <div class="card  demonstration">
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
      <el-table :data="tableData.slice((currpage - 1) * pagesize, currpage * pagesize)" align="center">
        <el-table-column prop="user_name" label="账号" sortable width="200">
        </el-table-column>
        <el-table-column prop="user_nickname" label="姓名" sortable width="200">
        </el-table-column>
        <el-table-column prop="level" label="等级" sortable width="200">
        </el-table-column>
        <el-table-column prop="book" label="阅读数量" sortable width="200">
        </el-table-column>
        <el-table-column fixed="right" label="操作" width="200">
          <template slot-scope="scope">
            <el-button @click="handleClick(scope.row)" type="text" size="small">查看</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-pagination background layout="prev, pager, next, sizes, total, jumper" :page-sizes="[5, 10, 15, 20]" :page-size="pagesize" :total="tableData.length" @current-change="handleCurrentChange" @size-change="handleSizeChange">
      </el-pagination>
    </div>
  </div>

</template>
<script>
import echarts from 'echarts'
import axios from 'axios'
import * as Tools from '../Tools/Tools'

export default {
  name: '',
  data() {
    return {
      msg: 8888,
      pagesize: 10,
      currpage: 1,
      chart: null,
      search_method: 1,
      charts: '',
      opinion: ['直接访问', '邮件营销', '联盟广告', '视频广告', '搜索引擎'],
      opinionData: [
        { value: 335, name: '直接访问' },
        { value: 310, name: '邮件营销' },
        { value: 234, name: '联盟广告' },
        { value: 135, name: '视频广告' },
        { value: 1548, name: '搜索引擎' }
      ],
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
    handleCurrentChange(cpage) {
      this.currpage = cpage
    },
    handleSizeChange(psize) {
      this.pagesize = psize
    },
    drawPie(id) {
      this.charts = echarts.init(document.getElementById(id))
      this.charts.setOption({
        tooltip: {
          trigger: 'item',
          formatter: '{a}<br/>{b}:{c} ({d}%)'
        },
        legend: {
          orient: 'vertical',
          x: 'left',
          data: this.opinion
        },
        series: [
          {
            name: '访问来源',
            type: 'pie',
            radius: ['50%', '70%'],
            avoidLabelOverlap: false,
            label: {
              normal: {
                show: false,
                position: 'center'
              },
              emphasis: {
                show: true,
                textStyle: {
                  fontSize: '30',
                  fontWeight: 'blod'
                }
              }
            },
            labelLine: {
              normal: {
                show: false
              }
            },
            data: this.opinionData
          }
        ]
      })
    },
    initChart() {
      this.chart = echarts.init(this.$refs.myEchart)
      // 把配置和数据放这里
      this.chart.setOption({
        color: ['#3398DB'],
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            // 坐标轴指示器，坐标轴触发有效
            type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
          }
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        xAxis: [
          {
            type: 'category',
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            axisTick: {
              alignWithLabel: true
            }
          }
        ],
        yAxis: [
          {
            type: 'value'
          }
        ],
        series: [
          {
            name: '直接访问',
            type: 'bar',
            barWidth: '60%',
            data: [10, 52, 200, 334, 390, 330, 220]
          }
        ]
      })
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
          if (value.user_name.indexOf(this.TableDataName) >= 0) {
            this.tableData.push(value)
          }
        } else if (saved.search_method === 0) {
          if (value.user_nickname.indexOf(this.TableDataName) >= 0) {
            this.tableData.push(value)
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
    this.$nextTick(function() {
      this.drawPie('main')
    })
    this.initChart()
    this.chushi()
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
