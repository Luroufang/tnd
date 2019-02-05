from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

HOSTNAME = '47.106.212.48'
PORT = '3306'
DATABASE = 'mydb'
USERNAME = 'finley'
PASSWORD = 'md123456'

Db_url = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, DATABASE)

engine = create_engine(Db_url)
Base = declarative_base(engine)
Session = sessionmaker(engine)








