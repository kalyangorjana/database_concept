import pymongo
class mongodb:
    def __init__(self,userid,password):
        self.userid = userid
        self.password = password

    def connection(self):
        """To build connection"""
        client = pymongo.MongoClient("mongodb+srv://"+self.userid+":"+self.password+"@cluster0.scrii35.mongodb.net/?retryWrites=true&w=majority")
        db = client.test
        print(db)
        return client

    def get_data(self):
        """To get data form the db"""

    def insert_data(self,database,coll,data):
        """To insert data into the db"""
        client = self.connection()
        db = client[database]
        coll = db[coll]
        coll.insert_one(data)
        print("Insert sucessfully")

    def update_data(self):
        """To upadte data in the db"""

    def delete_data(self):
        """To delete data form the db"""

mdb = mongodb("kalyan", "Kalyan123")
mdb.insert_data("database", "coll", {'name' : 'kalyan' , 'number' : 345})