import hashlib
from ntpath import join
from time import time
from flask import Flask,request, abort
WECHAT_TOKEN=''

app = Flask(__name__)

@app.route('/')
def wechat():
  # 对接服务器
  signature = request.args.get('signature')
  timestamp = request.args.get('timestamp')
  nonce = request.args.get('nonce')
  echostr = request.args.get('echostr')
  # 校验参数
  if not all([signature,timestamp,nonce,echostr]):
    abort(400)
  li = [WECHAT_TOKEN,timestamp,nonce,echostr]
  li.sort()
  tem_str = ''.join(li)
  #进行sha1加密，与signNature进行对比
  sign = hashlib.sha1(tem_str).hexdigest()
  if sign!=signature:
    abort(403)
  else:
    return echostr
if __name__ =='__main__':
  app.run(port=8000,debug=True)