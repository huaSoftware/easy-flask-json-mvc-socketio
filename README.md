
一套基于flask，vue的前后端分离的解决方案（无锡地区的py）。
后端flask三个入口文件：<br /> 
  1.json api入口启动run.py<br /> 
  2.restful api入口启动 restfulRun.py<br /> 
  3.websocket入口启动 socketRun.py<br /> 

一.后端flask程序运行流程：<br />
  run.py-><br />
  app/__init__.py -><br />
  app/Middleware/XSSProtection.py(抽象一层中间层用于处理一些统一验证的逻辑，根据也无需求添加，可以跳过)<br />
  app/Controllers/UsersController.py(接收前端json参数并分发给模型层处理,参考flask request模块接参方法)-><br />
  app/Models/Users.py(业务逻辑书写给模型层调用)-><br />
  app/Controllers/UsersController.py(接收模型层返回值返回)<br />

二.前端vue程序运行流程：<br/>
   暂时不更新