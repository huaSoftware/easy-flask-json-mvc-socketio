<template>
    <v-loadmore :top-method="loadTop" 
      :bottom-method="loadBottom" 
      :bottom-all-loaded="allLoaded" 
      :auto-fill="false" 
      :bottomPullText="bottomText"
      :bottomLoadingText="bottomLoadingText"
      :bottomDropText="bottomDropText"
      ref="loadmore">  
      <ul class="list" v-for="(val, key) in pageList">  
        <li>  
          <div>{{val.msg}}</div>  
          <div>{{val.add_time}}</div>  
        </li>  
      </ul>  
  </v-loadmore>
</template>
<script>
//http://mint-ui.github.io/#!/zh-cn,loadmore示例，警告千万不要打开:auto-fill="true",CPU差点烧掉！！！
import { Loadmore } from 'mint-ui';
import { getCommentList } from '@/api/user'
export default {
  data () {
    return {
      searchCondition:{  //分页属性  
          pageNo: 1,  
          pageSize: 10  
        },  
      pageList:[],  
      allLoaded: false, //是否可以上拉属性，false可以上拉，true为禁止上拉，就是不让往上划加载数据了  
      scrollMode:"auto", //移动端弹性滚动效果，touch为弹性滚动，auto是非弹性滚动  
      bottomText: '上拉加载',//自定义上拉文字
      bottomDropText: '释放加载',//自定义上拉释放文字
      bottomLoadingText: '上拉加载中...'//自定义上拉加载中文字
    }
  },
  components:{
      'v-loadmore':Loadmore,
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
      this.$refs.loadmore.onBottomLoaded();// 固定方法，查询完要调用一次，用于重新定位
    },
    loadTop() {
      //下拉刷新，模拟用加载数据
      this.more();
      //this.allLoaded = true;
      this.$refs.loadmore.onTopLoaded();// 固定方法，查询完要调用一次，用于重新定位
    },
    more() {
      getCommentList(this.searchCondition).then(res=>{
        this.searchCondition.pageNo++
        console.log(res)
        this.pageList = this.pageList.concat(res.list)
        if(res.total_page*res.current_page > res.count){
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

<style lang="less" scoped>
.mint-loadmore{
 padding-bottom:55px;
}
</style>
