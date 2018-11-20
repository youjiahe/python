#!/usr/bin/env python3
import pymysql
conn = pymysql.connect(
    host='139.159.193.210',
    port=3306,
    user="student",
    password="123456",
    db='devops',
    charset="utf8"
)

cusor=conn.cursor()
# insert1="insert into department values(%s,%s )"
# data=(1,"HR")
# ops=(2,"运维部")
# devs=(3,"开发部")
# finance=(4,"财务部")
# deps=[ops,devs,finance]
# cusor.execute(insert1,data)
# cusor.executemany(insert1,deps)

# update1="update department set dep_name=%s where dep_name=%s"
# data=("人事部","HR")
# cusor.execute(update1,data)
delete1="delete from department where dep_name=%s"
data=("财务部")
cusor.execute(delete1,data)
select1="select * from department"
cusor.execute(select1)
result=cusor.fetchall()
print(result)
conn.commit()
cusor.close()
conn.close()

