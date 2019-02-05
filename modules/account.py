from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.sql import exists
from modules.connect import Base, Session

session = Session()

class User(Base):
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








