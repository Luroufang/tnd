from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import exists
from modules.connect import Base, Session

session = Session()

class User(Base):
    """
    用户信息存储
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50))
    create_time = Column(DateTime, default=datetime.now())


    def __repr__(self):
        return '<User(#{}:{})>'.format(self.id, self.username)


    @classmethod
    def add_user(cls, username, password):
        user = User(username=username, password=password)

        session.add(user)
        session.commit()

    @classmethod
    def exist(cls, username):
        return session.query(exists().where(User.username == username)).scalar()

    @classmethod
    def by_name(cls, username):
        return session.query(cls).filter_by(username=username).all()


class Post(Base):
    """
    用户图片信息存储
    """
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    image_url = Column(String(200))
    thumb_url = Column(String(200))
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', backref='posts', uselist=False, cascade='all')

    def __repr__(self):
        return '<User(#{}:{},{})>'.format(self.id, self.image_url, self.thumb_url)


    @classmethod
    def add_post(cls, username, image_url, thumb_url):

        user = session.query(User).filter_by(username=username).first()
        post = Post(user=user, image_url=image_url, thumb_url=thumb_url)

        session.add(post)
        session.commit()

    @classmethod
    def get_post(cls):
        posts = session.query(cls).all()
        return posts