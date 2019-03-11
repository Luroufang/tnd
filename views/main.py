from pycket.session import SessionMixin
from tornado.web import authenticated
from tornado.web import RequestHandler

from views.photo import UploadImages
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
            #实例化
            upload_im = UploadImages('static',img['filename'])
            #保存图片
            upload_im.save_images(img['body'])
            #形成缩略图并保存
            upload_im.make_thumb()

            #图片信息保存到数据库
            Post.add_post(self.current_user,upload_im.image_path,upload_im.thumb_path)

        self.write('upload done')

