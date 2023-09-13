# 从flask包中导入Flask类
from flask import Flask, url_for
# 创建一个Flask对象
app = Flask(__name__)
# @app.route:是一个装饰器
# @app.route('/')就是将url中 / 映射到hello_world设个视图函数上面
# 以后你访问我这个网站的 / 目录的时候 会执行hello_world这个函数，然后将这个函数的返回值返回给浏览器

@app.route('/post/list/<page>/')
def my_list(page):
    return 'my list'


@app.route('/')
def hello_world():
    return url_for('my_list', page=2, num=8)
    # return "/post/list/2?num=8"


# 启动这个WEB服务
if __name__ == '__main__':
    # 默认为5000端口
    app.run(host="0.0.0.0", port=5000)  # 127.0.0.1
