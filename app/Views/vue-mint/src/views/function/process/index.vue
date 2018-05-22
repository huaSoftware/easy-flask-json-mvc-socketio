<template>
  <div class="clean">
    <mt-progress :value="value" :bar-height="5">
      <div slot="start">{{value}}%</div>
      <div slot="end">100%</div>
    </mt-progress>
  </div>
</template>
<script>
import { Progress } from 'mint-ui';

export default {
  data () {
    return {
      value:1
    }
  },
  components:{
    "mt-progress": Progress
  },
  props: {},
  watch: {
  
  },
  methods: {
    count(){
       this.value++   
       if(this.value == 100){
          clearInterval(window.s);
       }
    }
  },
  filters: {},
  computed: {
   
  },
  created () {
    window.s = setInterval(this.count,100)
  },
  mounted () {
  }
}
</script>

<style lang="less" scoped>

</style>
