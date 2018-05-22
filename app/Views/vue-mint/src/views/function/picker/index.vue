<template>
  <div class="clean">
    <mt-picker :slots="slots" @change="onValuesChange"></mt-picker>
  </div>
</template>
<script>
import { Picker } from 'mint-ui';

export default {
  data () {
    return {
      slots: [
        {
          flex: 1,
          values: ['2015-01', '2015-02', '2015-03', '2015-04', '2015-05', '2015-06'],
          className: 'slot1',
          textAlign: 'right'
        }, {
          divider: true,
          content: '-',
          className: 'slot2'
        }, {
          flex: 1,
          values: ['2015-01', '2015-02', '2015-03', '2015-04', '2015-05', '2015-06'],
          className: 'slot3',
          textAlign: 'left'
        }
      ]
    }
  },
  components:{
    "mt-picker": Picker
  },
  props: {},
  watch: {
  
  },
  methods: {
    onValuesChange(picker, values) {
      if (values[0] > values[1]) {
        picker.setSlotValue(1, values[0]);
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
