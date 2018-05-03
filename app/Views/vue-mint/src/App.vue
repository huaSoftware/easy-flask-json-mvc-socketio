<template>
  <div id="app">
    <!-- 头部导航 -->
    <mt-header fixed :title="this.$route.meta.title" v-show="this.$route.meta.header">
      <router-link to="/" slot="left" v-show="this.$route.meta.back">
        <mt-button icon="back">返回</mt-button>
      </router-link>
      <mt-button icon="more" slot="right" @click="fuckMore" v-show="this.$route.meta.more"></mt-button>
    </mt-header>
    <router-view/>
    <!-- 底部选项卡 -->
    <mt-tabbar  v-show="this.$route.meta.footer">
      <mt-tab-item id="首页">
        <span slot="icon" class="icon-zhu iconfont" @click="goHome"></span>
        首页
      </mt-tab-item>
      <mt-tab-item id="订单">
        <span slot="icon" class="icon-ding2 iconfont" @click="goOrder"></span>
        订单
      </mt-tab-item>
      <mt-tab-item id="发现">
        <span slot="icon" class="icon-search2 iconfont" @click="goFind"></span>
        发现
      </mt-tab-item>
      <mt-tab-item id="我的">
        <span slot="icon" class="icon-w iconfont"  @click="goMine"></span>
        我的
      </mt-tab-item>
    </mt-tabbar>
  </div>
</template>

<script>
import { Header } from 'mint-ui' // 头部组件
import { MessageBox } from 'mint-ui' // 消息盒子
import { Tabbar, TabItem } from 'mint-ui'; //底部选项卡，标签选项,这边难度有点大，暂时不引入tab-container切换子页面
export default {
  name: 'App',
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
    goHome() {
      alert(1)
      this.$router.push('/home/index')
    },
    goOrder() {
      this.$router.push('/order')
    },
    goFind() {
      this.$router.push('/find')
    },
    goMine() {
      this.$router.push('/mine')
    }
  },
  components:{},
  computed: {
  },
  filters:{} 
}
</script>

<style lang="less" scoped>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100%;
  height: 100%;
}

.iconfont{
  font-size:24px;
}

.mint-tabbar{
  position: fixed;
}
</style>
