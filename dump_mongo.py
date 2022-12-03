import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
#data file path
DATA_PATH = "/config/workspace/aps_failure_training_set1.csv"
Data_Base_Name = "aps"
Collection_Name = "sensor"


if __name__ =="__main__":
     df = pd.read_csv(DATA_PATH)
     df.reset_index(drop=True, inplace=True)
     json_record = list(json.loads(df.T.to_json()).values())
     client[Data_Base_Name][Collection_Name].insert_many(json_record)

