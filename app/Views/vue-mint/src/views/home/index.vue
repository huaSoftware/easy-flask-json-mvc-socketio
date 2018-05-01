<template>
  <!-- 一个组件一个div，不准有同级元素 -->
  <div class="content">
    <div @click="attackIt(1)" class="shilaimu">一只小史莱姆LV{{level}}，HP{{hp}}
    </div>
    <div class="hint">
      提示：双击史莱姆视为攻击
    </div>
  </div>
</template>
<script>
export default {
  //第一个详细讲
  name: 'home',// 给你的组件一个名字，有些地方需要
  // 划重点了，生命周期，不了解的看这https://segmentfault.com/a/1190000008010666
  beforeCreate() {},// 组件实例刚被创建，组件属性计算值前，容易data属性等
  created() {},// 组件实例创建完成，属性已经绑定，dom还没生成，$el属性还不存在
  beforeMount() {},// 模板编译之前
  mounted() {},// 模板编译之后
  beforeUpdate() {},// 组件更新之前
  updated() {},// 组件更新之后
  activated() {},// 组件移除时调用
  beforeDestroy() {},// 组件销毁前调用
  destroyed() {},// 组件销毁后调用
  //重点结束
  data() { // 重头戏，data双向绑定的数据写这边，对象，组数等放进来
    return {
      level: 1,
      hp: 10
    }
  },
  methods: {// 方法放这边 
    attackIt(value){
       this.hp = this.hp - value
       if(this.hp < 0){
         alert('成功打败史莱姆')
         //方法路由回到helloWorld
         this.$router.push('/')
       }
    },
  },
  components:{},// 子组件
  props: { // 父给子传参使用
    value: String
  },
  computed: { // 计算属性写这边，配合store里面的数据
  },
  filters:{} //过滤器
  //可能还有缺的，但是掌握这些就可以打怪了，说明就到这里，先打个史莱姆。
  /* 古人学问无遗力，少壮工夫老始成。
   * 纸上得来终觉浅，绝知此事要躬行。
   */
}
</script>
<style  scoped>
/* less是开启less语法， scoped是局部化css，让你写的css只能影响这个组件 */
.content{
  height:100%;
  width:100%;
}
.shilaimu{
  position: relative;
  top:60px;
}
.hint{
  position: fixed;
  bottom: 50px;
  text-align: center;
  width:100%;
}
</style>
