import pymongo
import logging

logging.basicConfig(filename='import_data.log', level=logging.DEBUG,
                    filemode='w', format="%(asctime)s %(levelname)s %(message)s")

class mongo_to_file:
    """
    class for perform data import to file form MONGO DB
    """
    def __init__(self,db,table):
        self.db_name = db
        self.table_name = table
        # setting connection
        logging.info("CONNECTING TO DATABASE    ")
        client = pymongo.MongoClient(
            "mongodb+srv://kalyan:Kalyan123@cluster0.scrii35.mongodb.net/?retryWrites=true&w=majority")
        db = client.test
        
        # create database if not exist
        logging.info("Searching for DB")
        database = client[self.db_name]

        # creating table with fields in the file
        logging.info("Serching for collection")
        self.collection = database[self.table_name]
    
    def import_data(self,file_name):
        try:
            logging.info("FETCHING ALL DATA FROM DB")
            data = self.collection.find()
            print("All Data Fetched Successfully!")
            with open(file_name+".json",'w') as f:
                for i in data:
                    f.write(str(i)+",")
        except pymongo.errors.OperationFailure as err:
            logging.error("There is some error")
            print("Something went wrong: {}".format(err))
        except FileNotFoundError as err2:
            logging.error(err2)

mf = mongo_to_file("Employee","course")
mf.import_data("new")