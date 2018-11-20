#!/usr/bin/env python3
import  pymysql
conn = pymysql.connect(
    host="139.159.193.210",
    port=3306,
    user="student",
    password="123456",
    db="nsd1806",
    charset="utf8"
)
curso=conn.cursor()
create1="create table test1(name char(10))"
show="show tables"
curso.execute(create1)
curso.execute(show)
result=curso.fetchall()
print(result)
conn.commit()
curso.close()
conn.close()