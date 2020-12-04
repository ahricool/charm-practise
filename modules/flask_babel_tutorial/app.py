"""
babel 用于翻译 flask string
文档  https://flask-babel.tkte.ch/#

"""


from flask import Flask
# from flask.ext.babel import Babel 旧版的 flask 需要这样引入
from flask_babel import Babel  # 新版的 flask 这样引入
from flask_babel import gettext, ngettext,lazy_gettext
from flask import g, request

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    # 如果这个 user 已经登录
    user = getattr(g, 'user', None)
    if user is not None:
        return user.locale
    # 否则我们就从 request 的 accept_languages 的 headers 里面猜用户要什么语言
    return request.accept_languages.best_match(['zh'])


@babel.timezoneselector
def get_timezone():
    user = getattr(g, "user", None)
    if user is not None:
        return user.timezone


gettext(u'A simpel String')
gettext(u'Value: %(value)s', value=42)
ngettext(u'%(num)s Apple', u'%(num)s Apples', 10)


@app.route("/")
def hello_world():
    return gettext("Hello, world!\n")+lazy_gettext("China!")


if __name__ == "__main__":
    app.run(port=5003, debug=True)
