import tornado.web

from tornado.web import RequestHandler

class MainHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")

    def post(self, *args, **kwargs):
        pass

class ShowHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("show.html")

    def post(self, *args, **kwargs):
        pass

class UploadHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("upload_pictures.html")

    def post(self, *args, **kwargs):
        pass


