import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

print(mydb.is_connected())
myCursor = mydb.cursor()
myCursor.execute("create table gktech.emp_details(emp_id int,name varchar(30),salary int,team varchar(30))")
