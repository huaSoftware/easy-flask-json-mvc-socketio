<template>
  <div class="content">
    <div class="login" >
      <mt-navbar v-model="selected">
        <mt-tab-item id="1">登录</mt-tab-item>
        <mt-tab-item id="2">注册</mt-tab-item>
      </mt-navbar>

      <mt-tab-container v-model="selected">
        <!-- 登录 -->
        <mt-tab-container-item id="1" class="login-wrapper">
          <mt-field label="邮箱" placeholder="请输入邮箱" v-model="login_email"></mt-field>
          <mt-field label="密码" placeholder="请输入密码" type="password" v-model="login_password"></mt-field>
          <mt-button type="primary" size="large" @click.native="handleLogin">登录</mt-button>
        </mt-tab-container-item>

        <!-- 注册 -->
        <mt-tab-container-item id="2" class="register-wrapper">
          <mt-field label="邮箱" placeholder="请输入邮箱" type="email" v-model="register_email"></mt-field>
          <mt-field label="密码" placeholder="请输入密码" type="password" v-model="register_password1"></mt-field>
          <mt-field label="确认密码" placeholder="请确认密码" type="password" v-model="register_password2"></mt-field>
          <mt-button type="primary" size="large" @click.native="handleRegister">注册</mt-button>
        </mt-tab-container-item>
      </mt-tab-container>
    </div>
  </div>
</template>
<script>
import {register} from '@/api/user'
export default {
  data () {
    return {
      selected: '1',
      login_email: '',
      login_password: '',
      register_email: '',
      register_password1: '',
      register_password2: '',
    }
  },
  props: {},
  watch: {},
  methods: {
    back () {
      this.$router.push({
        path: '/index'
      })
    },
    handleLogin () {
        this.$store.dispatch('Login', {'login_email':this.login_email,'login_password':this.login_password}).then(() => {
          this.$router.push('/find')
        }) 
    },
    handleRegister () {
      register(this.register_email, this.register_password1 ).then(res => {
        
      })
    }
  },
  filters: {},
  computed: {},
  created () {},
  mounted () {}
}
</script>

<style lang="less" scoped>
.compressImg{
  float:right;
  position: relative;
  margin-right:10px;
  margin-top:10px;

}
</style>
