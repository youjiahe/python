import pymysql
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
cusor.execute(select1)
cusor.scroll(1,mode="absolute")
res=cusor.fetchone()
print(res)
cusor.scroll(1,mode="relative")
res=cusor.fetchone()
print(res)
cusor.close()
conn.close()

