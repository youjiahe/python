#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Enum,ColumnDefault,Date,ForeignKey
from sqlalchemy.orm import sessionmaker   #连接数据库，建立session会话

engine = create_engine(
    "mysql+pymysql://student:123456@you/bbs?charset=utf8",
    encoding="utf8",
    echo=False   #开启日志输出，生产环境中改为false；  会有很多的debug信息
)

Base = declarative_base()  #创建基类
Session = sessionmaker(bind=engine)

class Department(Base):
    __tablename__='departments'   #表名
    dep_id = Column(Integer,primary_key=True)
    dep_name=Column(String(20),unique=True,nullable=False)
    def __str__(self):
        return "<部门 %s>" % self.dep_name

class Employees(Base):
    __tablename__='employees'
    emp_id = Column(Integer,primary_key=True)
    emp_name = Column(String(10),nullable=False)
    gender = Enum(("male","female"))
    birth_date = Column(Date)
    phone = Column(String(11),nullable=False)
    dep_id = Column(Integer,ForeignKey("departments.dep_id"))

    def __str__(self):
        return "<员工:%s>"  % self.emp_name
class Salary(Base):
    __tablename__='salary'
    auto_id = Column(Integer,primary_key=True)
    emp_id = Column(Integer,ForeignKey('employees.emp_id'))
    salary_date = Column(Date)
    basic = Column(Integer)
    awards = Column(Integer)

    def __str__(self):
        return "<工资:%d>"  % (self.basic+self.awards)

if __name__ == '__main__':
    Base.metadata.create_all(engine)
