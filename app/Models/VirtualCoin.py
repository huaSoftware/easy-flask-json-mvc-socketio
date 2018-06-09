from app.Models.BaseModel import BaseModel
import requests
import json
import time


""" 虚拟货币模型 """
class VirtualCoin(BaseModel):
    def getWsContent(self,CoinName):
      url = 'http://www.daoxiaoyue.com/ws/handle'
      data = '{"Command":2,"Body":{"Coin":"%s","Currency":"USD","Base":"CNY"}}'%(CoinName)
      headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '65',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'UM_distinctid=16399d1b4904c2-005f8fee29ab21-444a012d-1fa400-16399d1b491760; CNZZDATA1273159115=414225665-1527294057-%7C1527294057',
        'Host': 'www.daoxiaoyue.com',
        'Origin': 'http://www.daoxiaoyue.com',
        'Referer': 'http://www.daoxiaoyue.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
      }
      try:
          res = requests.post(url, data=data, headers=headers)
          datas = json.loads(res.text)
          return datas
      except:
          return  {"Body":{"Itmes":[]}}
       
  
