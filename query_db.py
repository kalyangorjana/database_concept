import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

myCursor = mydb.cursor()

# select all columns
print("__________First Query Response__________")
myCursor.execute("select * from gktech.student_details")
for i in myCursor:
    print(i)

# select purticular column
print("__________Second Query Response__________")
myCursor.execute("select studentID,firstname from gktech.student_details")
for i in myCursor:
    print(i)

# select purticular row(Where)
print("__________Third Query Response__________")
myCursor.execute("select * from gktech.student_details where studentID = 125")
for i in myCursor:
    print(i)

# select purticular row(Comparison Operator)
print("__________fourth Query Response__________")
myCursor.execute("select * from gktech.student_details where studentID < 125")
for i in myCursor:
    print(i)

# select purticular row(and)
print("__________fifth Query Response__________")
myCursor.execute("select * from gktech.student_details where studentID < 125 and firstname = 'kalyan'")
for i in myCursor:
    print(i)
