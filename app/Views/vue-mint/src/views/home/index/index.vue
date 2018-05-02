<template>
  <div class="content">
    <!-- 头部导航 -->
    <mt-header fixed :title="this.$route.meta.title ">
      <router-link to="/" slot="left">
        <mt-button icon="back">返回</mt-button>
      </router-link>
      <mt-button icon="more" slot="right" @click="fuckMore"></mt-button>
    </mt-header>
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
  </div>
</template>
<script>
import { Header } from 'mint-ui' // 头部组件
import { MessageBox } from 'mint-ui' // 消息盒子
import { Swipe, SwipeItem } from 'mint-ui' // 轮播

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
    fuckMore() {
      MessageBox('你以为还有？', '我帮你写算了...');
    },
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
</style>
