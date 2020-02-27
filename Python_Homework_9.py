import csv
import json
import pymongo


myclient = pymongo.MongoClient()
dblist = myclient.list_database_names()

for name in dblist:
    if name == 'test':
        myclient.drop_database('test')
    
mydb = myclient["test"]

col_proj = mydb.create_collection("project")
col_tasks = mydb.create_collection("tasks")


csv_tasks = 'C:/Users/vic/Python/tasks.csv'
csv_proj = 'C:/Users/vic/Python/project.csv'

def to_mongo(csv_filepath, col_name):
    with open(csv_filepath, 'r') as csvfile:
        with open('tmp.json', 'w') as jsonfile:
            json.dump(list(csv.DictReader(csvfile)), jsonfile)
            
    with open('tmp.json', "r") as file:
        for row in json.load(file):      
            col_name.insert_one(row)

if __name__ == '__main__':
    to_mongo(csv_tasks, col_tasks)
    to_mongo(csv_proj, col_proj)
    for row in col_tasks.find({"status": "canceled"}):
        print (row)
