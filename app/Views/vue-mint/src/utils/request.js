import axios from 'axios'
import store from '../store'
import router from '../router'
import { Toast } from 'mint-ui'

// 创建axios实例
const service = axios.create({
  baseURL: process.env.BASE_API, // api的base_url
  timeout: 15000// 请求超时时间
})

// request拦截器
service.interceptors.request.use(config => {
  // 定义在store/user中，以后会添加权限等设置
  let token = store.getters.token
  // console.log(store.getters.is_auth)
  if (store.getters.token) {
    config.headers['Authorization'] = token // 让每个请求携带自定义token 请根据实际情况自行修改
  }
  // config.headers['Content-Type'] = store.state.appData.headerContentType
  return config
}, error => {
  // Do something with request error
  console.log(error) // for debug
  Promise.reject(error)
})

// respone拦截器
service.interceptors.response.use(
  response => {
  /**
  * error为true时 显示msg提示信息
  */
    const res = response.data
    /* if (res.error === true) {
      Toast(res.msg)
      return Promise.reject('error')
    } */
    // error为false时，code为200时显示数据
    // store.dispatch('updateIsAuth', true)
    // console.log(store.getters.is_auth)
    if (res.error_code === 200 || res.error === false) {
      Toast(res.msg)
      return res
    }
    if (res.error_code === 400 || res.error === false) {
      /* 统一错误处理 */
      let msg = ''
      if (typeof res.msg === 'object') {
        for (let v in res.msg) {
          for (let i = 0; res.msg[v].length > i; i++) {
            msg = msg + ',' + res.msg[v][i]
          }
        }
        if (msg.substr(0, 1) === ',') msg = msg.substr(1)
        Toast(msg)
      } else {
        Toast(res.msg)
      }
      // Toast('网络错误')
      // return Promise.reject('error')
    }
    if (res.error_code === 401 || res.error === false) {
      Toast(res.msg)
      // return Promise.reject('error')
    }
    if (res.error_code === 5000 || res.error === false) {
      // Token expired
      Toast('token过期，请重新登陆')
      // 这里需要删除token，不然携带错误token无法去登陆
      window.localStorage.removeItem('token')
    }
  },
  error => {
    // console.log('err' + error)// for debug
    /* token未携带处理 */
    /*  if (error.response.status === 401) {
      // 401暂定位token错误
      // setTimeout(router.push('/login'), 3000)
    }
    if (error.response.status === 400) {
      Toast('网络错误')
    } */
    return Promise.reject(error)
  }
)

export default service
