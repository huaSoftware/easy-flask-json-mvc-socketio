import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
const _import = require('./_import_' + process.env.NODE_ENV)

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    // 第一个详细讲
    {
      path: '/home', // 路径
      name: 'home', // 给他个名字，后期路由传参用
      component: _import('home/index'), // 载入组件
      meta: { title: '首页' } // 定义一些公共状态，你喜欢就好
    }
  ]
})
