import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

print(mydb.is_connected())
myCursor = mydb.cursor()
myCursor.execute("create table gktech.student_details(studentID int,firstname varchar(30),lastname varchar(30),registrationdate date,team varchar(30))")
