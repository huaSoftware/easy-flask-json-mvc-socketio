<template>
  <div class="img-content clean">
    <div class="imgs-div">
        <img class="imgs"  @click="portrait('inputFileOne')"  :src="headImg" id="userImgOne">
    </div>
    <mt-progress :value="value" :bar-height="5">
        <div slot="end">{{value}}%</div>
    </mt-progress>
    <form id="myForm" name="myForm">
      <input  id="inputFileOne" @change="bind('userImgOne')" type="file" accept="image/*" name="documentOne" >
    </form>
    <div>{{reqUrl}}</div>
   <!--  <button @click="handleImg" class="mint-button mint-button--primary" style="float:right;margin-right:10px">上传图片</button> -->
  </div>
</template>
<script>
import storage from '@/utils/localstorage'
import { mapGetters } from 'vuex'
import { Progress } from 'mint-ui'
import { uploadBase64Img, imgShard, imgSwitch } from '@/api/user'
// vuex状态改变不能同步，所以需要watch和computed一起配合实时更新
// https://segmentfault.com/q/1010000007918478
// http://www.jb51.net/article/114472.htm
export default {
  data () {
    return {
      dict: {
          userImgOne:
            {   
                name:'',
                size:'',
                type:'',
                url: ''
            }
      },
      headImg: 'static/img/jia.jpg',
      uuid:'',
      rawPicList:[],
      reqPicList:[],
      value:0,
      reqUrl: ''
    }
  },
  props: {},
  watch: {

  },
  methods: {
		logout:function() {
			/*登出*/
			var btnArray = ['是','否'];
			mui.confirm('退出登录，确认？', '注 销', btnArray, function(e){
				if (e.index == 0) {
					window.localStorage.clear();
					document.location.href = '../index.html';
					return true;
				} 
			})		
		},
		portrait:function(id) {
			//呼出底部菜单
			/* if(window.plus){
	            var a=[{
	                title:'拍照'
	            },{
	                title:'从手机相册选择'
	            }];
	            plus.nativeUI.actionSheet({
	                title:'修改头像',
	                cancel:'取消',
	                buttons:a
	            },function(b){
	                switch(b.index){
	                    case 0:
	                        break;
	                    case 1:
	                        //拍照
	                        this.getImages();
	                        break;
	                    case 2:
	                        //打开相册
	                        this.galleryImages();
	                        break;
	                    default:
	                        break;
	                }
	            },false);   
	        }else{ */
	            let btn = document.getElementById(id);
				btn.click();
	        //}
		},
		bind:function(id) {
            let that = this
			let file = event.target.files[0];
		    // 选择的文件是图片
            try{
                this.dict[id].name = file.name
                this.dict[id].size = file.size
                this.dict[id].type = file.type
            }
            catch(err){
				console.log(err);
			}
		    var reader = new FileReader();//这是核心,读取操作就是由它完成.
            //reader.readAsText(selectedFile);//读取文件的内容,也可以读取文件的URL
            reader.onload = function (e) {
                //当读取完成后回调这个函数,然后此时文件的内容存储到了result中,直接操作即可
                that.uploadHeadImg(e.target.result, id);
            };
            try{
			    if (file.type.indexOf("image") == 0) {
			        reader.readAsDataURL(file);    
			    }
			}catch(err){
				console.log(err);
			}
		},
		//拍照
    getImages:function (){
        var mobileCamera=plus.camera.getCamera();
        mobileCamera.captureImage(function(e){
            plus.io.resolveLocalFileSystemURL(e,function(entry){
                var path=entry.toLocalURL()+'?version='+new Date().getTime();
                this.uploadHeadImg(path, id);
            },function(err){
                console.log("读取拍照文件错误");
            });
        },function(e){
            console.log("er",err);
        },function(){
            filename:'_doc/head.png';
        });
    },
    //从本地相册选择
    galleryImages(){
        console.log("你选择了从相册选择");
        let that = this
        plus.gallery.pick(function(a){
            plus.io.resolveLocalFileSystemURL(a,function(entry){
                plus.io.resolveLocalFileSystemURL('_doc/',function(root){
                    root.getFile('head.png',{},function(file){
                        //文件已经存在
                        file.remove(function(){
                            console.log("文件移除成功");
                            entry.copyTo(root,'head.png',function(e){
                                var path=e.fullPath+'?version='+new Date().getTime();
                                that.uploadHeadImg(path, id);
                            },function(err){
                                console.log("copy image fail: ",err);
                            });
                        },function(err){
                            console.log("删除图片失败：（"+JSON.stringify(err)+")");
                        });
                    },function(err){
                        //打开文件失败
                        entry.copyTo(root,'head.png',function(e){
                            var path=e.fullPath+'?version='+new Date().getTime();
                            that.uploadHeadImg(path, id);
                        },function(err){

                            console.log("上传图片失败：（"+JSON.stringify(err)+")");
                        });
                    });
                },function(e){
                    console.log("读取文件夹失败：（"+JSON.stringify(err)+")");
                });
            });
        },function(err){
            console.log("读取拍照文件失败: ",err);
        },{
            filter:'image'
        });
	},
        //上传图片
    uploadHeadImg:function (imgPath, id){
        let that = this
        //选中图片之后，头像当前的照片变为选择的照片
        var mainImg=document.getElementById(id);
        mainImg.src=imgPath;
        var images=new Image();
        images.src=imgPath;
        images.onload = function() { 
            let imgData=that.getBase64Image(images,that.dict[id].size,that.dict[id].type);
            that.dict[id].imgBase64 = imgData
            console.log(imgData)
            //将字符串切片放入列表,初始化一些属性
            that.reqUrl = ''
            that.value = 0
            that.reqPicList = []
            that.rawPicList = []
            that.uuid = that.uuidMethod()
            for(let i=0;i<imgData.length;i=i+50000){
                console.log(i)
                console.log(i+50000)
                let rawPicDict = {'uuid': that.uuid, index: i+50000, imgString: imgData.substring(i,i+50000)}
                that.rawPicList.push(rawPicDict)
                //lastIndex = i+100000
            }
            //let rawPicDict = {'uuid': uuid, index: lastIndex, imgString: imgData.substring(lastIndex,imgData.length)}
            //that.rawPicList.push(rawPicDict)
            for(let j=0;j<that.rawPicList.length;j++){
                that.splitImg(that.rawPicList[j])
            }
            //console.log(rawPicList)
            //imgShard
            //that.imgData.unshift(that.dict)
            /*ajax*/
        /*  var url    = '/api/v2/member.user.img';
        var data   = {'imgDatas':imgData,'url':GLOBAL_CONFIG['API_HOST']};
        var type   = 'post';
            var header = {'Content-Type':'application/json',
                'Authorization':GLOBAL_CONFIG['Authorization']};
        var success = function(data){
            if(resCheck(data)){		
                h('.loading').hide();
                mui.toast('上传成功！');
            }
            }; 
        Request(url,data,success,type,header).ajax(); */
        }
    },
    // 压缩图片转成base64
    getBase64Image:function (img, size ,type){
          console.log(img.width)
          if(size >307200){ //大于300KB就减少10倍长宽
              if(img.height >2000){
                  var width=img.width / 5.5;
                  var height=img.height / 5.5;
              }
              else if(img.height >1000) {
                  var width=img.width / 5;
                  var height=img.height / 5;
              }
              else if(img.height >500) {
                  var width=img.width / 2.5;
                  var height=img.height / 2.5;
              }
          }else{
              var width=img.width;
              var height=img.height;
          }
          var canvas=document.createElement("canvas");
        canvas.width=width;
        canvas.height=height;
        var ctx=canvas.getContext('2d');
        ctx.drawImage(img,0,0,width,height);
    
        var dataUrl=canvas.toDataURL(type,1);
        //console.log(dataUrl);
        return dataUrl.replace('data:'+type+':base64,','');
    },
    handleImg(){
      uploadBase64Img(this.dict).then(res =>{
          
      })
    },
    uuidMethod() {
        var s = [];
        var hexDigits = "0123456789abcdef";
        for (var i = 0; i < 36; i++) {
            s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
        }
        s[14] = "4";  // bits 12-15 of the time_hi_and_version field to 0010
        s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1);  // bits 6-7 of the clock_seq_hi_and_reserved to 01
        s[8] = s[13] = s[18] = s[23] = "-";
        var uuid = s.join("");
        return uuid;
    },
    splitImg(rawPicDict){
        //现在使用的是异步并行上传，可以修改成同步上传。then内执行数组减一操作并判断数组数组是否为空，空就结束
        imgShard(rawPicDict).then(res=>{
            if(res.data !== 0){
                this.reqPicList.push(res.data)
                console.log(this.reqPicList)
                console.log(this.rawPicList)
                this.value = (this.reqPicList.length / this.rawPicList.length) * 100
                console.log(this.value)
                if(this.reqPicList.length == this.rawPicList.length){
                    imgSwitch({uuid:this.uuid}).then(res=>{
                        console.log(res)
                        this.reqUrl  = '返回的后端保存地址:' + res.data.url
                        this.dict['userImgOne'].url = res.data.url
                    })
                }
            }else{
                //这里处理后端返回错误重传
                this.splitImg(rawPicDict)
            }
        }).catch(error=>{
            //这里处理网络返回错误重传
            this.splitImg(rawPicDict)
        })
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
.img-content{
    width:100%;
    clear: both;
}
#myForm{
    display:none;
}
.imgs-div{
    width: 32.5%;
    padding-bottom:32.5%;
    height:0px;
    position: relative;
    display: inline-block;
}
.imgs{
    width: 100%;
    height: 100%;
    position:absolute;
}
</style>
