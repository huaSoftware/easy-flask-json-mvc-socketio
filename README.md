<!--
 * @Author: hua
 * @Date: 2018-08-30 10:52:11
 * @LastEditors: hua
 * @LastEditTime: 2019-05-30 15:50:20
 -->
#### 项目介绍
一套基于flask，vue的前后端分离的解决方案（献给从事web开发的pythoner）。

人生苦短，我用python!

#### 更新情况
- [x] 2019.04.03 增加事务，验证装饰器，demo在UsersController下
- [x] 2019.05.30 增加全局异常日志记录及接口异常回溯描述返回
- [x] 2019.05.30 增加验证描述万国语言支持
- [] 2019.12.12 模型一键生成，继承模型进行后封装增删改查通用方法，减少操作orm的难度

#### 软件架构
一.后端flask程序:

	1.三个入口文件:

		json api入口启动run.py

		restful api入口启动 restfulRun.py

		websocket入口启动 socketRun.py	
	
	2.运行流程

		run.py->

		app/__init__.py ->

		app/Middleware/XSSProtection.py(抽象一层中间层用于处理一些统一验证的逻辑，根据需求进行添加)

		app/Controllers/UsersController.py(接收前端json参数并分发给模型层处理,参考flask request模块接参方法)->

		app/Models/Users.py(业务逻辑书写成静态方法或类方法给控制层调用)->

		app/Controllers/UsersController.py(接收模型层返回值返回)


二.前端vue程序:

	1.安装，运行，打包:

		采用webpack，vue,mint-ui技术的前端解决方案

		npm install(建议使用淘宝源 cnpm install)

		npm run dev(启动测试环境)

		npm run build(打包成浏览器识别的语法)

	2.一些重要的文件夹及文件:

		路由层:src/router/index.js

		视图层:src/views/*

		组件层:src/components/*

		api层:src/api/*

		资源层:src/assets/*

		仓储层(vuex):src/store/*

		工具层:src/utils/*

#### 作者其他开源产品
1. <a href="https://gitee.com/huashiyuting/tool_chicken" target="_blank">工具鸡前端app项目</a>
2. <a href="https://gitee.com/huashiyuting/status_bar_monitor" target="_blank">状态栏监听安卓客户端 </a>
3. <a href="https://gitee.com/huashiyuting/plainCms" target="_blank">plainCms</a>
#### 捐助作者
![捐助作者](https://images.gitee.com/uploads/images/2019/0124/105407_661d1190_1588193.png "mm_facetoface_collect_qrcode_1548297043215.png")	
