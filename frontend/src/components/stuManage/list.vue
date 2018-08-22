<!--suppress ALL -->
<template>
  <div>
    <!--为echarts准备一个具备大小的容器dom-->
    <div class="login-container demonstration">
      <!--<el-input placeholder="请输入查找的账户" icon="search" v-model="schfilter" v-on:change="find" class="search-input">-->
      <!--</el-input>-->
      <div class="searchWord">
        <div style="display: inline-block"> 搜索：</div>
        <el-input v-model="search" style="display: inline-block;width: 1300px" placeholder="请输入搜索内容">
        </el-input>
      </div>
      <el-table :data="tableData.slice((currpage - 1) * pagesize, currpage * pagesize)" align="center">
        <el-table-column prop="user_name" label="账号" sortable width="180">
        </el-table-column>
        <el-table-column prop="user_nickname" label="姓名" sortable width="180">
        </el-table-column>
        <el-table-column prop="user_level" label="等级" sortable width="180">
        </el-table-column>
        <el-table-column prop="book_num" label="阅读数量" sortable width="180">
        </el-table-column>
        <el-table-column fixed="right" label="操作" width="180">
          <template slot-scope="scope">
            <el-button @click="handleClick(scope.row)" type="text" size="small">查看</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-pagination background layout="prev, pager, next, sizes, total, jumper" :page-sizes="[5, 10, 15, 20]" :page-size="pagesize" :total="tableData.length" @current-change="handleCurrentChange" @size-change="handleSizeChange">
      </el-pagination>
    </div>
    <div class="login-container chart" id="main"></div>
    <div :class="className" :id="id" class="login-container chart column" ref="myEchart"></div>
  </div>
</template>
<script>
import echarts from 'echarts'
import axios from 'axios'
import * as Tools from '../Tools/Tools'

export default {
  props: {
    className: {
      type: String,
      default: 'yourClassName'
    },
    id: {
      type: String,
      default: 'yourID'
    }
  },
  name: '',
  data() {
    return {
      msg: 8888,
      pagesize: 10,
      currpage: 1,
      chart: null,
      charts: '',
      opinion: ['直接访问', '邮件营销', '联盟广告', '视频广告', '搜索引擎'],
      opinionData: [
        { value: 335, name: '直接访问' },
        { value: 310, name: '邮件营销' },
        { value: 234, name: '联盟广告' },
        { value: 135, name: '视频广告' },
        { value: 1548, name: '搜索引擎' }
      ],
      tableData: []
    }
  },
  watch: {
    schfilter: function(val, oldVal) {
      this.tableData = this.otableData.filter(
        item => ~item.user_name.indexOf(val)
      )
    }
  },
  tables() {
    const search = this.search
    if (search) {
      // filter() 方法创建一个新的数组，新数组中的元素是通过检查指定数组中符合条件的所有元素。
      // 注意： filter() 不会对空数组进行检测。
      // 注意： filter() 不会改变原始数组。
      return this.dormitory.filter(data => {
        // some() 方法用于检测数组中的元素是否满足指定条件;
        // some() 方法会依次执行数组的每个元素：
        // 如果有一个元素满足条件，则表达式返回true , 剩余的元素不会再执行检测;
        // 如果没有满足条件的元素，则返回false。
        // 注意： some() 不会对空数组进行检测。
        // 注意： some() 不会改变原始数组。
        return Object.keys(data).some(key => {
          // indexOf() 返回某个指定的字符在某个字符串中首次出现的位置，如果没有找到就返回-1；
          // 该方法对大小写敏感！所以之前需要toLowerCase()方法将所有查询到内容变为小写。
          return (
            String(data[key])
              .toLowerCase()
              .indexOf(search) > -1
          )
        })
      })
    }
    return this.dormitory
  },
  methods: {
    handleCurrentChange(cpage) {
      this.currpage = cpage
    },
    handleSizeChange(psize) {
      this.pagesize = psize
    },
    f: function() {
      this.tableData = this.otableData.filter(
        item => ~item.user_name.indexOf(this.text)
      )
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
      axios
        .post(Tools.get_url() + 'all_student', null)
        .then(function(response) {
          let nicknames = eval(response.data.user_nicknames)
          let names = eval(response.data.user_numbers)
          for (let i = 0; i < nicknames.length; ++i) {
            saved.tableData.push({
              user_nickname: nicknames[i],
              user_name: names[i]
            })
          }
        })
    },
    handleClick(row) {
      let saved = this
      let value = row.user_name
      axios
        .post(Tools.get_url() + 'all_student', value)
        .then(function(response) {
          let nicknames = eval(response.data.user_nicknames)
          let names = eval(response.data.user_numbers)
          for (let i = 0; i < nicknames.length; ++i) {
            saved.tableData.push({
              user_nickname: nicknames[i],
              user_name: names[i]
            })
          }
        })
    }
  },
  // 调用
  mounted() {
    this.$nextTick(function() {
      this.drawPie('main')
    })
    this.initChart()
    this.stulist()
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
</style>
