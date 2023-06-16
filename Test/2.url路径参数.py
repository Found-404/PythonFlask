# 从flask包中导入Flask类
from flask import Flask
# 创建一个Flask对象
app = Flask(__name__)
# @app.route:是一个装饰器
# @app.route('/')就是将url中 / 映射到hello_world设个视图函数上面
# 以后你访问我这个网站的 / 目录的时候 会执行hello_world这个函数，然后将这个函数的返回值返回给浏览器


@app.route('/')
def hello_world():
    return 'hello Flask!'


@app.route('/user/<user_id>')
def success(user_id):
    print('user_id:', type(user_id))
    return 'welcome %s %s' % user_id
    # return 'hello user{}'.format(user_id)


@app.route('/users/<int:user_id>')
def users_info(user_id):
    print(type(user_id))
    return f'正在获取 ID {user_id} 的用户信息'


@app.route('/users/<int(min=1):user_id>')
def user_info(user_id):
    print(type(user_id))
    return f'hello user {user_id}'


# 启动这个WEB服务
if __name__ == '__main__':
    # 默认为5000端口
    app.run(host="0.0.0.0", port=5000)  # 127.0.0.1
