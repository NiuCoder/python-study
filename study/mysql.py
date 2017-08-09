# -*- encoding:utf-8 -*-

import MySQLdb
conn = MySQLdb.connect(
		host = 'localhost',
		port = 3306,
		user = 'root',
		passwd = '',
		db = 'mysql',
	)
cur = conn.cursor()

# 创建数据库
# cur.execute("create table student(id int,name varchar(20),class varchar(30),age varchar(10))")
# cur.execute("insert into student values('2','Tom','3 year 2 class','9')")

# cur.execute("update student set class='3 year 1 class' where name='Tom'")

print cur.execute("select * from student")
print cur.fetchone()

cur.close()
conn.commit()
conn.close()
