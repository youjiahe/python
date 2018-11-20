#!/usr/bin/env python3
from sqlalchemy_ import Session,Department,Employees
session=Session()
################查询对象返回值######################
#
# query1=session.query(Department.dep_id,Department.dep_name)
# print('-' * 30)
# print(query1)
# print('-' * 30)
# print(query1.all())   #返回全部数据
# print('-' * 30)       #
# print(query1.first())

# 运行结果
# ------------------------------
# SELECT departments.dep_id AS departments_dep_id, departments.dep_name AS departments_dep_name
# FROM departments
# ------------------------------
# [(1, '人事部'), (4, '财务部'), (3, '运维开发部'), (2, '运维部')]
# ------------------------------
# (1, '人事部')
################多表查询######################
#多表查询 join .. on
query2=session.query(Employees.emp_id,Employees.emp_name,Department.dep_name)\
    .join(Department,Employees.dep_id==Department.dep_id)
for emp in query2:
    print(emp)