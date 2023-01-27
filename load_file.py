import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password",
  database = "gktech"
)

mycursor = mydb.cursor()
# Create a table
mycursor.execute("CREATE TABLE customers (index float, RI float,Na float,Mg flaot,Al float,Si float,K float,Ca float,Ba float,Fe float,Class float)")

# Load data from a text file
mycursor.execute("LOAD DATA LOCAL INFILE 'glass.data' INTO TABLE customers FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'")