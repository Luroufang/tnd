import os
import glob
from PIL import Image
from uuid import uuid4


def get_images(imgpath):
    os.chdir('static')
    img_path = glob.glob('{}/*.jpg'.format(imgpath))
    os.chdir('..')
    return img_path


def make_thumb(path):
    size = (128, 128)
    im = Image.open(path)
    im.thumbnail(size)
    filename = os.path.basename(path)
    name, ext = os.path.splitext(filename)
    save_path = 'static/imgs/thumb/{}_{}x{}{}'.format(name, size[0], size[1], ext)
    im.save(save_path, 'JPEG')
    return save_path


class UploadImages(object):
    size = (128,128)

    def __init__(self,static_path,name):
        self.static_path = static_path
        self.orig_name = name
        self.new_name = self.gen_new_name()

    def gen_new_name(self):
        """生成唯一字符串
        :return:
        """
        _, ext = os.path.splitext(self.orig_name)
        return uuid4().hex + ext

    @property
    def image_path(self):
        return os.path.join('imgs','uploads',self.new_name)

    @property
    def upload_path(self):
        return os.path.join(self.static_path,self.image_path)

    def save_images(self,content):
         with open(self.upload_path, 'wb') as f:
             f.write(content)
    @property
    def thumb_path(self):
        name, ext = os.path.splitext(self.new_name)
        thumb_name = '{}_{}x{}{}'.format(name,self.size[0],self.size[1],ext)
        return os.path.join('imgs','thumb',thumb_name)

    def make_thumb(self):
        im = Image.open(self.upload_path)
        im.thumbnail(self.size)
        save_path = os.path.join(self.static_path,self.thumb_path)
        im.save(save_path, 'JPEG')
        return save_path
