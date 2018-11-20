#!/usr/bin/env python3
from sqlalchemy_ import  Department,Session,Employees

session = Session()

# hr=Department(dep_id=1,dep_name="人事部")
# ops=Department(dep_id=2,dep_name="运维部")
# devops=Department(dep_id=3,dep_name="运维开发部")
# finance=Department(dep_id=4,dep_name="财务部")
# deps=[ops,devops,finance]
# session.add(hr)
# session.add_all(deps)
yjh = Employees (
    emp_id = 1,
    emp_name = "尤家和",
    gender = "男",
    birth_date = "19930311",
    phone = "13675220551",
    dep_id = 3
)
ljq = Employees (
    emp_id = 2,
    emp_name = "梁珈钎",
    gender = "女",
    birth_date = "19950311",
    phone = "13375223333",
    dep_id = 4
)
session.add_all([yjh,ljq])
session.commit()
session.close()