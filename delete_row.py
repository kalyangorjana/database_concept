import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

myCursor = mydb.cursor()

myCursor.execute("delete from gktech.student_details where firstname = 'siva'")
mydb.commit()

print("__________Delete Row__________")
myCursor.execute("select * from gktech.student_details")
for i in myCursor:
    print(i)
  
# To delete the all data ,remove the condition.