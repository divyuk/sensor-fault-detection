import pymongo
import os
from sensor.constant.database import DATABASE_NAME
from sensor.constant.env_variable import MONGODB_URL_KEY
import certifi
ca = certifi.where()
import pandas as pd
class MongoDBClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url  = os.getenv(MONGODB_URL_KEY)
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise e
    
    def check(self):
        db = self.database
        print(db)
        # Collection Name
        col = db["car"]
        #  Find All: It works like Select * query  of SQL. 
        df = pd.DataFrame(list(col.find()))
        print(df.head())
        
if __name__ == "__main__":
    m = MongoDBClient()
    print(m.check())