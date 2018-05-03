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
    <ul style="margin-top:10px;">
      <li v-for="item in list">
        <img v-lazy="item">
      </li>
    </ul>
  </div>
</template>
<script>
import { Swipe, SwipeItem } from 'mint-ui' // 轮播
import { Lazyload } from 'mint-ui' // 懒加载

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
      list:[
        'https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2493197328,3770105629&fm=27&gp=0.jpg',
        'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=319138660,3908650183&fm=27&gp=0.jpg',
        'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=2935625995,3978577917&fm=27&gp=0.jpg'
      ]
    }
  },
  methods: { 
    handleChange(index) {
      console.log(index)
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
  margin-top: 40px;
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
