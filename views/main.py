from pycket.session import SessionMixin
from tornado.web import authenticated
from tornado.web import RequestHandler
import os

from utills.photo import get_images, make_thumb
from modules.account import Post

class BaseHandler(RequestHandler, SessionMixin):
    def get_current_user(self):
        return self.session.get('m_user', None)


class MainHandler(BaseHandler):

    @authenticated
    def get(self, *args, **kwargs):
        imgs = Post.get_post()
        self.render("index.html", imgs=imgs)

    def post(self, *args, **kwargs):
        pass

class ShowHandler(BaseHandler):
    def get(self, *args, **kwargs):
        imgs = Post.get_post()
        self.render("show.html", imgs=imgs)

    def post(self, *args, **kwargs):
        pass

class UploadHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render("upload_pictures.html")

    def post(self, *args, **kwargs):
        img_list = self.request.files.get('upimgs', None)
        for img in img_list:
            print(img)
            save_to = 'static/uploads/{}'.format(img['filename'])
            with open(save_to, 'wb') as f:
                f.write(img['body'])
            thumb_path = make_thumb(save_to)

            image_url = 'uploads/{}'.format(img['filename'])
            thumb_url = os.path.relpath(thumb_path, 'static')
            Post.add_post(self.current_user, image_url, thumb_url)
        self.write('upload done')

