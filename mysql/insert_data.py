import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

print(mydb.is_connected())
myCursor = mydb.cursor()
myCursor.execute("insert into gktech.student_details values(123,'kalyan','gorjana','2022-09-11','Data Scientist'),(124,'saikrishna','munjeti','2022-09-09','Data Scientist'),(125,'praveen','behara','2022-09-10','Data Scientist'),(126,'gani','setti','2022-09-10','Data Scientist'),(127,'siva','varanasi','2022-10-10','Data Scientist')")
# need to commit the while change or modify the data in the database
# if you get error in the query string then add triple quotes to the string.
mydb.commit()


