import argparse
import csv
import json
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-csv')
parser.add_argument('-json')
arguments = parser.parse_args()

data = {}
with open(arguments.csv) as user_details:
    reader = csv.DictReader(user_details)
    for row in reader:
        user_id = row['user_id']
        data[user_id] = row
        data[user_id]["password"] = "null"
        with open(arguments.json,'w') as user_details_json:
            user_details_json.write(json.dumps(data, indent = 2))
