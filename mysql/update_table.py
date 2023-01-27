import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

myCursor = mydb.cursor()

myCursor.execute("update gktech.student_details set team = 'Full stack Java' where firstname = 'saikrishna'")
mydb.commit()

#update  between
myCursor.execute("update gktech.student_details set team = 'Mango DB' where studentID between 124 and 126")
mydb.commit()
print("__________Updated List__________")
myCursor.execute("select * from gktech.student_details")
for i in myCursor:
    print(i)