<template>
  <div class="clean">
    <mt-spinner type="snake" color="red"></mt-spinner>
    <mt-spinner type="double-bounce" color="yellow"></mt-spinner>
    <mt-spinner type="triple-bounce" color="green"></mt-spinner>
    <mt-spinner type="fading-circle" color="black"></mt-spinner>

    <!-- 或者接受传入类型的序号 -->
    <mt-spinner :type="0" color="#313434"></mt-spinner>
    <mt-spinner :type="1" color="#wrfdvs"></mt-spinner>
    <mt-spinner :type="2" color="#cccccc"></mt-spinner>
    <mt-spinner :type="3" color="#eeeeee"></mt-spinner>
  </div>
</template>
<script>
/* 加载动画 */
import { Spinner } from 'mint-ui';
export default {
  data () {
    return {
    
    }
  },
  components:{
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
<style lang="scss" scoped>
.clean span{
  position: relative;
  margin-left:50%;
  left:-14px;
  display: inline-block;
}

</style>
