# 从flask包中导入Flask类
from flask import Flask, jsonify
# 创建一个Flask对象
app = Flask(__name__)
# @app.route:是一个装饰器
# @app.route('/')就是将url中 / 映射到hello_world设个视图函数上面
# 以后你访问我这个网站的 / 目录的时候 会执行hello_world这个函数，然后将这个函数的返回值返回给浏览器


@app.route('/')
def hello_world():
    return 'hello Flask!'


@app.route('/return_str')
def return_str():
    return "你好，少年"


# app.config['JSON_AS_ASCII'] = False


@app.route('/return_json1')
def return_json1():
    json_dict = {
        "msg_int": 10,
        "msg_str": "你好，少年"
    }
    return jsonify(json_dict)


@app.route('/return_json2')
def return_json2():
    json_dict = {
        "msg_int": 10,
        "msg_str": "你好，少年"
    }
    return json_dict


@app.route('/demo1')
def demo1():

    # response内容, status状态码[可无], headers响应头
    return '状态码为 666', 666, {'itbaizhan': 'Python'}


# 启动这个WEB服务
if __name__ == '__main__':
    # 默认为5000端口
    app.run(host="0.0.0.0", port=5000)  # 127.0.0.1
