import pymysql
import sqlalchemy
conn = pymysql.connect(
    host='139.159.193.210',
    port=3306,
    user="student",
    password="123456",
    db="nsd1806",
    charset="utf8"
)
cusor=conn.cursor()  #创建游标，相当于指向数据库某个位置的指针
select1="select * from department"
update1="update department set department=%s where department=%s"
data=("人力资源部","HR")
cusor.execute(update1,data)
cusor.execute(select1)
res=cusor.fetchall()
print(res)
cusor.close()
conn.close()

