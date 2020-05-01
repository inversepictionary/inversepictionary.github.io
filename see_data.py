
import json
import time

with open('inversepictionary-export.json') as f:
  data = json.load(f)

for key, val in data['Descriptions'].items():
    print(val['user_ID'])
    print(val['description'])
    time.sleep(1)

print(len([key for key, val in data['Descriptions'].items()]))
print(len([key for key, val in data['Drawings'].items()]))