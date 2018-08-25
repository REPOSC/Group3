<template>
  <input class="file-btn" type="file" accept="image/*" @change="get_picture">
</template>
<script>
export default {
  props: ['index'],
  methods: {
    get_picture: function(e) {
      let picture = e.target.files[0]
      this.$emit('get_picture', { index: this.index, value: picture })
    }
  }
}
</script>
<style scoped>
</style>
