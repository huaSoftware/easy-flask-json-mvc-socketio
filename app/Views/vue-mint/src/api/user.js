import request from '@/utils/request'

export function login (email, password) {
  return request({
    url: '/api/v2/login',
    method: 'post',
    data: {
      email,
      password
    }
  })
}

export function register (email, password) {
  return request({
    url: '/api/v2/register',
    method: 'post',
    data: {
      email,
      password
    }
  })
}

export function logout (token) {
  return request({
    url: '/api/v2.admin/logout',
    method: 'post',
    data: {
      token
    }
  })
}

export function uploadBase64Img (data) {
  return request({
    url: '/api/v2//document/upload/base64',
    method: 'post',
    data
  })
}

export function getCommentList (data) {
  return request({
    url: '/api/v2/comments/get',
    method: 'post',
    data
  })
}
