import logging
import mysql.connector as conn

import csv

logging.basicConfig(filename="sql_bulk_upload.log", level=logging.DEBUG, filemode='w', format = "%(asctime)s %(levelname)s %(message)s")

class MySQL_Bulk_Upload():
    
    def __init__(self, host, user, password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        
    def create_connection(self):
        try:
            mydb = conn.connect(host = self.host, user = self.user, passwd = self.password, database = self.database)
            cursor = mydb.cursor()
            self.mydb = mydb
            self.cursor = cursor
            logging.info("Connection to DB successful")
            print("Connection to DB successful")
        except Exception as e:
            logging.error("Exception occurred", e)
        
        
    def create_table(self, table_name, columns):
        try:
            self.table_name = table_name
            self.columns = columns
            self.cursor.execute(f"CREATE TABLE if not exists {self.table_name}({self.columns})")
            self.mydb.commit()
            logging.info("table has created")
            print("Table has created")
        except Exception as e:
            logging.error("Exception occurred", e)
        
    def insert_data(self,csv_file):
        try:
            with open(csv_file, "r") as f:
                data  = csv.reader(f, delimiter = '\n')
                next(data)
                for i in data:
                    self.cursor.execute(f'insert into {self.database}.{self.table_name} values({str(i[0])})')
            self.mydb.commit()
            logging.info("Bulk Upload is successful")
        
        except Exception as e:
            print(e)
            logging.error("Exception occurred",e)
                   
        
    def show_data(self):
        try:
            self.cursor.execute(f"SELECT * from {self.table_name}")
            logging.info("Showing Data from table is successful")
            print(self.cursor.fetchall())
        except Exception as e:
            logging.error("Exception occurred", e)

obj = MySQL_Bulk_Upload("localhost", "abc", "password", "gktech")

obj.create_connection()

obj.create_table("glassdata2", "col1 INT(10), col2 float(30,10), col3 float(30,10), col4 float(30,10), col5 float(30,10), col6 float(30,10), col7 float(30,10), col8 float(30,10), col9 float(30,10), col10 float(30,10), col11 INT(10)")

obj.insert_data("/config/workspace/mysql/glass.csv")
