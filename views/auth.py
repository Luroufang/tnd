import tornado.web
from utills.account import register, login
from .main import BaseHandler




request = tornado.web.RequestHandler

# 注册
class RegisterHandler(request):
    def get(self, *args, **kwargs):
        self.render("auth/register.html", msg='')

    def post(self, *args, **kwargs):
        username = self.get_argument('username', None)
        password1 = self.get_argument('password', None)
        password2 = self.get_argument('password_again', None)

        if username and password1 and password2:

            if password1 == password2:
                msg = register(username, password1)
                if msg == 'ok':
                    self.redirect('/')
                else:
                    self.render('auth/register.html', msg=msg)
            else:
                self.render('auth/register.html', msg='密码输入不一致')
        else:
            self.render('auth/register.html', msg='输入不能为空')

# 登录
class LoginHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("auth/login.html", msg='')

    def post(self, *args, **kwargs):
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)
        if username and password:
            msg = login(username, password)
            if msg == 'ok':
                self.session.set('m_user', username)
                self.redirect('/')
            else:
                self.render('auth/login.html', msg=msg)
        else:
            self.render('auth/login.html', msg='用户名或密码不能为空')







