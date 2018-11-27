from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Enum,ColumnDefault,Date,ForeignKey
from sqlalchemy.orm import sessionmaker   #连接数据库，建立session会话

engine = create_engine(
    "mysql+pymysql://student:123456@139.159.193.210/bbs?charset='utf8'",
    encoding='utf8',
    echo=False
)

class MysqlAlchemy:
    def __init__(self,):