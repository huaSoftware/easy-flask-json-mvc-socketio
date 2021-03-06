import user from './modules/user'
import getters from './getters'
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

const store = new Vuex.Store({
  strict: debug, // 在非生产环境下，使用严格模式
  modules: {
    user
  },
  getters
})
export default store