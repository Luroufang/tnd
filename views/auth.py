from tornado.web import RequestHandler
from utills.account import register




class RegisterHandler(RequestHandler):
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








class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("auth/login.html")

    def post(self,*args,**kwargs):
        pass




