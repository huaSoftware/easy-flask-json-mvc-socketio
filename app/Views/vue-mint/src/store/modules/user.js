
import { login } from '@/api/user'
import { getToken, setToken } from '@/utils/auth'
import storage from '@/utils/localstorage'
import { Toast } from 'mint-ui'
const user = {
  state: {
    token: getToken('token', process.env.EXPIRATION_TIME),
    is_auth: false,
    user: storage.getLocalstorage('user')
  },

  actions: {// 支持异步
    // 登录
    Login ({ commit }, data) {
      return new Promise((resolve, reject) => {
        login(data.login_email, data.login_password).then(response => {
          console.log(response)
          const data = response.data
          console.log(data.token)
          Toast(response.data)
          // 存取token到localstorage
          setToken('token', data.token)
          // 存取user对象到localstorage
          storage.setLocalstorage('user', data.user)
          commit('SET_TOKEN', data.token)
          commit('SET_USER', data.user)
          resolve()// 成功解决，参看promise
        }).catch(error => {
          reject(error)// 失败拒绝
        })
      })
    },
    // updateIsAuth
    updateIsAuth ({ commit }, isAuth) {
      commit('SET_IS_AUTH', isAuth)
    }
  },

  mutations: {// 只支持同步
    // 这边设置下token，参看login.vue
    SET_TOKEN: (state, token) => {
      state.token = token
    },
    SET_IS_AUTH: (state, isAuth) => {
      state.is_auth = isAuth
    },
    // 保存用户id 以便调用此数据
    SET_USER: (state, user) => {
      state.user = user
      // console.log(state.userId)
    }
  }
}

export default user
