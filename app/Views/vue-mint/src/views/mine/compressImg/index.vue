<template>
  <div>
    <img class="imgs"  @click="portrait('inputFileOne')"  :src="headImg" id="userImgOne">
    <img class="imgs"  @click="portrait('inputFileTwo')"  :src="headImg" id="userImgTwo">
    <img class="imgs"  @click="portrait('inputFileThree')"  :src="headImg" id="userImgThree">
    <form id="myForm" name="myForm">
      <input  id="inputFileOne" @change="bind('userImgOne')" type="file" name="documentOne" >
      <input  id="inputFileTwo" @change="bind('userImgTwo')" type="file" name="documentTwo" >
      <input  id="inputFileThree" @change="bind('userImgThree')" type="file" name="documentThree" >
    </form>
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
      imgData: []
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
			if(window.plus){
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
	        }else{
	            let btn = document.getElementById(id);
				btn.click();
	        }
		},
		bind:function(id) {
            let that = this
			let file = event.target.files[0];
		    // 选择的文件是图片
		    var reader = new FileReader();//这是核心,读取操作就是由它完成.
            //reader.readAsText(selectedFile);//读取文件的内容,也可以读取文件的URL
            reader.onload = function (e) {
                //当读取完成后回调这个函数,然后此时文件的内容存储到了result中,直接操作即可
                console.log(id)
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
    galleryImages:function (){
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
              var imgData=that.getBase64Image(images);
              let dict = {}
              dict[id] = imgData
              that.imgData.unshift(dict)
              console.log(that.imgData)
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
	    getBase64Image:function (img){
            var canvas=document.createElement("canvas");
            var width = 300;
	        var height = 400;
	       /*  var width=img.width;
            var height=img.height;
	        if(width>height){
	            if(width>100){
	                height=Math.round(height*=100/width);
	                width=100;
	            }
	        }else{
	            if(height>100){
	                width=Math.round(width*=100/height);
	            }
	            height=100;
	        } */
	        canvas.width=width;
	        canvas.height=height;
	        var ctx=canvas.getContext('2d');
	        ctx.drawImage(img,0,0,width,height);
			
	        var dataUrl=canvas.toDataURL('image/png',1);
	        //console.log(dataUrl);
	        return dataUrl.replace('data:image/png:base64,','');
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
#myForm{
    display:none;
}
.imgs{
    width:100px;
    height:100px;
}
</style>
