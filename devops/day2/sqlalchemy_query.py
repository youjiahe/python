#！/usr/bin/env python3
from sqlalchemy_ import Department,Session
from sqlalchemy import and_,or_
session=Session()
####################################################
#基础搜索
# query1=session.query(Department)   #SQL语句
# print(query1)
# for dep in query1:
#     print(dep)
#     print('%s -> %s' % (dep.dep_id,dep.dep_name))

# 运行结果：
# SELECT departments.dep_id AS departments_dep_id, departments.dep_name AS departments_dep_name
# FROM departments
# 1 -> 人事部
# 4 -> 财务部
# 3 -> 运维开发部
# 2 -> 运维部
####################################################
#基础搜索----->元组
# query2=session.query(Department.dep_id,Department.dep_name)
# print(query2)
# for dep in query2:
#     print(dep)      #元组组成的列表
# for dep_id,dep_name in query2:
#     print('%s => %s' % (dep_id,dep_name))

# 运行结果：
# SELECT departments.dep_id AS departments_dep_id, departments.dep_name AS departments_dep_name
# FROM departments
# (1, '人事部')
# (4, '财务部')
# (3, '运维开发部')
# (2, '运维部')
# 1 => 人事部
# 4 => 财务部
# 3 => 运维开发部
# 2 => 运维部
##################搜索单个字段##################################
#搜索单个字段
# query3=session.query(Department.dep_name.label('部门'))
# print(query3)
# for dep in query3:
#     print(dep.部门)

# #运行结果：
# # SELECT departments.dep_name AS `部门`
# # FROM departments
# # 人事部
# # 财务部
# # 运维开发部
# # 运维部
#####################排序###############################
#排序
# query4=session.query(Department).order_by(Department.dep_id)
# print(query4)
# for dep in query4:
#     print(dep)
#     print('%s => %s' % (dep.dep_id,dep.dep_name))

# #运行结果：
# SELECT departments.dep_id AS departments_dep_id, departments.dep_name AS departments_dep_name
# FROM departments ORDER BY departments.dep_id
# <部门 人事部>
# 1 => 人事部
# <部门 运维部>
# 2 => 运维部
# <部门 运维开发部>
# 3 => 运维开发部
# <部门 财务部>
# 4 => 财务部
#####################切片###############################
#切片
# query5=session.query(Department).order_by(Department.dep_id)[1:3]
# print(query5)
# for dep in query5:
#     print(dep)
#     print('%s => %s' % (dep.dep_id, dep.dep_name))

# #运行结果：
# [<sqlalchemy_.Department object at 0x7fc88eb39b70>, <sqlalchemy_.Department object at 0x7fc88eb399e8>]
# <部门 运维部>
# 2 => 运维部
# <部门 运维开发部>
# 3 => 运维开发部
#####################过滤结果###############################
#过滤结果   filter------>where
# query6=session.query(Department).filter(Department.dep_id>2).order_by(Department.dep_id)
# print(query6)
# for dep in query6:
#     print(dep)
#     print('%s => %s' % (dep.dep_id, dep.dep_name))

# #运行结果：
# SELECT departments.dep_id AS departments_dep_id, departments.dep_name AS departments_dep_name
# FROM departments
# WHERE departments.dep_id = %(dep_id_1)s
# <部门 运维开发部>
# 3 => 运维开发部
######################范围匹配##############################
#范围匹配  in_()  ~  in
# query7=session.query(Department).filter(Department.dep_name.in_(["财务部","人事部"]))
# print(query7)
# for dep in query7:
#     print('%s => %s' % (dep.dep_id, dep.dep_name))
#
# query8=session.query(Department).filter(~Department.dep_name.in_(["财务部","人事部"]))
# print(query8)
# for dep in query8:
#     print('%s => %s' % (dep.dep_id, dep.dep_name))
######################逻辑匹配##############################
#逻辑匹配  and_()  or_()
# query9=session.query(Department).filter(and_(Department.dep_id>=1,Department.dep_id<=3))
# print(query9)
# for dep in query9:
#     print('%s => %s' % (dep.dep_id, dep.dep_name))
#
# query10=session.query(Department).filter(or_(Department.dep_id==2,Department.dep_id==3))
# # print(query10)
# for dep in query10:
#     print('%s => %s' % (dep.dep_id, dep.dep_name))
#######################空匹配#############################
#空匹配  None  is_(None)  isnot(None)
# query11=session.query(Department).filter(Department.dep_name.is_(None))
# print(query11)
# for dep in query11:
#     print('%s => %s' % (dep.dep_id, dep.dep_name))
#
# query11=session.query(Department).filter(Department.dep_name.isnot(None))
# print(query11)
# for dep in query11:
#     print('%s => %s' % (dep.dep_id, dep.dep_name))
####################################################
