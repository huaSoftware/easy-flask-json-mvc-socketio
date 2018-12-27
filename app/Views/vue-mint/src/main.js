// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import Mint from 'mint-ui'
import { InfiniteScroll } from 'mint-ui'

import 'mint-ui/lib/style.css'
import '../static/css/common.css'
// 统一图标样式 https://icomoon.io/app/#/select/font
import '@/assets/style.css'

Vue.config.productionTip = false
// 全局注册mint
Vue.use(Mint)
Vue.use(InfiniteScroll)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
