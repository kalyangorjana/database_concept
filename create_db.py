import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

print(mydb.is_connected())
myCursor = mydb.cursor()
myCursor.execute("create database gktech")