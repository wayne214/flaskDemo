from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def index():
    return 'Index'
@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

# 唯一的 URL / 重定向行为
# projects 的 URL 是中规中矩的，尾部有一个斜杠，看起来就如同一个文件夹。 访问一个没有斜杠结尾的 URL 时 Flask 会自动进行重定向，帮你在尾部加上一个斜杠。
#
# about 的 URL 没有尾部斜杠，因此其行为表现与一个文件类似。如果访问这个 URL 时添加了尾部斜杠就会得到一个 404 错误。这样可以保持 URL 唯一，并帮助 搜索引擎避免重复索引同一页面。

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def projects():
    return 'The about page'

if __name__ == '__main__':
    app.run()
