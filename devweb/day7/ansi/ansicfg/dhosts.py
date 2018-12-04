#!/usr/bin/env python3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Enum,ColumnDefault,Date,ForeignKey
from sqlalchemy.orm import sessionmaker   #连接数据库，建立session会话
import json
engine = create_engine(
    "sqlite:////root/git/python/devweb/day7/ansi/db.sqlite3",
    encoding="utf8",
)

Base = declarative_base()  #创建基类
Session = sessionmaker(bind=engine)

class HostGroup(Base):
    __tablename__='ops_tools1_hostgroup'
    id=Column(Integer,primary_key=True)
    groupname = Column(String(50),unique=True)

    def __str__(self):
        return self.groupname

class Hosts(Base):
    __tablename__='ops_tools1_hosts'
    id = Column(Integer,primary_key=True)
    hostname =Column(String(50),unique=True)
    ipaddr = Column(String(15),unique=True)
    group_id = Column(Integer,ForeignKey('ops_tools1_hostgroup.groupname'))

    def __str__(self):
        return '<%s : %s>' % (self.ipaddr,self.hostname)

if __name__ == '__main__':
    session=Session()
    result = {}
    qset = session.query(Hosts.ipaddr,HostGroup.groupname)\
        .join(HostGroup,Hosts.group_id==HostGroup.id)
    for ip,group in qset:
        if group not in result:
            result[group] = {}
            result[group]['hosts']=[]
        result[group]['hosts'].append(ip)

    print(json.dumps(result))
