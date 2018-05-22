<template>
  <div class="clean">
    <mt-checklist
      title="复选框列表"
      v-model="value"
      :options="['选项A', '选项B', '选项C']">
    </mt-checklist>
  </div>
</template>
<script>
import { Checklist } from 'mint-ui';
export default {
  data () {
    return {
      value:[]
    }
  },
  components:{
    'mt-checklist': Checklist
  },
  props: {},
  watch: {
  
  },
  methods: {
   
  },
  filters: {},
  computed: {
   
  },
  created () {

  },
  mounted () {
  }
}
</script>

<style lang="less" scoped>

</style>