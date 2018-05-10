/* 权限函数工具库
 * author hua
 * 2018,3,29
 */
/* 获取token
 * params:tokenName;令牌名
 * params:expirationTime;过期时间
 * return bool or token
 */
export function getToken (tokenName, expirationTime) {
  let data = window.localStorage.getItem(tokenName)
  if (data == null) {
    return false
  }
  let dataObj = JSON.parse(data)
  if ((new Date().getTime() - dataObj.time) > parseInt(expirationTime)) {
    // window.localStorage.clear()
    localStorage.removeItem(tokenName)
    /*  mui.alert('账号过期', '信息框', function () {
      // document.location.href = 'http://www.baidu.com'
      router.go({ name: 'login' })
    }) */
    return false
  } else {
    var dataObjDatatoJson = dataObj.data
    return dataObjDatatoJson
  }
}

/* 设置token
 * params:tokenName;令牌名
 * params:tokenVal;令牌值
 * return bool
 */
export function setToken (tokenName, tokenVal) {
  let curTime = new Date().getTime()
  window.localStorage.setItem(tokenName, JSON.stringify({ data: tokenVal, time: curTime }))
  return true
}

/* 销毁token
 * params:tokenName;令牌名
 * return bool
 */
export function removeToken (tokenName) {
  localStorage.removeItem(tokenName)
  return true
}
