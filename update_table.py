import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

myCursor = mydb.cursor()

myCursor.execute("update gktech.student_details set team = 'Full stack Java' where firstname = 'praveen'")
mydb.commit()

print("__________Updated List__________")
myCursor.execute("select * from gktech.student_details")
for i in myCursor:
    print(i)