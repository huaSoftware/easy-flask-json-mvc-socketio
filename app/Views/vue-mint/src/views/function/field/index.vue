<template>
  <div class="clean">
    <form id="validators_form" @submit.prevent="handleValidator">
      <mt-field label="用户名" placeholder="请输入用户名" :attr="{name:'username'}" v-model="username" :state="validated_status.username"></mt-field>
      <mt-field label="邮箱" placeholder="请输入邮箱" type="email" :attr="{name:'email'}" v-model="email" :state="validated_status.email"></mt-field>
      <mt-field label="密码" placeholder="请输入密码" type="password"  :attr="{name:'password'}" v-model="password" :state="validated_status.password"></mt-field>
      <mt-field label="手机号" placeholder="请输入手机号" type="tel" :attr="{name:'phone'}" v-model="phone" :disableClear="true" :state="validated_status.phone"></mt-field>
      <mt-field label="网站" placeholder="请输入网址" type="url" :attr="{name:'website'}" v-model="website" :disabled="true" :state="validated_status.website"></mt-field>
      <mt-field label="数字" placeholder="请输入数字" type="number" :attr="{name:'number'}" v-model="number" :state="validated_status.number"></mt-field>
      <mt-field label="生日" placeholder="请输入生日" type="date" :attr="{name:'birthday'}" v-model="birthday" :state="validated_status.birthday"></mt-field>
      <mt-field label="自我介绍" placeholder="自我介绍" type="textarea" rows="4" :attr="{name:'introduction'}" v-model="introduction" :state="validated_status.introduction"></mt-field>
      <mt-button type="primary">提交</mt-button>
    </form>
  </div>
</template>
<script>
import { Button } from 'mint-ui'
import { Field } from 'mint-ui'
import { Toast } from 'mint-ui'
import { validated, validatedError }from '@/utils/validator'
export default {
  data () {
    return {
      username: '',
      email: '',
      password: '',
      phone: '',
      website: '',
      number: '',
      birthday: '',
      introduction: '',
      validated_status: {
        username: null,
        email: null,
        password:null,
        phone:null,
        website:null,
        number: null,
        birthday:null,
        introduction:null
      },
      validators_option:[
        {
          name: 'username',
          display:"用户名必填|用户名不能大于20位|用户名不能小于6位",
          rules: 'required||max_length(20)|min_length(6)'
        },
        {
          name: 'email',
          display:"邮箱必填|邮箱不能大于12位|邮箱不能小于6位",
          rules: 'required|max_length(12)|min_length(6)'
        },
        {
          name: 'password',
          display:"密码必填|密码不能大于12位|密码不能小于6位",
          rules: 'required|max_length(12)|min_length(6)'
        },
        {
          name: 'phone',
          display:"你输入的不是合法手机号|手机号必填|手机号不能大于12位|手机号不能小于6位",
          rules: 'is_phone|required|max_length(12)|min_length(6)'
        },
        {
          name: 'website',
          display:"你输入的不是合法网站|网站不能大于12位|网站不能小于6位",
          rules: 'is_url|max_length(12)|min_length(6)'
        },
        {
          name: 'number',
          display:"你输入的不是合法网站|网站不能大于12位|网站不能小于6位",
          rules: 'is_url|max_length(12)|min_length(6)'
        },
        {
          name: 'birthday',
          display:"生日不能大于12位|生日不能小于6位",
          rules: 'max_length(12)|min_length(6)'
        },
        {
          name: 'introduction',
          display:"留言不能大于12位|留言不能小于6位",
          rules: 'max_length(12)|min_length(6)'
        }
      ],
    }
  },
  components:{
    'mt-field': Field
  },
  props: {},
  watch: {
  
  },
  methods: {
    handleValidator() {
       //验证处理,返回错误信息
      var errors = validated('validators_form',this.validators_option)
      //根据错误生成input状态
      console.log(errors)
      validatedError(errors ,this.validated_status)
      if(errors.length == 0){
        Toast('成功通过验证')
      }
    }
  },
  filters: {},
  computed: {
   
  },
  created () {

  },
  mounted () {
  }
}
</script>

<style lang="less" scoped>

</style>