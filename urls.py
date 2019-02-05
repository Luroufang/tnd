import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

from views.main import MainHandler, ShowHandler, UploadHandler
from views.auth import RegisterHandler, LoginHandler

from utills.setting import setting


define("port", default=8000, help="run on the given port", type=int)

class Application(tornado.web.Application):

    def __init__(self):
            handlers = [
                (r"/", MainHandler),
                (r"/register", RegisterHandler),
                (r"/login", LoginHandler),
                (r"/show", ShowHandler),
                (r"/upload", UploadHandler)
            ]
            settings = setting()
            tornado.web.Application.__init__(self, handlers, debug=True, **settings)



def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__=="__main__":
    main()
