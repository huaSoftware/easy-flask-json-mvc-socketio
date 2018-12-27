<template>
  <div class="toast-content clean">
      <div class="raw-toast"  @click="rawToast">
        点击弹出弹窗
      </div>
      <div class="icon-toast" @click="iconToast">
        点击弹出带有icon的弹窗
      </div>
      <div class="site-toast" @click="siteToast">
        自定义弹窗位置
      </div>
  </div>
</template>
<script>
import { Toast  } from 'mint-ui'

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
   rawToast(){
     Toast('原生弹窗')
   },
   iconToast(){
    Toast({
      message: '带图标弹窗',
      iconClass: 'icon icon-dui-01'
    });
   },
   siteToast(){
    Toast({
      message: '提示',
      position: 'top',
      duration: 5000
    });
    /* 'top' 'bottom' 'middle' */
   }
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
.toast-content{
  width: 100%;
  height: 100%;
}
.raw-toast{
  top:20px;
  width:80%;
  height:50px;
  background:#f5f5f5;
  left:10%;
  position: relative;
  text-align: center;
  line-height: 50px;
}
.icon-toast{
  top:40px;
  width:80%;
  height:50px;
  background:#f5f5f5;
  left:10%;
  position: relative;
  text-align: center;
  line-height: 50px;
}
.site-toast{
  top:60px;
  width:80%;
  height:50px;
  background:#f5f5f5;
  left:10%;
  position: relative;
  text-align: center;
  line-height: 50px;
}
</style>
