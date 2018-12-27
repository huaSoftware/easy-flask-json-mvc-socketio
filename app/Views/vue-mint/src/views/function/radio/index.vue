<template>
  <div class="clean">
    <mt-radio
      title="单选框列表"
      v-model="value"
      :options="['选项A', '选项B', '选项C']">
    </mt-radio>
  </div>
</template>
<script>
import { Radio } from 'mint-ui';
export default {
  data () {
    return {
      value:''
    }
  },
  components:{
    'mt-radio': Radio
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