const getters = {
  token: state => state.user.token,
  is_auth: state => state.user.is_auth,
  user: state => state.user.user
}
export default getters
