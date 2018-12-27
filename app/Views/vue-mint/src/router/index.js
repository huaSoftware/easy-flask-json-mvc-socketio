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
      meta: { title: '我的', header: true, back: true, more: true, footer: true }
    },
    {
      path: '/find',
      name: 'find',
      component: _import('find/index'),
      meta: { title: '全局的两种存储方式', header: true, back: true, more: true, footer: true }
    },
    {
      path: '/function',
      name: 'function',
      component: _import('function/index'),
      meta: { title: 'mint功能', header: true, back: true, more: true, footer: true },
      children: [
        {
          path: 'compressImg',
          component: _import('function/compressImg/index'),
          meta: { title: '压缩图片', header: true, back: true, more: true, footer: true }
        },
        {
          path: 'splitImg',
          component: _import('function/compressImg/splitImg'),
          meta: { title: '分片压缩图片', header: true, back: true, more: true, footer: true }
        },
        {
          path: 'loadMore',
          component: _import('function/load-more/index'),
          meta: { title: '上下拉加载', header: true, back: true, more: true, footer: true }
        },
        {
          path: 'infinite-scroll',
          name: 'infinite-scroll',
          component: _import('function/infinite-scroll/index'),
          meta: { title: '无限滚动', header: true, back: true, more: true, footer: true }
        },
        {
          path: 'spinner',
          name: 'spinner',
          component: _import('function/spinner/index'),
          meta: { title: '加载效果', header: true, back: true, more: true, footer: true }
        },
        {
          path: 'toast',
          name: 'toast',
          component: _import('function/toast/index'),
          meta: { title: '吐司', header: true, back: true, more: true, footer: true }
        },
        {
          path: 'process',
          name: 'process',
          component: _import('function/process/index'),
          meta: { title: '进度条', header: true, back: true, more: true, footer: true }
        },
        {
          path: 'picker',
          name: 'picker',
          component: _import('function/picker/index'),
          meta: { title: '选择器', header: true, back: true, more: true, footer: true }
        },
        {
          path: 'checklist',
          name: 'checklist',
          component: _import('function/checklist/index'),
          meta: { title: '复选框', header: true, back: true, more: true, footer: true }
        },
        {
          path: 'radio',
          name: 'radio',
          component: _import('function/radio/index'),
          meta: { title: '单选框', header: true, back: true, more: true, footer: true }
        },
        {
          path: 'actionSheet',
          name: 'actionSheet',
          component: _import('function/actionSheet/index'),
          meta: { title: '操作表', header: true, back: true, more: true, footer: true }
        },
        {
          path: 'field',
          name: 'field',
          component: _import('function/field/index'),
          meta: { title: '表单编辑器', header: true, back: true, more: true, footer: true }
        }
      ]
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
