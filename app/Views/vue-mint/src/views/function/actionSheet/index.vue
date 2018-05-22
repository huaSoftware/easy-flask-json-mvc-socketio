<template>
  <div class="clean">
    <button class="mint-button mint-button--default mint-button--large" @click="actionSheet">  
      <label class="mint-button-text">点击上拉 action sheet</label>  
    </button>  
    <mt-actionsheet
      :actions="actions"
      v-model="sheetVisible">
    </mt-actionsheet>
  </div>
</template>
<script>
import { Actionsheet } from 'mint-ui';
export default {
  data () {
    return {
      actions:[{  
        name: '拍照',  
        method :'' // 调用methods中的函数  
      }, {  
        name: '从相册中选择',   
        method :''// 调用methods中的函数  
      }],  
      // action sheet 默认不显示，为false。操作sheetVisible可以控制显示与隐藏  
      sheetVisible: false  
    }
  },
  components:{
    'mt-actionsheet': Actionsheet
  },
  props: {},
  watch: {
  
  },
  methods: {
     actionSheet(){  
      this.sheetVisible = true;  
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

</style>