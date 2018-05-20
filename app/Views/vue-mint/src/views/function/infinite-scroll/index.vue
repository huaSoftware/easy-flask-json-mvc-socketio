<template>
  <!--ul里面几个scoller就是无限滚动的几个api,不推荐-->
  <ul class="mui-table-view clean" 
      v-infinite-scroll="loadBottom" 
      infinite-scroll-disabled="false" 
      infinite-scroll-distance="0" 
      infinite-scroll-immediate-check="false">
    <!--li数据遍历循环部分-->
    <li class="mui-table-view-cell" v-for="item in pageList">
      <a class="mui-navigate-right">
      <span class="mui-pull-left">{{item.msg}}</span>
      <span class="mui-pull-right">{{item.add_time}}</span>
      </a>
    </li>
    <!--底部判断是加载图标还是提示“全部加载”-->
    <li class="more_loading" v-show="!queryLoading">
      <mt-spinner type="snake" color="#00ccff" :size="20" v-show="moreLoading&&!allLoaded"></mt-spinner>
      <span v-show="allLoaded">已全部加载</span>
    </li>
  </ul>
</template>
<script>
import { getCommentList } from '@/api/user'
export default {
  data () {
    return {
      //初始化无限加载相关参数
      queryLoading: false,
      moreLoading: false,
      allLoaded: false,
      searchCondition:{  //分页属性  
          pageNo: 1,  
          pageSize: 20  
        },  
      pageList:[],  
    }
  },
  components:{
  },
  props: {},
  watch: {
  
  },
  methods: {
    handleTopChange(status) {
      this.topStatus = status;
    },
    loadBottom() {
      // 上拉加载
      this.more();// 上拉触发的分页查询
      //this.allLoaded = true;
    },
    more() {
      if(this.allLoaded){
        this.moreLoading = true;
        return;
      }
      if(this.queryLoading){
        return;
      }
      this.moreLoading = !this.queryLoading;
      this.searchCondition.pageNo++
      getCommentList(this.searchCondition).then(res=>{
        this.pageList = this.pageList.concat(res.data.commentsList)
        if(res.data.paged.more == 0){
           this.allLoaded = true;// 若数据已全部获取完毕
        }
      })
    },
    refresh() {

    }
  },
  filters: {},
  computed: {
   
  },
  created () {
    this.more()
  },
  mounted () {
  }
}
</script>
<style lang="scss" scoped>
.mui-table-view{
  margin-top:40px;
  height:100%;
}
</style>
