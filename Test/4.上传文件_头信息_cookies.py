# 从flask包中导入Flask类
from flask import Flask, request
# 创建一个Flask对象
app = Flask(__name__)
# @app.route:是一个装饰器
# @app.route('/')就是将url中 / 映射到hello_world设个视图函数上面
# 以后你访问我这个网站的 / 目录的时候 会执行hello_world这个函数，然后将这个函数的返回值返回给浏览器


@app.route('/')
def hello_world():
    return 'hello Flask!'


@app.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['pic']
    # with open('./demo.png', 'wb') as new_file:
    #   new_file.write(f.read())

    # print(photo.filename)         # 图片的名字
    # print(photo.headers)          # 请求头部信息
    # print(photo.content_type)     # 文件类型
    # print(photo.mimetype)         # 内容类型
    # print(photo.mimetype_params)  # 类型参数

    f.save('./{}'.format(f.filename))  # 将图片以本名的方式储存在本地
    return '上传成功!'


@app.route('/args')
def args():
    cookies = request.cookies.get('uid')
    headers = request.headers.get('ContentType')
    url = request.url
    method = request.method
    return f'上传成功！！ {cookies} =={headers} == {url} == {method}'


# 启动这个WEB服务
if __name__ == '__main__':
    # 默认为5000端口
    app.run(host="0.0.0.0", port=5000)  # 127.0.0.1
