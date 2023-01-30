import pymongo
import logging

logging.basicConfig(filename='CRUDMongo_class.log', level=logging.DEBUG,
                    filemode='w', format="%(asctime)s %(levelname)s %(message)s")


class CRUDMongo:
    """
    class for perform the creation, read, update and delete operations on data with MONGO DB
    """

    def __init__(self):
        # setting connection
        logging.info("CONNECTING TO DATABASE    ")
        client = pymongo.MongoClient(
            "mongodb+srv://kalyan:Kalyan123@cluster0.scrii35.mongodb.net/?retryWrites=true&w=majority")
        db = client.test

        # create database if not exist
        logging.info("CREATING DB IF NOT EXIST")
        database = client['task']

        # creating table with fields in the file
        logging.info("CREATING TABLE IF NOT EXIST")
        self.collection = database['user']

    def insert_data(self):
        try:
            logging.info("INSERTING DATA INTO DATABASE")
            id = int(input("Enter ID: "))
            fname = input("Enter First name: ")
            lname = input("Enter Last name: ")
            cname = input("Enter Course name: ")
            cno = int(input("Enter Contact Number: "))
            data = {
                'id': id,
                'first_name': fname,
                'last_name': lname,
                'course': cname,
                'contact_no': cno,
            }
            self.collection.insert_one(data)
            logging.info("DATA INSERTED")
            print("Data Inserted Successfully!")
            pass
        except pymongo.errors.OperationFailure as err:
            logging.error("There is some error")
            print("Something went wrong: {}".format(err))

    def get_all_data(self):
        try:
            logging.info("FETCHING ALL DATA FROM DB")
            data = self.collection.find()
            print("All Data Fetched Successfully!")
            print("######  The Data  ######")
            for i in data:
                print(i, sep=" , ")
            logging.info("FETCHED ALL DATA FROM DB")
        except pymongo.errors.OperationFailure as err:
            logging.error("There is some error")
            print("Something went wrong: {}".format(err))

    def get_specific_data(self):
        try:
            logging.info("FETCHING SPECIFIC DATA FROM DB")
            id = int(input("Enter ID: "))
            data = self.collection.find({'id': id})
            print("Data Fetched Successfully!")
            print("######  The Data  ######")
            for i in data:
                print(i, sep=" , ")
            logging.info("FETCHED SPECIFIC DATA FROM DB")
        except pymongo.errors.OperationFailure as err:
            logging.error("There is some error")
            print("Something went wrong: {}".format(err))

    def update_data(self):
        try:
            logging.info("UPDATING SPECIFIC RECORD IN DB")
            id = int(input("Enter ID To Update Data: "))
            data = self.collection.find({'id': id})
            if data:
                print(f"###  Data Found of ID: {id}  ###")
                for i in data:
                    print(i)
                fnm = input("Enter New First Name To Update: ")
                lnm = input("Enter New Last Name To Update: ")
                cnm = input("Enter New Course Name To Update: ")
                mno = int(input("Enter New Mo.No. To Update: "))
                self.collection.update_one({"id": id}, {"$set": {
                                           "first_name": fnm, "last_name": lnm, "course": cnm, "contact_no": mno}})
                print("Data Updated Successfully!")
                logging.info("UPDATED RECORD IN DB")
        except pymongo.errors.OperationFailure as err:
            logging.error("There is some error")
            print("Something went wrong: {}".format(err))

    def delete_specific_record(self):
        try:
            logging.info("DELETING SPECIFIC RECORD FROM DB")
            id = int(input("Enter ID To Delete Data: "))
            data = self.collection.find({'id': id})
            if data:
                print(f"###  Data Found of ID: {id}  ###")
                for i in data:
                    print(i)
                print("Are Sure Want to Delete This Record?")
                choice = input("Enter (Yes/No): ")
                if choice.lower() == 'yes':
                    self.collection.delete_one({"id": id})
                    print("Data Deleted Successfully!")
                    logging.info("DELETED SPECIFIC RECORD IN DB")
                else:
                    print("Cancelled! No Record Deleted!")
        except pymongo.errors.OperationFailure as err:
            logging.error("There is some error")
            print("Something went wrong: {}".format(err))


instance = CRUDMongo()
print("Choose Operation To Be Performed: ")
print("Insert Record Into Database => 1")
print("Get All Data From DB => 2 ")
print("Get Specific Data From DB => 3 ")
print("Update Specific Data => 4 ")
print("Delete Specific Record => 5")

choice = int(input("Enter Option => "))
if choice == 1:
    instance.insert_data()
elif choice == 2:
    instance.get_all_data()
elif choice == 3:
    instance.get_specific_data()
elif choice == 4:
    instance.update_data()
elif choice == 5:
    instance.delete_specific_record()
else:
    print("Invalid Input")
