import mysql.connector;
#  In this library we have the method connect which help to connect the python to mysql ==> connect()

conn = mysql.connector.connect(
    host = 'localhost',
    port = '3306',
    username = 'root',
    password = 'aaka0505',
    database = 'cromacampus'
    )
print(conn)

# cursor() is the method which helps to write the query in python to database
cur = conn.cursor()


#==========================================IT IS MANDOTORY ===========================================
"""
sql  = "CREATE DATABASE cromaCampus"
cur.execute(sql)


sql = '''
Create TABLE student(
sid int primary key auto_increment,
sname varchar(30),
sadd text,
email text
)
'''
cur.execute(sql)

INSERT VALUES---
sql =  "insert into student values(101 , 'Aakash' , 'Ghazaiabad' , 'a.gmail.com')"  
cur.execute(sql)
print(cur.rowcount)
conn.commit()
"""






sql  ="select * from student"
print(cur.execute(sql))























