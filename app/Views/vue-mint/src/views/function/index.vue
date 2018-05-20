<template>
  <div class="content">
    <mt-cell title="mint功能" value="这里我们将展示mint的各种组件功能"></mt-cell>
    <router-link class="top" to="/function/compressImg">多图片压缩</router-link>
    <router-link class="top" to="/function/loadMore">上下拉加载</router-link>
    <router-link class="top" to="/function/infinite-scroll">无限加载</router-link>
    <router-link class="top" to="/function/spinner">加载效果</router-link>
     <keep-alive>
        <router-view ></router-view>
    </keep-alive>
  </div>
</template>
<script>
//http://mint-ui.github.io/#!/zh-cn,loadmore示例，警告千万不要打开:auto-fill="true",CPU差点烧掉！！！
import { Loadmore } from 'mint-ui';
import { Cell } from 'mint-ui';
import { getCommentList } from '@/api/user'
export default {
  data () {
    return {
    }
  },
  components:{
    'mt-cell': Cell
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
.content{
  height:100vh;
  overflow: scroll;
}
.top{
  display: inline-block;
  width:33.33%;
  height:50px;
  line-height: 50px;
  text-align: center;
  float: left;
  text-decoration:none;
  background: #f5f5f5;
  color:#26a2ff;
}

</style>
