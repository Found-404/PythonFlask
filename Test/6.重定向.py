from flask import Flask, request, url_for, redirect
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login/')
def login():
    return '这是登录页面'
# falsk中重定向


@app.route('/profile/')
def proflie():
    # 判断query中是否有name字段
    if request.args.get('name'):
        return '个人中心页面'
    else:
        # return redirect(url_for('login'))
        return redirect(url_for('login'), code=302)


if __name__ == '__main__':
    app.run(debug=True)
