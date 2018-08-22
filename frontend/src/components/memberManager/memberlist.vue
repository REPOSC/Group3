<template>
  <div class="card">
    <el-table :data="tableData">
      <el-table-column prop="user_number" label="账号">
      </el-table-column>
      <el-table-column prop="user_name" label="姓名">
      </el-table-column>
    </el-table>
    <div class="Pagination">
      <el-pagination @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="currentPage" :page-size="20" layout="total, prev, pager, next" :total="count">
      </el-pagination>
    </div>
  </div>
</template>

<script>
import * as Tools from '../Tools/Tools'
import axios from 'axios'
export default {
  data() {
    return {
      tableData: [],
      currentRow: null,
      offset: 0,
      limit: 20,
      count: 0,
      currentPage: 1
    }
  },

  created: function() {
    let saved = this
    axios.post(Tools.get_url() + 'get_managers', null).then(function(response) {
      let user_names = eval(response.data.user_names)
      let user_numbers = eval(response.data.user_numbers)
      for (let i = 0; i < user_numbers.length; ++i) {
        saved.tableData.push({
          user_number: user_numbers[i],
          user_name: user_names[i]
        })
      }
    })
  }
}
</script>
