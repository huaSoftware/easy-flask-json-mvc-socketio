<template>
  <div class="content">
    <!-- swipe轮播 -->
    <mt-swipe :auto="4000" @change="handleChange">
      <mt-swipe-item>
        <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1525276235543&di=fb64efa8f722442e804f405f3d157b93&imgtype=0&src=http%3A%2F%2Fwww.ppvke.com%2FBlog%2Fwp-content%2Fuploads%2F2016%2F11%2Fpython3.jpg">
      </mt-swipe-item>
      <mt-swipe-item>
        <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1525276235543&di=fb64efa8f722442e804f405f3d157b93&imgtype=0&src=http%3A%2F%2Fwww.ppvke.com%2FBlog%2Fwp-content%2Fuploads%2F2016%2F11%2Fpython3.jpg">
      </mt-swipe-item>
      <mt-swipe-item>
        <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1525276235543&di=fb64efa8f722442e804f405f3d157b93&imgtype=0&src=http%3A%2F%2Fwww.ppvke.com%2FBlog%2Fwp-content%2Fuploads%2F2016%2F11%2Fpython3.jpg">
      </mt-swipe-item>
    </mt-swipe>
    <mt-cell title="flask+vue" value="前后端分离轻架构"></mt-cell>
    <mt-cell title="socketio" value="view层下面有几个静态文件哦~"></mt-cell>
    <mt-cell title="jwt" value="鉴权模块体验请点击我的"></mt-cell>
    <mt-cell title="vuex" value="js全局数据体验请点击vuex"></mt-cell>
    <mt-cell title="mint功能" value="体验mint各种功能请点击mint功能"></mt-cell>
  </div>
</template>
<script>
import { Swipe, SwipeItem } from 'mint-ui' // 轮播
import { Lazyload } from 'mint-ui' // 懒加载
import { Cell } from 'mint-ui' // 单元格
export default {
  name: 'index',
  beforeCreate() {},
  created() {},
  beforeMount() {},
  mounted() {},
  beforeUpdate() {},
  updated() {},
  activated() {},
  beforeDestroy() {},
  destroyed() {},
  data() { 
    return {
    }
  },
  methods: { 
    handleChange(index) {
      //console.log(index)
    }
  },
  components:{},
  computed: {
  },
  filters:{} 
}
</script>
<style lang="less" scoped>
.mint-swipe{
  width:100%;
  height:30%;
}
.mint-swipe-item img{
  width:100%;
}
image[lazy=loading] {
  width: 40px;
  height: 300px;
  margin: auto;
}
ul li img{
  width:100%;
}
</style>
