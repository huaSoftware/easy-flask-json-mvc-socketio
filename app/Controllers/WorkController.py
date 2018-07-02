""" 生产者控制层 """
from app import app
from flask import request

@app.route('/work/start', methods=['POST'])
def workStart():
  id = request.json.get('id')

