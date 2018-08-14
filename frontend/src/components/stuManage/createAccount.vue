<template>
  <div class="signup">
    <Layout><Sider><Home/></Sider>
      <Layout class="content">
        <div class="member">
          <label>添加人数</label>
          <Input type="number" style="width: 180px"/>
          <br><br>
          <label>选择等级</label>
          <Select style="width:180px">
            <Option>等级1</Option>
            <Option>等级2</Option>
            <Option>等级3</Option>
            <Option>等级4</Option>
          </Select>
          <br><br><br><br>
          <Button class="add">添加</Button>
        </div>
      </Layout>
    </Layout>
  </div>
</template>

<script>
import Home from '@/components/Home'

export default {
  components: {
    Home
  }
}
</script>

<style scoped>
.content {
  background-color: #fff
}
.member {
  padding-top: 100px
}
.add {
  width: 80px
}
</style>
