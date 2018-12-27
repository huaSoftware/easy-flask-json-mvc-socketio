<template>
  <div class="content">
    <div class="json">{{vuex.user}},{{vuex.is_auth}},{{vuex.token}}</div>
    <div class="explain">理解：js是脚本语言，所以执行完释放变量。vuex，内存数据，读取快，就像redis一样，全局的，页面关闭后释放。</div>
    <div class="json">{{localToken}}</div>
    <div class="explain">理解：与vuex相反，localstorage是本地缓存，持久化，I/O是很慢的。</div>
  </div>
</template>
<script>
import storage from '@/utils/localstorage'
import { mapGetters } from 'vuex'
// vuex状态改变不能同步，所以需要watch和computed一起配合实时更新
// https://segmentfault.com/q/1010000007918478
// http://www.jb51.net/article/114472.htm
export default {
  data () {
    return {
      localToken : '',
      vuex: {
        user: '',
        is_auth: '',
        token: ''
      }
    }
  },
  props: {},
  watch: {
    user(val) {
      this.vuex.user = val;
    },
    is_auth(val) {
      this.vuex.is_auth = val;
    },
    token(val) {
      this.vuex.token = val;
    }
  },
  methods: {

  },
  filters: {},
  computed: {
    // ...拓展运算符,比较迷，会用就好https://segmentfault.com/q/1010000008303593
    ...mapGetters({
      user: 'user',
      is_auth: 'is_auth',
      token: 'token'
    })
  },
  created () {
    console.log(this.$store)
    this.vuex.user = this.$store.getters.user
    this.vuex.is_auth = this.$store.getters.is_auth
    this.vuex.token = this.$store.getters.token
    this.localToken = storage.getLocalstorage('token')
  },
  mounted () {
  }
}
</script>

<style lang="less" scoped>
.json{
  margin-top:20px;
  word-wrap: break-word;
}
.explain{
  margin-top:40px;
  color:red;
}
</style>
