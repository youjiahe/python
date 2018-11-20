#!/usr/bin/env python3
from sqlalchemy_again import Departments,Session,Employees,Salary
session=Session()


# hr=Departments(dep_id=1,dep_name="人事部")
# ops=Departments(dep_id=2,dep_name="运维部")
# fin=Departments(dep_id=3,dep_name="财务部")
# dev=Departments(dep_id=4,dep_name="开发部")
# session.add_all([hr,ops,fin,dev])
# yjh = Employees(
#     emp_id=1,
#     emp_name="尤家和",
#     gender="男",
#     birth_date="19960311",
#     dep_id=1
# )
# kobe = Employees(
#     emp_id=2,
#     emp_name="禾斗",
#     gender="男",
#     birth_date="19780311",
#     dep_id=3
# )
# session.add_all([yjh,kobe])
query1=session.query(Departments.dep_id,Departments.dep_name)
for dep in query1:
    print(dep)
session.commit()
session.close()

