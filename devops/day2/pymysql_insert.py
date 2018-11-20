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
insert1="insert into department values (%s,%s)"
hr=(1,"HR")
deps=[(2,"")]
cusor.execute(insert1,hr)
cusor.executemany()
conn.commit()   #都需要确认
cusor.close()
conn.close()