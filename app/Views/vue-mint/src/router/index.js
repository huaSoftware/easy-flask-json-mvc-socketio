import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
const _import = require('./_import_' + process.env.NODE_ENV)

Vue.use(Router)

const router = new Router({
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
      component: _import('home/guide'), // 载入组件
      meta: { title: '引导页', header: false, back: false, more: false, footer: false } // 定义一些公共状态，你喜欢就好
    },
    {
      path: '/home/index',
      name: 'home.index',
      component: _import('home/index/index'),
      meta: { title: '首页', header: true, back: true, more: true, footer: true }
    },
    {
      path: '/mine',
      name: 'mine',
      component: _import('mine/index'),
      meta: { title: '我的', header: true, back: true, more: true, footer: true },
      children: [
        {
          path: 'compressImg',
          component: _import('mine/compressImg/index'),
          meta: { title: '压缩图片', header: true, back: true, more: true, footer: true }
        }
      ]
    },
    {
      path: '/find',
      name: 'find',
      component: _import('find/index'),
      meta: { title: '发现', header: true, back: true, more: true, footer: true }
    }
  ]
})

// 在每个路由前执行一些东西，中间件啊，多好啊，美妙啊，棒棒哒~
router.beforeEach((to, from, next) => {
  if (to.meta.title) {
    document.title = to.meta.title
  }
  next()
})
export default router
