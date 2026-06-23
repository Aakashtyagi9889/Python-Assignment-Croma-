# import mysql.connector;
# #  In this library we have the method connect which help to connect the python to mysql ==> connect()

# conn = mysql.connector.connect(
#     host = 'localhost',
#     port = '3306',
#     username = 'root',
#     password = 'aaka0505',
#     database = 'cromacampus'
#     )
# print(conn)

# # cursor() is the method which helps to write the query in python to database
# cur = conn.cursor()


# #==========================================IT IS MANDOTORY ===========================================
# """
# sql  = "CREATE DATABASE cromaCampus"
# cur.execute(sql)


# sql = '''
# Create TABLE student(
# sid int primary key auto_increment,
# sname varchar(30),
# sadd text,
# email text
# )
# '''
# cur.execute(sql)

# INSERT VALUES---
# sql =  "insert into student values(101 , 'Aakash' , 'Ghazaiabad' , 'a.gmail.com')"  
# cur.execute(sql)
# print(cur.rowcount)
# conn.commit()
# """






# sql  ="select * from student"
# print(cur.execute(sql))






import mysql.connector;
conn = mysql.connector.connect(
    host = "localhost",
    password = "aaka0505",
    port = "3306",
    username = "root",
    database = "db_connectivity"
    )
cur = conn.cursor()





sql = """insert into student values
(101 , 'Aakash' , 24000.26),
(102 , 'avi ' , 25000.26),
(102 , 'Abhay Tyagi ' , 24000.26)

"""

sql  =  "select * from student"
cur.execute(sql)
data =  cur.fetchall()


for a in data:
    print("Student Id : " , a[0])
    print("Student Name : " ,a[1])
    print("Student Salary : " ,a[2])
    print("--------------------------")



sql  =  "drop database db_connectivity"
cur.execute(sql)



















